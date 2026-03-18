# 🚀 Automation Testing Framework Showcase
**Ứng viên**: NGUYỄN CÔNG LẬP NHÂN  
**Vị trí ứng tuyển**: Automation Test Engineer

---

## 🎯 Giới thiệu Dự án
Dự án này được thiết kế để chứng minh kỹ năng Automation Testing thực chiến. Nó không chỉ giải quyết bài test logic cơ bản mà còn đóng gói toàn bộ vào một **Khung Kiểm thử Tự động đa tầng (Multi-layer Auto Framework)** chuyên nghiệp.

## 📂 Cấu trúc Thư mục (Project Structure)
```text
Auto_Framework/
├── core/                  # Chứa logic code giải các bài toán (Unit Test targets)
├── data/                  # Chứa data mẫu định dạng JSON phục vụ cho Data-Driven Testing
├── docs/                  # Tài liệu giải thích Framework và chiến lược Test cho NTD
├── pages/                 # Triển khai mô hình Page Object Model (POM) cho UI
├── reports/               # Nơi chứa kết quả chạy Auto (HTML & Allure Report)
├── tests/                 # Nơi chứa toàn bộ kịch bản E2E tự động
│   ├── api_tests/         # Kịch bản kiểm thử API (Requests)
│   ├── ui_tests/          # Kịch bản kiểm thử Giao diện (Selenium)
│   └── unit_tests/        # Kịch bản kiểm thử Logic với BVA & EP (Pytest)
├── .github/workflows/     # Cấu hình tự động chạy CI/CD (Github Actions)
├── conftest.py            # Cấu hình Fixtures dùng chung cho toàn bộ Pytest
├── pytest.ini             # Cấu hình config cho Pytest
├── requirements.txt       # Danh sách thư viện Python cần thiết
└── run_all_tests.bat      # Script thi hành toàn bộ test (1-Click Run)
```

## 🏗️ Kiến trúc Framework
Framework được xây dựng bằng ngôn ngữ **Python** và **Pytest**, áp dụng các Design Pattern hàng đầu trong ngành:

1. **Page Object Model (POM)**:
   - Tách biệt hoàn toàn UI Elements (`pages/`) và Test Scripts (`tests/ui_tests/`).
   - Tăng tính tái sử dụng và dễ dàng maintain khi UI thay đổi.

2. **Data-Driven Testing (DDT)**:
   - Dữ liệu test (Test Data) được tách riêng vào file JSON (`data/test_data.json`).
   - Tự động chạy hàng loạt Test Cases chỉ từ một function sử dụng `@pytest.mark.parametrize`.

3. **Multi-layer Testing Architecture**:
   - **Unit Tests**: Áp dụng kỹ thuật **Hộp đen (Black Box)** gồm *Equivalence Partitioning (EP)* và *Boundary Value Analysis (BVA)* để test các hàm logic tính toán.
   - **API Tests**: Tích hợp module HTTP Requests để verify dữ liệu Backend.
   - **UI Tests**: Tích hợp Selenium WebDriver để chạy kịch bản Web/E2E.

4. **Advanced Reporting & CI/CD**:
   - Tích hợp **Allure Report**: Tự động ghi lại các Test Steps và *đính kèm ảnh chụp màn hình (Screenshot)* khi gặp lỗi.
   - **GitHub Actions (`.github/workflows`)**: Sẵn sàng tích hợp DevSecOps / Continuous Testing.

## ⚙️ Hướng dẫn cài đặt và chạy thử

### 1. Yêu cầu môi trường
- Python 3.10+
- Firefox/Chrome Browser

### 2. Cài đặt và Chạy (1-Click Run)
Chỉ cần bấm đúp vào file `run_all_tests.bat` (Hoặc mở CMD và chạy nó).
File Batch này được thiết kế tự động hoàn toàn (Portable):
1. Tự động kiểm tra và khởi tạo Virtual Environment (`venv`) độc lập ngay trong thư mục nếu chưa có.
2. Tự động kích hoạt và tải tất cả thư viện cần thiết (`requirements.txt`).
3. Thực thi toàn bộ bộ Test (UI, API, Unit).

### 3. Xem báo cáo kết quả (Test Report)
Sau khi chay xong, hệ thống sẽ tự động sinh ra một file Báo cáo HTML siêu nhẹ:
- Hãy vào thư mục `reports/` và bấm đúp mở file **`report.html`** trên trình duyệt lưới để xem kết quả Pass/Fail cực kỳ trực quan.

*(Tùy chọn nâng cao)*: Nếu máy đã cài sẵn Java và Allure CLI, có thể xem báo cáo xịn xò hơn của Allure bằng lệnh:
```bash
allure serve reports/allure-results
```
## 📚 Tài liệu tham khảo (Documentation)
Để hiểu rõ hơn về lý do tại sao các Test Cases lại được thiết kế như vậy, hoặc giải đáp các thắc mắc về cơ chế tự động mở trình duyệt, thao tác gõ phím, cũng như các kỹ thuật BVA/EP được áp dụng:
👉 **[Xem chi tiết tại: Giải thích kết quả Test & FAQ](docs/08_Giai_Thich_Ket_Qua_Test.md)**

---
> *"Quality is not an act, it is a habit."* - Aristotle  
> Cảm ơn FPT Software đã tạo ra một bài test thú vị. Hy vọng kiến trúc hệ thống này chứng minh được năng lực và tư duy chất lượng của tôi phù hợp với vị trí và văn hóa công ty.
