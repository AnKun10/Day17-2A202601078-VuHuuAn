# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1844.7 ms**
- Average token reduction vs full source context: **8.7%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.8 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G08 | long_term | PASS | 2725.7 | 705 | 0.0% |  |
| G09 | long_term | PASS | 1918.9 | 1797 | 0.0% |  |
| G12 | semantic | PASS | 315.3 | 365 | 20.5% |  |
| G14 | semantic | PASS | 402.1 | 217 | 43.9% |  |
| G15 | semantic | PASS | 339.6 | 217 | 52.7% |  |
| G19 | mixed | PASS | 5958.3 | 581 | 0.0% |  |
| G03 | long_term | PASS | 3525.4 | 1790 | 0.0% |  |
| G04 | long_term | PASS | 3240.6 | 1788 | 0.0% |  |
| G05 | long_term | PASS | 1910.5 | 1783 | 0.0% |  |
| G10 | episodic | PASS | 1030.1 | 467 | 0.0% |  |
| G11 | episodic | PASS | 421.1 | 494 | 0.0% |  |
| G13 | semantic | PASS | 476.2 | 363 | 35.8% |  |
| G16 | mixed | PASS | 4382.0 | 581 | 0.0% |  |
| G18 | mixed | PASS | 576.6 | 489 | 13.5% |  |
| G20 | mixed | PASS | 3008.0 | 831 | 0.0% |  |
| G06 | long_term | PASS | 2599.2 | 1786 | 0.0% |  |
| G07 | long_term | PASS | 1893.9 | 1791 | 0.0% |  |
| G17 | mixed | PASS | 2170.3 | 581 | 8.1% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G08 - long_term

`<USER_SUMMARY> The user's project is LOTUS-88. They prioritize Java and Spring Boot, and do not use Python for backend examples. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. </EPISODES>  <FACT`

### G09 - long_term

`<USER_SUMMARY> The user is studying async/await, coroutines, and Tasks. Their personal project is ORCHID-27, for which they prefer Python. For work, the company project BLUEBIRD-42 requires backend development in TypeScript with NestJS, explicitly not Python. The user is debugging async HTTP requests and attempting to increase the timeout to 60 seconds. They need to complete a benchmark report, LAB-REPORT-1600, by Friday at 16:00. The lab assistant also asked to check the connection pool, client lifecycle, and concurrency. A recent incident, ASYNC-FIX-20, was resolved by reusing an aiohttp ClientSession and setting concurrency to 20, indicating the main issue was connection churn, not the ti`

### G12 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal `

### G14 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G15 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's project is LOTUS-88. They prioritize Java and Spring Boot, and do not use Python for backend examples. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. </EPIS`

### G03 - long_term

`<USER_SUMMARY> The user is studying async/await, coroutines, and Tasks. Their personal project is ORCHID-27, for which they prefer Python. For work, the company project BLUEBIRD-42 requires backend development in TypeScript with NestJS, explicitly not Python. The user is debugging async HTTP requests and attempting to increase the timeout to 60 seconds. They need to complete a benchmark report, LAB-REPORT-1600, by Friday at 16:00. The lab assistant also asked to check the connection pool, client lifecycle, and concurrency. A recent incident, ASYNC-FIX-20, was resolved by reusing an aiohttp ClientSession and setting concurrency to 20, indicating the main issue was connection churn, not the ti`

### G04 - long_term

`<USER_SUMMARY> The user is studying async/await, coroutines, and Tasks. Their personal project is ORCHID-27, for which they prefer Python. For work, the company project BLUEBIRD-42 requires backend development in TypeScript with NestJS, explicitly not Python. The user is debugging async HTTP requests and attempting to increase the timeout to 60 seconds. They need to complete a benchmark report, LAB-REPORT-1600, by Friday at 16:00. The lab assistant also asked to check the connection pool, client lifecycle, and concurrency. A recent incident, ASYNC-FIX-20, was resolved by reusing an aiohttp ClientSession and setting concurrency to 20, indicating the main issue was connection churn, not the ti`

### G05 - long_term

`<USER_SUMMARY> The user is studying async/await, coroutines, and Tasks. Their personal project is ORCHID-27, for which they prefer Python. For work, the company project BLUEBIRD-42 requires backend development in TypeScript with NestJS, explicitly not Python. The user is debugging async HTTP requests and attempting to increase the timeout to 60 seconds. They need to complete a benchmark report, LAB-REPORT-1600, by Friday at 16:00. The lab assistant also asked to check the connection pool, client lifecycle, and concurrency. A recent incident, ASYNC-FIX-20, was resolved by reusing an aiohttp ClientSession and setting concurrency to 20, indicating the main issue was connection churn, not the ti`

### G10 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Minh dang lam kiem ke lai mo hinh cac du an backend `

### G11 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession`

### G13 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data witho`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> The user is studying async/await, coroutines, and Tasks. Their personal project is ORCHID-27, for which they prefer Python. For work, the company project BLUEBIRD-42 requires backend development in TypeScript with NestJS, explicitly not Python. The user is debugging async HTTP requests and attempting to increase the timeout to 60 seconds. They need to complete a benchmark report, LAB-REPORT-1600, by Friday at 16:00. The lab assistant also asked to check the connection pool, client lifecycle, and concurrency. A recent incident, ASYNC-FIX-20, was resolved by reusing an aiohttp ClientSession and setting concurrency to 20, indicating the main issue was connection churn`

### G18 - mixed

`<EPISODIC> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Minh dang chuan bi tu on lai phan async cua Python vi tuan `

### G20 - mixed

`<LONG_TERM> <USER_SUMMARY> The user is studying async/await, coroutines, and Tasks. Their personal project is ORCHID-27, for which they prefer Python. For work, the company project BLUEBIRD-42 requires backend development in TypeScript with NestJS, explicitly not Python. The user is debugging async HTTP requests and attempting to increase the timeout to 60 seconds. They need to complete a benchmark report, LAB-REPORT-1600, by Friday at 16:00. The lab assistant also asked to check the connection pool, client lifecycle, and concurrency. A recent incident, ASYNC-FIX-20, was resolved by reusing an aiohttp ClientSession and setting concurrency to 20, indicating the main issue was connection churn`

### G06 - long_term

`<USER_SUMMARY> The user is studying async/await, coroutines, and Tasks. Their personal project is ORCHID-27, for which they prefer Python. For work, the company project BLUEBIRD-42 requires backend development in TypeScript with NestJS, explicitly not Python. The user is debugging async HTTP requests and attempting to increase the timeout to 60 seconds. They need to complete a benchmark report, LAB-REPORT-1600, by Friday at 16:00. The lab assistant also asked to check the connection pool, client lifecycle, and concurrency. A recent incident, ASYNC-FIX-20, was resolved by reusing an aiohttp ClientSession and setting concurrency to 20, indicating the main issue was connection churn, not the ti`

### G07 - long_term

`<USER_SUMMARY> The user is studying async/await, coroutines, and Tasks. Their personal project is ORCHID-27, for which they prefer Python. For work, the company project BLUEBIRD-42 requires backend development in TypeScript with NestJS, explicitly not Python. The user is debugging async HTTP requests and attempting to increase the timeout to 60 seconds. They need to complete a benchmark report, LAB-REPORT-1600, by Friday at 16:00. The lab assistant also asked to check the connection pool, client lifecycle, and concurrency. A recent incident, ASYNC-FIX-20, was resolved by reusing an aiohttp ClientSession and setting concurrency to 20, indicating the main issue was connection churn, not the ti`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user is studying async/await, coroutines, and Tasks. Their personal project is ORCHID-27, for which they prefer Python. For work, the company project BLUEBIRD-42 requires backend development in TypeScript with NestJS, explicitly not Python. The user is debugging async HTTP requests and attempting to increase the timeout to 60 seconds. They need to complete a benchmark report, LAB-REPORT-1600, by Friday at 16:00. The lab assistant also asked to check the connection pool, client lifecycle, and concurrency. A recent incident, ASYNC-FIX-20, was resolved by reusing an aiohttp ClientSession and setting concurrency to 20, indicating the main issue was connection churn`
