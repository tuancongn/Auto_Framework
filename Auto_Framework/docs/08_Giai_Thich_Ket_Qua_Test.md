# 📘 GIẢI THÍCH KẾT QUẢ AUTOMATION TEST
## Giải thích chung

Khi chạy file `run_all_tests.bat`, giao diện Console chạy các dòng log và thông báo `24 passed in 56.58s`. Dưới đây là cách giải thích chi tiết:

---

## 1. Tại sao terminal lại báo "PASSED"?
- **"PASSED"** có nghĩa là **Kết quả Thực tế (Actual Result)** của phần mềm hoàn toàn khớp với **Kết quả Mong đợi (Expected Result)** mà chúng ta đã thiết lập trong Test Case.
- Ví dụ ở bài Unit Test tính tiền điện, với đầu vào (Input) là `0 kWh`, hàm trả về đúng `0 VND` (Biên BVA). Code tự động dùng lệnh `assert` để so sánh, khi 2 bên khớp nhau, nó in ra `[0-0] PASSED`.

## 2. Tại sao trình duyệt lại TỰ MỞ lên, TỰ GÕ và TỰ ĐÓNG lại?
Đó chính là **UI Automation Testing (Kiểm thử tự động giao diện)**.
- **Tự mở lên**: Framework sử dụng thư viện `Selenium WebDriver` để giao tiếp trực tiếp với lõi của trình duyệt Chrome. Câu lệnh `driver.get(URL)` đã ra hiệu cho trình duyệt khởi động và truy cập vào trang web `saucedemo.com`.
- **Tự gõ**: Framework áp dụng mô hình **POM (Page Object Model)** để xác định vị trí của thẻ HTML (như ô Input Username/Password) thông qua ID/XPath. Sau đó dùng lệnh `send_keys` (với tốc độ `time.sleep` đã set chậm lại để giống con người) để truyền text vào.
- **Tự đóng**: Ở file `conftest.py`, có một hàm tên là `yield driver` và sau đó là `driver.quit()`. Đây là nguyên tắc "Dọn dẹp (Teardown)" trong Testing: Dù test Pass hay Fail, hệ thống luôn phải đóng trình duyệt lại ở cuối mỗi Test Case để giải phóng bộ nhớ (RAM) cho máy tính, giúp máy không bị giật lag khi chạy hàng ngàn Test Cases.

## 3. Tại sao gõ sai mật khẩu mà test vẫn báo `PASSED`?
Kịch bản `test_invalid_login` cố tình gõ sai User/Pass, hệ thống web báo lỗi đỏ, nhưng màn hình CMD vẫn in chữ màu xanh `PASSED`. Tại sao?
- Đây là **Negative Testing** (Test kịch bản lỗi). Expectation (Kết quả mong đợi) là *Web PHẢI hiện ra dòng chữ lỗi Đỏ đó*. Trong code Automation, mã đã lấy dòng chữ đỏ đó ra và so sánh: Nếu dòng chữ đó khớp 100% với file JSON data, tức là chức năng *Bắt lỗi đăng nhập của Web* hoạt động chính xác. Do đó Test Case này PASSED."
- Tính năng này được gọi là **DDT (Data-Driven Testing)**: Mã đã đọc danh sách các user sai từ file `test_data.json` và lặp lại logic test tự động.

## 4. Báo cáo Allure (Allure Report) chứa những gì?
- Terminal đen trắng (Console log) chỉ dành cho Engineer xem lúc debug. Còn khi báo cáo cho Khách hàng, Product Owner (PO) hoặc Project Manager (PM), chúng ta cần Báo cáo hình ảnh.
- Framework này đã cài đặt một "Hook" (Móc nối) vào lõi của phần mềm test. Mỗi khi trình duyệt click một nút, API gửi một request, nó tự ghi lại (log).
- **Đặc biệt**: Nếu có 1 Test bị Fail, cái Hook này sẽ gọi lệnh chụp ảnh màn hình (`get_screenshot_as_png`) ngay tại khoảnh khắc bị lỗi. Báo cáo Allure sẽ đính kèm tấm ảnh đó, giúp team Dev nhìn vào là biết giao diện đang hỏng ở đâu ngay lập tức mà Tester không cần phải mô tả dài dòng.

---

## 🎯 CÂU HỎI THƯỜNG GẶP

### ❓ Q: "Em viết code Automation thì em dùng mô hình gì để dễ bảo trì?"
**Trả lời**: Dạ em dùng mô hình **POM (Page Object Model)** kết hợp **Data-Driven**. POM giúp tách các Locator (Id, Class) của nút bấm ra khỏi code logic test. Nếu ngày mai website đổi giao diện, em chỉ cần vào file `pages/login_page.py` để sửa 1 đoạn nhỏ, mà KHÔNG cần đụng chạm gì đến hàng chục file Test Cases ở ngoài. Việc này giúp giảm chi phí maintain cực kỳ hiệu quả.

### ❓ Q: "Tại sao em lại kết hợp song song giữa Unit Test, API Test và UI Test?"
**Trả lời**: Dạ vì em áp dụng mô hình **Test Pyramid (Kim tự tháp kiểm thử)**. Làm E2E Test (UI Test) thì quan sát rất trực quan nhưng chạy rất chậm và dễ đứt gãy (flaky). Do đó với những logic IF-ELSE tính toán như bài Test của công ty, em dùng Unit Test kết hợp kỹ thuật BVA (Giá trị biên) và EP (Phân lớp tương đương) để chạy nhanh gọn. Với data, em test trực tiếp qua API (Postman/Requests) để đảm bảo Backend ổn định.

### ❓ Q: "Vậy bình thường em code xong thì ai sẽ bấm chạy cái này?"
**Trả lời**: Dạ em đã cấu hình sẵn một luồng **CI/CD** bằng file `.github/workflows`. Trong mô hình hiện đại, mỗi khi anh Dev bấm "Push code" lên server, Github Actions sẽ tự động dựng một máy ảo Ubuntu, tự bật Server ngầm (Headless chrome) chạy bộ đồ nghề này của em trong vòng 2 phút. Nếu code Pass 100% thì nó mới cho Dev merge. Như vậy em "Shift-Left" quy trình QA, tiết kiệm thời gian test manual lặp đi lặp lại rất nhiều.
