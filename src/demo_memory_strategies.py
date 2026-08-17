"""Extra (student-added) demo: compare context-management strategies.

The starter kit ships three strategies in src/short_term.py (buffer, summary,
sliding). This demo adds two more implemented HERE (the starter files are
locked by pytest, so nothing outside this new file is modified):

- window-only : naive sliding window - keep ONLY the last K turns, no summary,
                no durable notes. Shows WHY the lab's sliding strategy needs
                durable notes: old constraints silently fall off the window.
- hybrid      : priority eviction - durable/constraint messages are pinned
                verbatim, filler turns are evicted first, and only the evicted
                filler is summarized. No lossy compression of constraints.

All five strategies replay the same message stream (the E10 fixture: one
deadline constraint followed by filler turns) at K=6 and K=4, then we check
whether the REVIEW-DEADLINE-1600 constraint survived and how many tokens the
rendered context costs.

Run:
    docker compose run --rm app python -m src.demo_memory_strategies

Writes: reports/strategy_comparison.md
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from rich.console import Console
from rich.table import Table

from .config import ROOT
from .short_term import DURABLE_PATTERNS, ChatMessage, ShortTermMemory
from .utils import estimate_tokens

console = Console()

# Same constraint + filler shape as the graded E10 fixture, extended to 30
# turns so the token growth of `buffer` is visible.
MESSAGES = [
    ("user", "Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten."),
    ("assistant", "Acknowledged review constraint."),
] + [
    ("user" if i % 2 else "assistant", f"Filler turn {i} about an already-resolved detail.")
    for i in range(1, 29)
]

REQUIRED_MARKERS = ("REVIEW-DEADLINE-1600", "Friday", "16:00")


def _is_durable(text: str) -> bool:
    low = text.casefold()
    has_marker = bool(re.search(r"\b[A-Z][A-Z0-9-]{5,}\b", text))
    return any(p in low for p in DURABLE_PATTERNS) or has_marker


@dataclass
class WindowOnlyMemory:
    """Naive sliding window: last K turns, nothing else survives."""

    max_recent_messages: int = 6
    messages: list[ChatMessage] = field(default_factory=list)
    compactions: int = 0

    def add(self, role: str, content: str) -> None:
        self.messages.append(ChatMessage(role=role, content=content))
        if len(self.messages) > self.max_recent_messages:
            self.messages = self.messages[-self.max_recent_messages:]
            self.compactions += 1

    def render(self) -> str:
        return "\n".join(f"{m.role}: {m.content}" for m in self.messages)

    def stats(self) -> dict[str, int]:
        return {
            "messages_kept": len(self.messages),
            "compactions": self.compactions,
            "estimated_tokens": estimate_tokens(self.render()),
        }


@dataclass
class PriorityEvictionMemory:
    """Hybrid: pin durable messages verbatim, evict filler first.

    Compared to the lab's sliding strategy (which compresses old turns into an
    extractive summary), this keeps constraints lossless and only summarizes
    the disposable filler it evicts - trading a slightly larger pinned section
    for zero risk of mangling a constraint during summarization.
    """

    max_recent_messages: int = 6
    max_pinned: int = 8
    pinned: list[ChatMessage] = field(default_factory=list)
    recent: list[ChatMessage] = field(default_factory=list)
    evicted_summary: str = ""
    compactions: int = 0

    def add(self, role: str, content: str) -> None:
        self.recent.append(ChatMessage(role=role, content=content))
        if len(self.recent) > self.max_recent_messages:
            evicted = self.recent[: -self.max_recent_messages]
            self.recent = self.recent[-self.max_recent_messages:]
            for msg in evicted:
                if _is_durable(msg.content):
                    if all(p.content != msg.content for p in self.pinned):
                        self.pinned.append(msg)
                        self.pinned = self.pinned[-self.max_pinned:]
                else:
                    snippet = f"{msg.role}: {msg.content[:60]}"
                    self.evicted_summary = (self.evicted_summary + " | " + snippet)[-600:]
            self.compactions += 1

    def render(self) -> str:
        parts: list[str] = []
        if self.pinned:
            parts.append(
                "<PINNED_CONSTRAINTS>\n"
                + "\n".join(f"- {m.role}: {m.content}" for m in self.pinned)
                + "\n</PINNED_CONSTRAINTS>"
            )
        if self.evicted_summary:
            parts.append(f"<EVICTED_SUMMARY>\n{self.evicted_summary}\n</EVICTED_SUMMARY>")
        if self.recent:
            parts.append(
                "<RECENT_TURNS>\n"
                + "\n".join(f"{m.role}: {m.content}" for m in self.recent)
                + "\n</RECENT_TURNS>"
            )
        return "\n".join(parts)

    def stats(self) -> dict[str, int]:
        return {
            "messages_kept": len(self.recent) + len(self.pinned),
            "compactions": self.compactions,
            "estimated_tokens": estimate_tokens(self.render()),
        }


def build_memory(strategy: str, k: int):
    if strategy in ("buffer", "summary", "sliding"):
        return ShortTermMemory(strategy=strategy, max_recent_messages=k, pressure_tokens=300)
    if strategy == "window-only":
        return WindowOnlyMemory(max_recent_messages=k)
    if strategy == "hybrid":
        return PriorityEvictionMemory(max_recent_messages=k)
    raise ValueError(strategy)


def run_one(strategy: str, k: int) -> dict[str, object]:
    memory = build_memory(strategy, k)
    for role, content in MESSAGES:
        memory.add(role, content)
    rendered = memory.render()
    survived = [m for m in REQUIRED_MARKERS if m.casefold() in rendered.casefold()]
    stats = memory.stats()
    return {
        "strategy": strategy,
        "k": k,
        "tokens": stats["estimated_tokens"],
        "kept": stats["messages_kept"],
        "compactions": stats.get("compactions", 0),
        "deadline_ok": len(survived) == len(REQUIRED_MARKERS),
        "survived": survived,
        "rendered": rendered,
    }


NOTES = {
    "buffer": "Giu tat ca: khong bao gio mat constraint nhung token tang tuyen tinh theo so turn.",
    "window-only": "Chi giu K turn cuoi: re nhat nhung constraint cu RoI khoi window -> mat deadline.",
    "summary": "Nen turn cu thanh extractive summary: giu duoc constraint neu summarizer nhan ra no.",
    "sliding": "Summary + durable notes + K turn gan nhat (default cua lab): constraint song trong durable notes.",
    "hybrid": "Pin constraint nguyen van, evict filler truoc, chi summarize filler: lossless voi constraint.",
}


def main() -> None:
    strategies = ("buffer", "window-only", "summary", "sliding", "hybrid")
    results = [run_one(s, k) for k in (6, 4) for s in strategies]

    table = Table(title=f"Context strategies on the E10-style stream ({len(MESSAGES)} turns)")
    for col, justify in (
        ("Strategy", "left"), ("K", "right"), ("Tokens", "right"),
        ("Msgs kept", "right"), ("Compactions", "right"), ("Deadline survives?", "left"),
    ):
        table.add_column(col, justify=justify)
    for r in results:
        table.add_row(
            str(r["strategy"]), str(r["k"]), str(r["tokens"]), str(r["kept"]),
            str(r["compactions"]),
            "[green]YES[/green]" if r["deadline_ok"] else f"[red]NO[/red] ({len(r['survived'])}/3)",
        )
    console.print(table)

    report = Path(ROOT) / "reports" / "strategy_comparison.md"
    report.parent.mkdir(exist_ok=True)
    lines = [
        "# Short-term context strategies - comparison (student extension)",
        "",
        f"Stream: 1 deadline constraint (`REVIEW-DEADLINE-1600`, Friday, 16:00) + filler, {len(MESSAGES)} turns total.",
        "PASS = all 3 markers still present in the rendered context after the whole stream.",
        "",
        "| Strategy | K | Est. tokens | Msgs kept | Compactions | Deadline survives |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for r in results:
        ok = "PASS" if r["deadline_ok"] else f"FAIL ({len(r['survived'])}/3)"
        lines.append(
            f"| {r['strategy']} | {r['k']} | {r['tokens']} | {r['kept']} | {r['compactions']} | {ok} |"
        )
    lines += ["", "## Ghi chu tung chien luoc", ""]
    for name in strategies:
        lines.append(f"- **{name}**: {NOTES[name]}")
    lines += [
        "",
        "## Bai hoc",
        "",
        "1. `buffer` khong bao gio quen nhung chi phi token tang tuyen tinh - khong scale.",
        "2. `window-only` cho thay sliding window NGAY THO la nguy hiem: constraint cu roi khoi window va bien mat.",
        "3. `summary` re hon buffer nhung lossy - constraint chi song neu summarizer trich dung no.",
        "4. `sliding` (default cua lab) = summary + durable notes + recent turns: compaction khong phai 'tom tat van hoa',",
        "   ma la giu state/decision/TODO/constraint co chu dich (E10 pass nho durable notes, ke ca khi K giam 6 -> 4).",
        "5. `hybrid` di xa hon: pin constraint nguyen van (lossless), chi summarize filler bi evict -",
        "   doi them mot it token co dinh lay su chac chan rang constraint khong bi bien dang.",
        "",
    ]
    report.write_text("\n".join(lines), encoding="utf-8")
    console.print(f"Report written to {report}")

    console.print("\n[bold]Rendered context at K=4 (the graded variation):[/bold]")
    for r in results:
        if r["k"] == 4 and r["strategy"] in ("window-only", "sliding", "hybrid"):
            console.rule(str(r["strategy"]))
            console.print(str(r["rendered"]))


if __name__ == "__main__":
    main()
