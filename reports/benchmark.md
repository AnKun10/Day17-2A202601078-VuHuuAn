# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **932.3 ms**
- Average token reduction vs full source context: **18.7%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| E06 | semantic | PASS | 492.5 | 60 | 86.9% |  |
| E09 | long_term | PASS | 1675.8 | 802 | 0.0% |  |
| E10 | short_term | PASS | 0.5 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1887.9 | 1819 | 0.0% |  |
| E03 | long_term | PASS | 1929.2 | 1736 | 0.0% |  |
| E04 | episodic | PASS | 260.4 | 372 | 0.0% |  |
| E05 | episodic | PASS | 272.2 | 356 | 0.0% |  |
| E07 | mixed | PASS | 1852.6 | 396 | 29.9% |  |
| E11 | semantic | PASS | 252.8 | 60 | 89.4% |  |
| E08 | long_term | PASS | 1631.2 | 1771 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: Payment API Retry Policy: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.`

### E09 - long_term

`MARKERS: LOTUS-88 NOTE: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. NOTE: Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. FACT: LOTUS-88 uses Java for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: LOTUS-88 uses Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran's project is LOTUS-88. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran does not use Python in the backend example. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Java. [valid_at=2026-08-01T11:00:00Z, inval`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`MARKERS: ORCHID-27, BLUEBIRD-42, LAB-REPORT-1600, ASYNC-FIX-20 NOTE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI NOTE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. NOTE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. FACT: Minh Nguyen does not like Java. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=None] FACT: Minh Nguyen still prefers Python for personal demos for`

### E03 - long_term

`MARKERS: ORCHID-27, BLUEBIRD-42, LAB-REPORT-1600, ASYNC-FIX-20 NOTE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. FACT: Minh Nguyen increased the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen has a todo to complete the benchmark report before Friday at 16:00. [valid_at=2026-08-01T09:04:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FAC`

### E04 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? Chi preference cua Minh, dung tron so thich dong nghiep. EPISODE: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playbook truoc khi tang tim`

### E05 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? Chi preference cua Minh, dung tron so thich dong nghiep. EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon`

### E07 - mixed

`<LONG_TERM> MARKERS: ORCHID-27, BLUEBIRD-42, LAB-REPORT-1600, ASYNC-FIX-20 NOTE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=None] FACT: Minh Nguyen still prefers Python for personal demos for project ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen does not like Java. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] F`

### E11 - semantic

`EPISODE: Async HTTP Incident Playbook: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.`

### E08 - long_term

`MARKERS: ORCHID-27, BLUEBIRD-42, LAB-REPORT-1600, ASYNC-FIX-20 NOTE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI FACT: The project BLUEBIRD-42 requires TypeScript for the backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: The project BLUEBIRD-42 requires NestJS for the backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Python is prohibited for the backend of the project BLUEBIRD-42. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Da tach scope BLUEBIRD-42 uses TypeScript/NestJS. [valid_at=2026`
