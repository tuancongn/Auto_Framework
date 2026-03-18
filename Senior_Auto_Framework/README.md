# 🚀 Senior Automation Testing Framework Showcase
**Ứng viên**: [Tên Của Bạn]  
**Vị trí ứng tuyển**: Automation Test Engineer (Senior Level)

---

## 🎯 Giới thiệu Dự án
Dự án này được thiết kế để chứng minh kỹ năng Automation Testing thực chiến ở mức độ **Senior Engineer**. Nó không chỉ giải quyết bài test logic cơ bản (30% coding) mà còn đóng gói toàn bộ vào một **Khung Kiểm thử Tự động đa tầng (Multi-layer Auto Framework)** chuyên nghiệp.

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
File Batch này sẽ tự động:
1. Kích hoạt Virtual Environment nội bộ (`C:\Users\Admin\Desktop\Python\FirstProject1\venv`).
2. Tải tất cả thư viện cần thiết (`requirements.txt`).
3. Thực thi toàn bộ bộ Test (UI, API, Unit).

### 3. Xem báo cáo Allure
Nếu máy bạn đã cài sẵn Allure CLI, chỉ cần gõ lệnh sau để mở báo cáo đẹp mắt trên trình duyệt:
```bash
allure serve reports/allure-results
```

---
> *"Quality is not an act, it is a habit."* - Aristotle  
> Cảm ơn FPT Software đã tạo ra một bài test thú vị. Hy vọng kiến trúc hệ thống này chứng minh được năng lực và tư duy chất lượng của tôi phù hợp với vị trí và văn hóa công ty.
