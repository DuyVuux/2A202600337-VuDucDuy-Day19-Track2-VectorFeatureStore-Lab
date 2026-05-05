# Reflection — Lab 19

**Tên:** _Vũ Đức Duy_
**MSSV:** _2A202600337_
**Cohort:** _01_
**Path đã chạy:** _lite_

---

## Câu hỏi (≤ 200 chữ)

> Trên golden set 50 queries, mode nào thắng ở loại query nào (`exact` /
> `paraphrase` / `mixed`), và tại sao? Khi nào bạn **không** dùng hybrid
> (i.e. khi nào pure BM25 hoặc pure vector là lựa chọn đúng)?

- **Exact queries:** BM25 thắng (96.7%) nhờ khớp từ khóa chính xác tuyệt đối. Hybrid giữ vững phong độ này.
- **Paraphrase queries:** Cả hai đều giảm hiệu năng (KW: 33.3%, SEM: 24.0%). Semantic yếu do model `bge-small-en` hạn chế với tiếng Việt trong Lite path.
- **Mixed queries:** Hybrid thắng tuyệt đối (100.0%) nhờ kết hợp tín hiệu từ cả hai phía.

**Khi nào không dùng Hybrid:** Không dùng khi cần latency cực thấp và chi phí thấp (BM25 là đủ cho exact search), hoặc khi embedding model đã quá mạnh bao quát được cả keyword signal.

---

## Điều ngạc nhiên nhất khi làm lab này

Sự kết hợp đơn giản qua RRF lại mang lại hiệu quả robust đến vậy, đặc biệt là trên các query hỗn hợp (mixed).

---

## Bonus challenge

- [ ] Đã làm bonus (xem `bonus/`)
- [ ] Pair work với: _None_
