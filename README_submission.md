# README_submission - Lab 17 (Vu Huu An - 2A202601078)

Practice **11/11 PASS**; **Golden 20/20 (+10)**; no-memory baseline 2/11 (xem `reports/`).

Bonus UI (`src/ui_server.py` + `ui/index.html`, Ant Design + GPT-5.6-Luna; Streamlit `demo_ui.py` cung da wire): case picker, evidence tung layer, budget meter, chat giu history dung user/thread (`submission/ui_*.png`).

## 3 cau thuc hanh

**1. Layer quan trong nhat trong bo test nay:** long-term - nhieu case nhat (E02, E03, E08, E09) va E07 mixed cung phu thuoc no; sai TODO 1 la mat 5/11 case. No ganh 2 tinh chat kho nhat: recency (E08) va isolation (E09).

**2. Trade-off Zep vs Redis+Qdrant:** Zep lo tron extraction, temporal graph (valid_at/invalid_at), conflict/recency, Context Block lap san; doi lai ton API, ingestion bat dong bo (phai poll, ~1.1-1.8s/query) va it kiem soat schema. Redis+Qdrant re, nhanh, kiem soat het nhung phai tu build extraction, conflict, provenance, deletion - de sai isolation.

**3. Guardrail chong memory poisoning:** (a) consent gate + PII minimization truoc durable write (`privacy_guard.py`); (b) heartbeat chi de-dup/mark stale/recap, khong tu them instruction hay quyen moi (`AGENTS.md`); (c) record giu provenance (source, timestamp, confidence) de audit/rollback; (d) high-impact update can review truoc write-back.

## 4 cau phan tich benchmark

**1. Layer hit rate thap nhat:** khong co - moi layer 100%. Mong manh nhat la long-term: latency cao nhat va reduction 0% do append bonus edges.

**2. Case retrieve nhieu token nhat:** E08 (1602 tokens; E02 1601, E03 1597) - long-term vi Context Block + 30 edge facts.

**3. E07 mixed:** long-term (**Python** - preference cua Minh) + semantic (**Idempotency-Key** - shared KB). Thieu mot trong hai la FAIL.

**4. Reduction vs hit rate:** no-memory reduction 81.8% nhung hit 18.2% - khong retrieve gi nen "giam token" ma sai gan het; student reduction ~21% nhung hit 100%. Reduction chi co nghia khi kem hit rate.

## E08 recency & E10 compaction

**E08:** update stage 3 tao fact moi scoped theo BLUEBIRD-42 (TypeScript/NestJS); fact Python cu khong bi xoa ma gan invalid_at, van dung cho ORCHID-27 - recency + scope thay vi ghi de.

**E10:** compaction evict raw turns nhung durable notes giu nguyen REVIEW-DEADLINE-1600/Friday/16:00 ke ca khi K giam 6 xuong 4. Mo rong: 5 chien luoc trong `reports/strategy_comparison.md` - window-only mat deadline (0/3), hybrid pin constraint lossless.

**Bai hoc golden:** long eval query bi luu thanh episode gay nhieu; fix G18: rank episode mang marker len truoc khi trim budget.
