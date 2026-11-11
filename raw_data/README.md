# Dữ liệu log gốc

Cấu hình huấn luyện tại [train_config.yaml](../configs/train_config.yaml)
tham chiếu hai file `raw_data/train.txt` và `raw_data/test.txt`. Các file log
này chưa có trong bản checkout hiện tại; `drive.txt` lưu thông tin nguồn để
tham khảo khi chuẩn bị dữ liệu.

Pipeline đọc mỗi dòng log, phân tích Apache log, chuẩn hóa timestamp rồi
tổng hợp số request theo cửa sổ thời gian. Cần cung cấp đủ hai file theo
cấu hình trước khi chạy `python main.py`.

Các CSV trong [data/](../data/README.md) và kết quả dự báo đã lưu phục vụ
demo, nhưng điểm vào huấn luyện hiện tại vẫn yêu cầu log gốc; nó không tự
chuyển sang huấn luyện từ CSV khi thiếu log.
