---
tieu-de: Được trích là đã giải quyết, nhưng *chưa ai đo*
phu-de: Kiểm toán mức hiện thực kênh trong semantic communication cho mạng phi mặt đất
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Physical Communication, nộp 13/09/2026
profile: nghien-cuu
tong-phut: 20
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: ntn-semcom-realism-audit · figures/out/numbers.tex
moc-ngay: số liệu tới 13/09/2026
---

## !cover
@phut: 0.5
@che-do: noi
@notes: Đọc đúng tên bài. Chưa cảm ơn ai, để cuối.

## Khảo sát của lĩnh vực đã nói hết, trừ một câu
@phut: 1.5
@che-do: noi
@notes: Đặt câu hỏi rồi IM ba giây. Đừng đọc slide.

Khảo sát của lĩnh vực có hẳn một bảng ánh xạ **hạn chế NTN** sang **công trình giải quyết nó**.

Câu bảng ấy bỏ ngỏ: những công trình đó *có thật sự được đo dưới hạn chế đó không*.

## Giao thức kiểm toán
@phan: PHƯƠNG PHÁP
@hinh: toan
@phut: 2.5
@che-do: hinh
@nen: luoi
@notes: Hai nhánh chạy ĐỘC LẬP, chỉ gặp nhau ở bước cuối. Chỉ vào chỗ gặp.

!hinh hinh/fig1-protocol.svg | Hai nhánh đo **độc lập**, chỉ gặp nhau ở bước cuối. Hình vẽ lại ở khổ slide, số lấy từ `numbers.tex` của bài.

## Hạn chế bị bỏ qua lớn cỡ nào
@phan: ĐỘ LỚN
@phut: 2.5
@che-do: so
@notes: Đây là số về VẬT LÝ, không phải về văn liệu. Nó đúng bất kể kiểm kê ra gì.

!so {{doppler_ka}} | Doppler băng Ka, trung vị | đo trên {{so_luot}} lượt bay thật
!so {{doppler_troi}} | tốc độ trôi Doppler, cực đại | nhanh hơn chu kỳ khối truyền
!so {{so_luot}} | lượt phân biệt từ TLE Starlink | không mô phỏng, dùng SGP4 trên dữ liệu công khai

## Phân bố thật qua một chòm sao
@phan: ĐỘ LỚN
@hinh: lon
@phut: 2.0
@che-do: hinh
@nen: luoi
@notes: Trục ngang là Doppler. Chỉ vào đuôi phải, đó là chỗ văn liệu không chạm tới.

!hinh hinh/fig2-orbital.svg | Phân bố đo được, không phải giả định. Đây là **số về vật lý**, có giá trị riêng kể cả khi phần kiểm kê cho kết quả ngược.

## Kiểm kê hai mươi sáu công trình
@phan: KIỂM KÊ
@phut: 3.0
@che-do: so
@wow
@dan: Chúng tôi lấy đúng quần thể của khảo sát, không tự chọn bài.
@notes: Nói hai con số không rồi IM ba giây. Đừng giải thích ngay, để phòng tự hiểu.

!so {{vet_quy_dao}} | công trình dùng vệt kênh từ quỹ đạo thật | không một bài nào
!so {{doppler_bien_thien}} | công trình đo dưới Doppler BIẾN THIÊN | Doppler tĩnh thì có, biến thiên thì không
!so {{awgn}} | công trình đánh giá dưới AWGN thuần | kênh dễ nhất có thể

## Nêu ra một đằng, đo một nẻo
@phan: KIỂM KÊ
@hinh: toan
@phut: 2.0
@che-do: hinh
@notes: Cột trái là thứ bài NÊU, cột phải là thứ bài ĐO. Chỉ vào khoảng cách.

!hinh hinh/fig6-matrix.svg | Mỗi ô là một cặp **hạn chế được trích** với **công trình được trích là giải quyết nó**. Mã hoá hai người độc lập, có báo hệ số đồng thuận.

## Đánh giá lại trên GPU
@phan: ĐÁNH GIÁ LẠI
@phut: 2.0
@che-do: so
@notes: Đây là phần người ta sẽ hỏi nhất. Bảng đầy đủ ở backup một.

!so {{sup_vong_ho}} | mức sụp chất lượng khi chạy vòng hở | ước lượng lại pha mỗi ba mươi hai ký hiệu thì KHÔNG sụp
!so {{muc_kiem}} | mục trong danh mục kiểm hiện thực | neo vào {{chuan_neo}}, không tự nghĩ

## Hai kết quả chạy ngược giả thuyết của chính bài
@phan: BÀN LUẬN
@phut: 1.5
@che-do: hoi
@notes: Đây là chỗ làm bài đáng tin. Nói chậm, đừng giấu.

Giả định SNR tĩnh trong một khối truyền hoá ra **ĐÚNG**: SNR chỉ trôi rất chậm.

Quét SNR cả lượt bay cũng **nhỏ hơn** chúng tôi chờ đợi.

!luu-y Vì sao vẫn báo cáo | Hai chỗ này đi ngược giả thuyết ban đầu. Bỏ đi thì bài dễ bán hơn, nhưng **chính chúng làm phần còn lại đáng tin**.

## Làm gì với kết quả này
@phut: 1.0
@che-do: noi
@notes: Nói chậm. Đây là chỗ người nghe ghi lại.

{{TAKE_HOME}}

- danh mục kiểm hiện thực neo vào chuẩn, dùng lại được cho khảo sát sau
- bộ sinh kênh tuân thủ chuẩn, cắm được vào bộ khung có sẵn

## !cam-on
@phut: 1.0
@che-do: lang
@notes: Nhắc lại take-home rồi dừng hẳn. Không mở slide mới.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng, dưới sáu mươi giây.

Danh mục kiểm và bộ sinh kênh đều **mở**. Lấy về chạy trên bài của bạn trước khi gửi đi.

## !backup Bảng kiểm kê đầy đủ
@che-do: so
@notes: Mở khi bị hỏi cách mã hoá hoặc quần thể.

!bang bang_kiem_ke

## !backup Lệch điều kiện huấn luyện và đánh giá
@che-do: so
@notes: Mở khi bị hỏi mức sụp chất lượng đo thế nào.

!bang bang_lech

## !backup Quần thể lấy từ đâu
@che-do: noi
@notes: Mở khi bị hỏi vì sao chỉ hai mươi sáu bài.

!so {{quan_the}} | công trình trong quần thể của khảo sát | lấy nguyên, không tự chọn
!so {{doc_duoc}} | công trình lấy được toàn văn | phần còn lại khai rõ là không đọc được
!so {{ma_hoa}} | công trình mã hoá được | mỗi bài hai người đọc độc lập

## !backup Một lượt bay trông ra sao
@hinh: toan
@che-do: hinh
@notes: Mở khi bị hỏi hình học từng lượt, hoặc vì sao chọn ngưỡng góc ngẩng.

!hinh hinh/fig3-pass.svg | Một lượt bay đơn lẻ: cự ly nghiêng, góc ngẩng và Doppler biến thiên **trong vòng vài phút**.

## !backup Suy hao theo góc ngẩng
@hinh: lon
@che-do: hinh
@notes: Mở khi bị hỏi vì sao suy hao không phải hằng số trong một lượt.

!hinh hinh/fig4-elevation.svg | Suy hao đổi theo góc ngẩng suốt lượt bay. Đây là thứ mô hình AWGN cố định **không có**.

## !backup Kiểm kê theo từng hiệu ứng
@hinh: lon
@che-do: hinh
@notes: Mở khi bị hỏi phân bố kiểm kê, hoặc vì sao con số không lại nằm ở hai hiệu ứng ấy.

!hinh hinh/fig5-census.svg | Số công trình **nêu ra** so với số công trình **thực sự đo** dưới từng hiệu ứng.

## !backup Lệch điều kiện huấn luyện và đánh giá
@hinh: lon
@che-do: hinh
@notes: Mở cùng bảng lệch. Chỉ vào chỗ vòng hở sụp.

!hinh hinh/fig7-mismatch.svg | Chất lượng khôi phục khi điều kiện đánh giá **rời khỏi** điểm huấn luyện.

## !backup Độ dài khối và ước lượng lại pha
@hinh: lon
@che-do: hinh
@notes: Mở khi bị hỏi vì sao ước lượng lại pha mỗi ba mươi hai ký hiệu thì không sụp.

!hinh hinh/fig8-blocklen.svg | Ước lượng lại pha theo chu kỳ ngắn thì mức sụp **biến mất**.
