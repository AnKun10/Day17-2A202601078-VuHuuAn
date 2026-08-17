# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1215.1 ms**
- Average token reduction vs full source context: **13.1%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.6 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | PASS | 1804.8 | 793 | 0.0% |  |
| G09 | semantic | PASS | 259.9 | 167 | 63.6% |  |
| G10 | semantic | PASS | 267.9 | 107 | 76.7% |  |
| G14 | mixed | PASS | 1832.5 | 444 | 0.0% |  |
| G03 | long_term | PASS | 1671.8 | 1842 | 0.0% |  |
| G04 | long_term | PASS | 1625.5 | 1858 | 0.0% |  |
| G07 | episodic | PASS | 271.2 | 243 | 0.0% |  |
| G08 | episodic | PASS | 272.2 | 244 | 0.0% |  |
| G11 | mixed | PASS | 1875.6 | 453 | 19.8% |  |
| G13 | mixed | PASS | 516.0 | 426 | 24.6% |  |
| G15 | mixed | PASS | 2140.9 | 757 | 0.0% |  |
| G16 | mixed | PASS | 1870.4 | 503 | 11.0% |  |
| G17 | mixed | PASS | 1905.8 | 503 | 11.0% |  |
| G18 | mixed | PASS | 481.9 | 423 | 25.1% |  |
| G19 | mixed | PASS | 1827.1 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1541.3 | 1824 | 0.0% |  |
| G12 | mixed | PASS | 1823.9 | 444 | 29.8% |  |
| G20 | mixed | PASS | 2312.4 | 623 | 1.4% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`MARKERS: LOTUS-88 NOTE: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. NOTE: Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. FACT: Lan Tran does not use Python in the backend example. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: LOTUS-88 uses Java for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran prioritizes Spring Boot. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Java. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: LOTUS-88 uses Spring Boot for backend examples. [valid_at=2026-08-0`

### G09 - semantic

`EPISODE: Payment API Retry Policy: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. EPISODE: Agent Memory Privacy Rule: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Memory Context Budget: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G10 - semantic

`EPISODE: Agent Memory Privacy Rule: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Memory Context Budget: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G14 - mixed

`<LONG_TERM> MARKERS: LOTUS-88 NOTE: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. NOTE: Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. FACT: Lan Tran does not use Python in the backend example. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: LOTUS-88 uses Java for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: LOTUS-88 uses Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran's project is LOTUS-88. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Spring Boot. [valid_at=2026-08-`

### G03 - long_term

`MARKERS: ORCHID-27, LAB-REPORT-1600, ASYNC-FIX-20, BLUEBIRD-42 NOTE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. NOTE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. NOTE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI FACT: Minh Nguyen still prefers Python for personal demos for project ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z,`

### G04 - long_term

`MARKERS: ORCHID-27, LAB-REPORT-1600, ASYNC-FIX-20, BLUEBIRD-42 NOTE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. NOTE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI NOTE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen often confuses Task with coroutin`

### G07 - episodic

`EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: Hom nay to`

### G08 - episodic

`EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Ho`

### G11 - mixed

`<LONG_TERM> MARKERS: ORCHID-27, BLUEBIRD-42, LAB-REPORT-1600, ASYNC-FIX-20 NOTE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. NOTE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI NOTE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. FACT: Minh Nguyen increased the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen failed to d`

### G13 - mixed

`<EPISODIC> EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon`

### G15 - mixed

`<LONG_TERM> MARKERS: ORCHID-27, BLUEBIRD-42, LAB-REPORT-1600, ASYNC-FIX-20 NOTE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. NOTE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at`

### G16 - mixed

`<LONG_TERM> MARKERS: ORCHID-27, BLUEBIRD-42, LAB-REPORT-1600, ASYNC-FIX-20 NOTE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguye`

### G17 - mixed

`<LONG_TERM> MARKERS: ORCHID-27, BLUEBIRD-42, LAB-REPORT-1600, ASYNC-FIX-20 NOTE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Coroutine has priority over Task when explaining. [valid_at=2026-08-01T09:02:20Z, invalid_at=None] FACT: Minh Nguyen requests that if this topic (async/await) comes up later, it be explained using a timeline. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen often confuses Task wi`

### G18 - mixed

`<EPISODIC> EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam vie`

### G19 - mixed

`<LONG_TERM> MARKERS: ORCHID-27, BLUEBIRD-42, LAB-REPORT-1600, ASYNC-FIX-20 NOTE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. NOTE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen suggests that reusing aiohttp ClientSession is an effective pattern`

### G05 - long_term

`MARKERS: ORCHID-27, BLUEBIRD-42, LAB-REPORT-1600, ASYNC-FIX-20 NOTE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI NOTE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. NOTE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. FACT: Minh Nguyen still prefers Python for personal demos for project ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: The demo ca nhan ORCHID-27 project prioritizes Python. [valid_at=2026-08-01T09:00:20Z, invalid_at=None] FACT:`

### G12 - mixed

`<LONG_TERM> MARKERS: ORCHID-27, BLUEBIRD-42, LAB-REPORT-1600, ASYNC-FIX-20 NOTE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI FACT: The project BLUEBIRD-42 requires TypeScript for the backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: The project BLUEBIRD-42 requires NestJS for the backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Python is prohibited for the backend of the project BLUEBIRD-42. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Da tach scope BLUEBIRD-42 uses TypeScript/NestJS. [v`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
