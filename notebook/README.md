# Notebook tiền xử lý và phân tích

- [pre_process.ipynb](pre_process.ipynb): đọc dữ liệu, thiết lập cửa sổ,
  phân chia train/test theo thời gian, tạo đặc trưng và xuất dữ liệu đã xử lý.
- [eda_analysis.ipynb](eda_analysis.ipynb): khám phá chuỗi thời gian,
  phân rã xu hướng/mùa vụ/phần dư và so sánh dữ liệu gốc với nội suy.

Notebook có sử dụng PySpark và các thư viện phân tích như matplotlib,
seaborn, statsmodels ngoài các thành phần phục vụ demo. Kiểm tra đường dẫn
dữ liệu và môi trường notebook trước khi chạy lại; output lưu sẵn không
đồng nghĩa notebook đã được chạy trong môi trường hiện tại.

Pipeline huấn luyện dùng mã trong `forecasting/preprocess/` và
`forecasting/train/`. Khi thay đổi đặc trưng trong notebook, cần đối chiếu
với pipeline và `demo/utils/metrics_forecast.py` để tránh khác biệt giữa
dữ liệu huấn luyện và suy luận. Xem [tài liệu cơ chế](../readme_demo_policies.md).
