from __future__ import annotations

import json
import re
from types import SimpleNamespace
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty, normalize
from .zep_common import prime_eval_thread, render_graph_search, safe_call

# Durable lab markers look like ORCHID-27 / LAB-REPORT-1600: uppercase code,
# at least one hyphen, at least one digit. Requiring the hyphen+digit rejects
# plain uppercase words (BLUEBIRD, TODO, HTTP) that show up inside long noisy
# eval prompts stored as episodes.
MARKER_RE = re.compile(r"\b[A-Z][A-Z0-9]*-[A-Z0-9-]*\d\b")


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4 - long-term retrieval via the Zep Context Block.
        prime_eval_thread(self.client, user_id, thread_id, query)
        context = self.client.thread.get_user_context(thread_id=thread_id)

        # Bonus: edge facts carry valid_at/invalid_at validity ranges, which
        # surface deadline/open-loop facts the Context Block may summarize away.
        # A low limit can miss those facts, so ask for plenty.
        edges = safe_call(
            self.client.graph.search,
            user_id=user_id,
            query=cap_query(query),
            scope="edges",
            limit=30,
        )

        # Fact extraction can drop literal codes (a "finish the benchmark
        # report" fact loses LAB-REPORT-1600), so pull a few query-relevant
        # marker-bearing raw episodes as compact notes. The mixed-case budget
        # trim keeps only the HEAD of this text, so order by usefulness per
        # query: literal-marker notes, then query-ranked facts, then the broad
        # Context Block narrative.
        episodes = safe_call(
            self.client.graph.search,
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=6,
        )
        episode_texts: list[str] = []
        notes: list[str] = []
        for ep in (getattr(episodes, "episodes", None) or []) if episodes else []:
            content = (getattr(ep, "content", "") or "").strip()
            if not content:
                continue
            episode_texts.append(content)
            if MARKER_RE.search(content) and len(notes) < 3:
                notes.append("NOTE: " + content[:180])

        edge_text = render_graph_search(edges) if edges is not None else ""
        context_text = getattr(context, "context", None) or ""

        # Durable identifiers are the highest-value atoms of long-term memory,
        # and Zep's fact extraction sometimes drops them ("finish the
        # benchmark report" loses LAB-REPORT-1600). Mine every literal code
        # from the sources just retrieved (all user-scoped, so no cross-user
        # leak is possible) and pin them at the very head so the budget trim
        # can never cut an identifier away.
        markers: list[str] = []
        for found in MARKER_RE.findall("\n".join([context_text, edge_text, *episode_texts])):
            if found not in markers:
                markers.append(found)
        header = "MARKERS: " + ", ".join(markers[:12]) if markers else ""

        return join_nonempty([header, "\n".join(notes), edge_text, context_text])

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4 - user-scoped episode search (past trajectories).
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=8,
        )
        # Two defenses so marker-bearing reflections survive the tight
        # episodic budget (which keeps only the HEAD of the rendered text):
        # 1) rank episodes that carry durable markers (ASYNC-FIX-20 style
        #    codes) before verbose marker-less ones - long paraphrased eval
        #    queries stored as episodes would otherwise outrank the actual
        #    trajectory;
        # 2) cap each episode's length so more distinct episodes fit.
        episodes = list(getattr(results, "episodes", None) or [])
        episodes.sort(
            key=lambda e: 0 if MARKER_RE.search(getattr(e, "content", "") or "") else 1
        )
        ranked = SimpleNamespace(
            context=getattr(results, "context", None),
            edges=getattr(results, "edges", None),
            episodes=episodes,
            nodes=getattr(results, "nodes", None),
            observations=getattr(results, "observations", None),
            thread_summaries=getattr(results, "thread_summaries", None),
        )
        return render_graph_search(ranked, episode_char_cap=400)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4 - shared domain graph (graph_id, NOT user_id).
        # scope="episodes" returns raw document text that keeps literal markers
        # (e.g. PAYMENT-RULE-3); scope="auto" extracts facts and drops them.
        results = self.client.graph.search(
            graph_id=graph_id,
            query=cap_query(query),
            scope="episodes",
            limit=8,
        )
        # Each seeded document exists twice in the graph (a JSON episode and a
        # plain-text summary episode). Rendering both would let one document's
        # duplicate fill the tight semantic budget and push the next document
        # out entirely, so deduplicate on the summary text and keep one
        # compact line per document.
        lines: list[str] = []
        seen: set[str] = set()
        for ep in getattr(results, "episodes", None) or []:
            content = (getattr(ep, "content", "") or "").strip()
            if not content:
                continue
            entity, summary = "", content
            if content.startswith("{"):
                try:
                    doc = json.loads(content)
                    entity = str(doc.get("entity") or "")
                    summary = str(doc.get("summary") or content)
                except Exception:
                    pass
            key = normalize(summary)
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"EPISODE: {entity}: {summary}" if entity else f"EPISODE: {summary}")
        text = "\n".join(lines)
        if not text.strip():
            fallback = self.client.graph.search(
                graph_id=graph_id,
                query=cap_query(query),
                scope="nodes",
                limit=8,
            )
            text = render_graph_search(fallback)
        return text

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4 - enforce the 10/4/3/3 budget and STM>LT>EP>SEM priority.
        return self.budget.assemble(layers)
