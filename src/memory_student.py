from __future__ import annotations

import re
from types import SimpleNamespace
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search, safe_call


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
        parts = [getattr(context, "context", None) or ""]

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
        if edges is not None:
            parts.append(render_graph_search(edges))
        return join_nonempty(parts)

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
        #    codes, same regex as short_term durable notes) before verbose
        #    marker-less ones - long paraphrased eval queries stored as
        #    episodes would otherwise outrank the actual trajectory;
        # 2) cap each episode's length so more distinct episodes fit.
        marker_re = re.compile(r"\b[A-Z][A-Z0-9-]{5,}\b")
        episodes = list(getattr(results, "episodes", None) or [])
        episodes.sort(
            key=lambda e: 0 if marker_re.search(getattr(e, "content", "") or "") else 1
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
        text = render_graph_search(results)
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
