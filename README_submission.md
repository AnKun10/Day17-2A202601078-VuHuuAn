# README_submission - Lab 17 (Vu Huu An - 2A202601078)

Practice **11/11 PASS**; **Golden 20/20 (+10)** (ca v2 va v3); no-memory baseline 2/11 (xem `reports/`).

Bonus UI (`src/ui_server.py` + `ui/index.html`, Ant Design + GPT-5.6-Luna; Streamlit cung da wire): case picker, evidence tung layer, budget meter, chat giu history (`submission/ui_*.png`).

## 3 cau thuc hanh

**1. Layer quan trong nhat trong bo test nay:** long-term - nhieu case nhat (E02, E03, E08, E09) va E07 mixed cung phu thuoc no; sai TODO 1 la mat 5/11 case; kem theo recency (E08) va isolation (E09).

**2. Trade-off Zep vs Redis+Qdrant:** Zep lo tron extraction, temporal graph (valid_at/invalid_at), conflict/recency, Context Block lap san; doi lai ton API, ingestion bat dong bo (phai poll, retrieve ~1.5-1.9s) va it kiem soat schema. Redis+Qdrant re, nhanh, kiem soat het nhung phai tu build extraction, conflict, provenance, deletion - de sai isolation.

**3. Guardrail chong memory poisoning:** (a) consent gate + PII minimization truoc durable write (`privacy_guard.py`); (b) heartbeat chi de-dup/mark stale/recap, khong tu them instruction hay quyen moi (`AGENTS.md`); (c) record giu provenance de audit/rollback; (d) high-impact update can review truoc write-back.

## 4 cau phan tich benchmark

**1. Layer hit rate thap nhat:** khong co - moi layer 100%. Mong manh nhat la long-term: latency cao nhat va reduction 0% do append bonus edges.

**2. Case retrieve nhieu token nhat:** E02 (1819 tokens; E08 1771, E03 1736) - long-term vi Context Block + 30 edge facts + marker notes.

**3. E07 mixed:** long-term (**Python** - preference cua Minh) + semantic (**Idempotency-Key** - shared KB). Thieu mot trong hai la FAIL.

**4. Reduction vs hit rate:** no-memory reduction 81.8% nhung hit 18.2% - vi khong retrieve gi; student reduction 18.8% nhung hit 100%. Reduction chi co nghia khi kem hit rate.

## E08 recency & E10 compaction

**E08:** update stage 3 tao fact moi scoped theo BLUEBIRD-42 (TypeScript/NestJS); fact Python cu khong bi xoa ma gan invalid_at, van dung cho ORCHID-27 - recency + scope.

**E10:** compaction evict raw turns nhung durable notes giu nguyen REVIEW-DEADLINE-1600/Friday/16:00 ke ca khi K giam 6 xuong 4. So sanh 5 chien luoc: `reports/strategy_comparison.md` (window-only mat deadline 0/3).

**Bai hoc golden (v2+v3):** (1) eval query thanh episode nhieu - rank marker-episode len dau; (2) Zep extract roi ma literal - pin dong MARKERS dau long-term; (3) KB doc co 2 ban JSON/text - dedupe de 4 doc lot budget.
