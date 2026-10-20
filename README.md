# Được trích là đã giải quyết, nhưng chưa ai đo

Bài nói 20 phút cho bài báo **NTN semantic communication realism audit**
(nộp Physical Communication 13/09/2026, tác giả đơn: Đỗ Phúc Hảo, CAIRA, Đại học
Kiến trúc Đà Nẵng).

👉 **Mở `index.html`.** Một tệp tự chứa, chạy được khi không có mạng.

## Xem thế nào

| phím | việc |
|---|---|
| `↓` `Space` `PageDn` | slide sau |
| `→` `←` | bước trong slide, hết thì sang slide |
| `o` | tổng quan toàn bộ |
| **`p`** | cửa sổ người nói: ghi chú, đồng hồ, sớm muộn bao nhiêu phút |
| **`e`** | xuất PDF ngay từ trang |
| `?` | bảng phím |

Cuộn chuột thì cùng tệp ấy thành trang đọc. Một bản nội dung, không hai.

## Nội dung

**20 slide, 20 phút**: 12 slide mạch chính, 8 slide dự phòng cho phần hỏi đáp.
Tám hình của bài đều có mặt. Bản PDF ở `deck.pdf`.

Con số chốt: **0/26** công trình dùng vệt kênh từ quỹ đạo thật · **0/26** đo dưới
Doppler biến thiên · **16/26** chỉ đánh giá dưới AWGN thuần.

## Dựng lại

Deck dựng bằng bộ kit **[deck-web](https://github.com/haodpsut/deck-web)**.
`lay_so.py` đọc `figures/out/numbers.tex` của bài, `lay_hinh.py` bọc bộ sinh hình
matplotlib của bài để lấy SVG giữ chữ thật. **Không con số nào gõ tay vào deck.**

```bash
python3 lay_so.py && python3 lay_hinh.py     # cần thư mục bài ở cạnh
python3 ../../_templates/deck-web/dung.py .  # dựng index.html
python3 ../../_templates/deck-web/qa.py   .  # 25 cổng
```

## Khai dùng AI

Lịch sử commit của kho này mang trailer `Co-Authored-By: Claude`.
