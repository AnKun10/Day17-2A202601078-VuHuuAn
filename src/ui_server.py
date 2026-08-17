"""Bonus mini-product UI backend (student-added, Ant Design frontend).

Serves `ui/index.html` (React + Ant Design v5) plus a small JSON API on the
same origin. Retrieval logic is shared with the Streamlit demo: this server
calls `src.demo_ui.retrieve_for_case` (the BONUS TODO implementation) and the
grader's own `src.evaluate.score_case` for the PASS/FAIL marker check, so the
UI shows exactly what the benchmark scores.

Run (same port mapping as `make ui`):

    docker compose run --rm --service-ports app python -m src.ui_server
    # open http://localhost:8501

Endpoints:
    GET  /               -> ui/index.html
    GET  /api/cases      -> {cases, meta}
    POST /api/retrieve   -> {layers, merged_context, budget, check, latency_ms}
    POST /api/chat       -> retrieval for the chat turn + Gemini grounded reply
"""

from __future__ import annotations

import json
import os
import time
import traceback
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

from .config import ROOT, settings
from .demo_ui import load_cases, retrieve_for_case
from .evaluate import score_case
from .llm import SYSTEM_INSTRUCTION, gemini_available, generate_reply
from .memory_student import StudentMemory
from .zep_common import get_zep_client

UI_DIR = ROOT / "ui"
PORT = 8501

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

_client = None


def openai_available() -> bool:
    return bool(OPENAI_API_KEY)


def openai_reply(memory_context: str, history: list[dict[str, str]], user_message: str) -> str:
    """Grounded chat reply via the OpenAI Chat Completions REST API.

    Uses stdlib urllib so the starter requirements.txt stays untouched. The
    grounding format mirrors src/llm.py so both providers behave the same.
    """
    grounding = (
        "Retrieved memory context for this turn:\n"
        "-------------------------------------\n"
        f"{memory_context.strip() or '(no memory retrieved)'}\n"
        "-------------------------------------\n\n"
        f"User message: {user_message}"
    )
    messages = [{"role": "system", "content": SYSTEM_INSTRUCTION}]
    for msg in history:
        role = "user" if msg.get("role") == "user" else "assistant"
        if msg.get("content"):
            messages.append({"role": role, "content": msg["content"]})
    messages.append({"role": "user", "content": grounding})

    payload = json.dumps(
        {"model": OPENAI_MODEL, "messages": messages, "max_completion_tokens": 800}
    ).encode("utf-8")
    request = urllib.request.Request(
        f"{OPENAI_BASE_URL}/chat/completions",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        },
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        data = json.loads(response.read().decode("utf-8"))
    return (data["choices"][0]["message"]["content"] or "").strip()


def llm_reply(memory_context: str, history: list[dict[str, str]], user_message: str) -> str:
    """OpenAI first, Gemini as fallback, raw context as last resort."""
    errors: list[str] = []
    if openai_available():
        try:
            return openai_reply(memory_context, history, user_message)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"OpenAI: {exc}")
    if gemini_available():
        try:
            return generate_reply(memory_context, history, user_message)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Gemini: {exc}")
    note = "; ".join(errors) or "no LLM key configured"
    return (
        f"(LLM unavailable - {note})\n\nRetrieved memory context:\n"
        + (memory_context[:1500] or "(no memory retrieved)")
    )


def zep_client():
    global _client
    if _client is None:
        _client = get_zep_client()
    return _client


def find_case(case_id: str) -> dict[str, Any]:
    for case in load_cases():
        if case["id"] == case_id:
            return case
    raise KeyError(f"Unknown case id: {case_id}")


def run_retrieval(case: dict[str, Any], extra_messages: list[dict[str, str]]) -> dict[str, Any]:
    memory = StudentMemory(zep_client())
    started = time.perf_counter()
    result = retrieve_for_case(memory, case, extra_messages)
    latency_ms = round((time.perf_counter() - started) * 1000, 1)
    passed, missing, forbidden = score_case(case, result["merged_context"])
    return {
        **result,
        "latency_ms": latency_ms,
        "check": {
            "passed": passed,
            "missing": missing,
            "forbidden_found": forbidden,
            "must_contain_all": case.get("must_contain_all", []),
            "must_not_contain": case.get("must_not_contain", []),
        },
    }


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args: Any) -> None:
        print(f"[ui] {self.address_string()} {fmt % args}")

    def _send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path: Path, content_type: str) -> None:
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _read_body(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length") or 0)
        if not length:
            return {}
        return json.loads(self.rfile.read(length).decode("utf-8"))

    def do_GET(self) -> None:  # noqa: N802
        try:
            if self.path in ("/", "/index.html"):
                self._send_file(UI_DIR / "index.html", "text/html; charset=utf-8")
            elif self.path == "/api/cases":
                self._send_json(
                    {
                        "cases": load_cases(),
                        "meta": {
                            "zep_ok": bool(settings.zep_api_key),
                            "gemini_ok": openai_available() or gemini_available(),
                            "model": OPENAI_MODEL if openai_available() else settings.gemini_model,
                            "context_tokens": settings.context_tokens,
                        },
                    }
                )
            else:
                self._send_json({"error": "not found"}, status=404)
        except Exception as exc:  # noqa: BLE001
            traceback.print_exc()
            self._send_json({"error": f"{type(exc).__name__}: {exc}"}, status=500)

    def do_POST(self) -> None:  # noqa: N802
        try:
            body = self._read_body()
            case = find_case(body.get("case_id", ""))
            extra = body.get("extra_messages") or []

            if self.path == "/api/retrieve":
                self._send_json(run_retrieval(case, extra))
            elif self.path == "/api/chat":
                message = (body.get("message") or "").strip()
                history = body.get("history") or []
                result = run_retrieval({**case, "query": message}, history + [{"role": "user", "content": message}])
                context = result.get("merged_context", "")
                reply = llm_reply(context, history, message)
                self._send_json({**result, "reply": reply})
            else:
                self._send_json({"error": "not found"}, status=404)
        except KeyError as exc:
            self._send_json({"error": str(exc)}, status=404)
        except Exception as exc:  # noqa: BLE001
            traceback.print_exc()
            self._send_json({"error": f"{type(exc).__name__}: {exc}"}, status=500)


def main() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Lab 17 antd demo UI on http://localhost:{PORT}")
    print(
        "Zep:", "ok" if settings.zep_api_key else "MISSING",
        "| OpenAI:", OPENAI_MODEL if openai_available() else "missing",
        "| Gemini:", "ok" if gemini_available() else "missing",
    )
    server.serve_forever()


if __name__ == "__main__":
    main()
