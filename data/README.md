# Dữ liệu đã xử lý

Thư mục chứa các cặp `train_*_autoscaling.csv` và `test_*_autoscaling.csv`
cho ba khung tổng hợp: `1m`, `5m`, `15m`. Mỗi dòng biểu diễn một cửa sổ
thời gian; `requests_count` là số request trong cửa sổ đó.

- `timestamp`: thời điểm của cửa sổ dữ liệu.
- `requests_count`: biến mục tiêu dự báo và tải đầu vào mô phỏng.
- Các cột lag, rolling, temporal, burst/event: đặc trưng đã xử lý nếu có.

Các CSV hiện có chia train trước ngày 23/08/1995 và test từ ngày đó.
Dữ liệu train bắt đầu trong tháng 07/1995; dữ liệu test kéo dài tới
01/09/1995, nên khoảng thời gian thực tế rộng hơn mô tả chỉ tháng 08 trong
README chính.

Demo đọc các file này trực tiếp. Khi mô phỏng, capacity/server phải cùng
đơn vị thời gian với mỗi dòng. Nếu CSV dự báo có cả `timestamp` và `y_true`,
tab Forecast/Optimization có thể dùng dữ liệu thực trong CSV dự báo thay cho
CSV test được chọn. Xem [cơ chế demo](../readme_demo_policies.md).
