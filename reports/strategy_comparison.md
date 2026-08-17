# Short-term context strategies - comparison (student extension)

Stream: 1 deadline constraint (`REVIEW-DEADLINE-1600`, Friday, 16:00) + filler, 30 turns total.
PASS = all 3 markers still present in the rendered context after the whole stream.

| Strategy | K | Est. tokens | Msgs kept | Compactions | Deadline survives |
| --- | ---: | ---: | ---: | ---: | --- |
| buffer | 6 | 437 | 30 | 0 | PASS |
| window-only | 6 | 86 | 6 | 24 | FAIL (0/3) |
| summary | 6 | 426 | 5 | 5 | PASS |
| sliding | 6 | 511 | 6 | 24 | PASS |
| hybrid | 6 | 302 | 8 | 24 | PASS |
| buffer | 4 | 437 | 30 | 0 | PASS |
| window-only | 4 | 58 | 4 | 26 | FAIL (0/3) |
| summary | 4 | 512 | 3 | 9 | PASS |
| sliding | 4 | 512 | 4 | 26 | PASS |
| hybrid | 4 | 273 | 6 | 26 | PASS |

## Ghi chu tung chien luoc

- **buffer**: Giu tat ca: khong bao gio mat constraint nhung token tang tuyen tinh theo so turn.
- **window-only**: Chi giu K turn cuoi: re nhat nhung constraint cu RoI khoi window -> mat deadline.
- **summary**: Nen turn cu thanh extractive summary: giu duoc constraint neu summarizer nhan ra no.
- **sliding**: Summary + durable notes + K turn gan nhat (default cua lab): constraint song trong durable notes.
- **hybrid**: Pin constraint nguyen van, evict filler truoc, chi summarize filler: lossless voi constraint.

## Bai hoc

1. `buffer` khong bao gio quen nhung chi phi token tang tuyen tinh - khong scale.
2. `window-only` cho thay sliding window NGAY THO la nguy hiem: constraint cu roi khoi window va bien mat.
3. `summary` re hon buffer nhung lossy - constraint chi song neu summarizer trich dung no.
4. `sliding` (default cua lab) = summary + durable notes + recent turns: compaction khong phai 'tom tat van hoa',
   ma la giu state/decision/TODO/constraint co chu dich (E10 pass nho durable notes, ke ca khi K giam 6 -> 4).
5. `hybrid` di xa hon: pin constraint nguyen van (lossless), chi summarize filler bi evict -
   doi them mot it token co dinh lay su chac chan rang constraint khong bi bien dang.
