# 📘 SOFTWARE TESTING FUNDAMENTALS
## (Non-Functional Testing, Black Box Testing, Test Types)

---

## I. TESTING CƠ BẢN

### 1. Software Testing là gì?
Là quá trình **đánh giá và xác minh** rằng phần mềm hoạt động đúng theo yêu cầu, không có lỗi, và đáp ứng nhu cầu của người dùng.

### 2. Mục đích của Testing:
- **Tìm defects** (lỗi) trước khi delivery
- **Xác minh** sản phẩm đáp ứng requirements
- **Đảm bảo chất lượng** (Quality Assurance)
- **Cung cấp thông tin** cho stakeholders về chất lượng sản phẩm
- **Ngăn ngừa** defects (prevention > detection)

### 3. 7 Nguyên tắc Testing (7 Testing Principles - ISTQB):

| # | Nguyên tắc | Giải thích |
|---|-----------|------------|
| 1 | **Testing shows the presence of defects** | Testing chứng minh có bug, KHÔNG chứng minh không có bug |
| 2 | **Exhaustive testing is impossible** | Không thể test hết tất cả combinations → dùng risk-based approach |
| 3 | **Early testing** | Test sớm → tiết kiệm chi phí (Shift-Left) |
| 4 | **Defect clustering** | 80% bugs tập trung ở 20% modules (Pareto principle) |
| 5 | **Pesticide paradox** | Chạy lại cùng test cases → không tìm thêm bug → cần update test cases |
| 6 | **Testing is context-dependent** | Cách test khác nhau tùy loại phần mềm |
| 7 | **Absence-of-errors fallacy** | Không có bug ≠ phần mềm tốt (có thể không đáp ứng user needs) |

---

## II. FUNCTIONAL TESTING VS NON-FUNCTIONAL TESTING

### 🔵 Functional Testing (Kiểm thử chức năng)

**Định nghĩa**: Test xem phần mềm **làm gì** (WHAT it does) - kiểm tra các chức năng hoạt động đúng theo requirements.

**Các loại Functional Testing:**
1. **Unit Testing** - Test từng function/method riêng lẻ
2. **Integration Testing** - Test tương tác giữa các modules
3. **System Testing** - Test toàn bộ hệ thống
4. **UAT (User Acceptance Testing)** - End-user test
5. **Smoke Testing** - Test cơ bản nhất sau build mới
6. **Sanity Testing** - Test nhanh sau minor changes
7. **Regression Testing** - Re-test sau khi fix bug hoặc thêm feature

**Ví dụ**: Login page
- Nhập đúng username/password → đăng nhập thành công ✅
- Nhập sai password → hiển thị thông báo lỗi ✅
- Để trống fields → validation message ✅

### 🔴 Non-Functional Testing (Kiểm thử phi chức năng) ⭐ TRỌNG TÂM

**Định nghĩa**: Test phần mềm **hoạt động như thế nào** (HOW it works) - kiểm tra các đặc tính chất lượng NGOÀI chức năng.

**Các loại Non-Functional Testing:**

#### 1. Performance Testing (Kiểm thử hiệu năng)
- **Load Testing**: Test với lượng user dự kiến (expected load)
  - VD: Website expected 1000 users → test với 1000 users đồng thời
- **Stress Testing**: Test vượt quá giới hạn để tìm breaking point
  - VD: Test với 10000 users để xem system crash ở đâu
- **Volume Testing**: Test với lượng data lớn
  - VD: Database có 10 triệu records
- **Endurance/Soak Testing**: Test trong thời gian dài
  - VD: Chạy system liên tục 72 giờ để phát hiện memory leaks
- **Spike Testing**: Test với tải đột ngột tăng/giảm
  - VD: Flash sale - 0 users → 5000 users trong 1 phút

#### 2. Security Testing (Kiểm thử bảo mật)
- **SQL Injection**: Thử inject SQL qua input fields
- **XSS (Cross-Site Scripting)**: Thử inject JavaScript
- **Authentication/Authorization**: Kiểm tra login, phân quyền
- **Data Encryption**: Verify data mã hóa
- **Vulnerability Scanning**: Quét lỗ hổng bảo mật

#### 3. Usability Testing (Kiểm thử khả dụng)
- Navigation dễ sử dụng
- Layout nhất quán
- Error messages rõ ràng
- Accessibility (cho người khuyết tật)
- Learnability (dễ học sử dụng)

#### 4. Compatibility Testing (Kiểm thử tương thích)
- **Browser compatibility**: Chrome, Firefox, Safari, Edge
- **OS compatibility**: Windows, macOS, Linux, Android, iOS
- **Device compatibility**: Desktop, Tablet, Mobile
- **Resolution compatibility**: Các độ phân giải khác nhau

#### 5. Reliability Testing (Kiểm thử độ tin cậy)
- **Recovery Testing**: Khả năng phục hồi sau crash
- **MTBF (Mean Time Between Failures)**: Thời gian trung bình giữa các lần hỏng
- **MTTR (Mean Time To Repair)**: Thời gian trung bình để sửa

#### 6. Scalability Testing
- Khả năng mở rộng khi tăng load
- Horizontal scaling (thêm servers) vs Vertical scaling (nâng cấp server)

#### 7. Localization & Internationalization Testing
- **L10n**: Test ngôn ngữ, tiền tệ, date format cho từng locale
- **I18n**: Test kiến trúc hỗ trợ đa ngôn ngữ

### So sánh Functional vs Non-Functional:

| Tiêu chí | Functional | Non-Functional |
|-----------|-----------|----------------|
| Focus | WHAT it does | HOW it does it |
| Dựa trên | Requirements | Expectations |
| Ví dụ | Login, Search, Payment | Performance, Security, Usability |
| Thực hiện trước? | Thường trước | Thường sau functional |
| Manual/Auto | Cả hai | Thường automation (Performance) |
| Tools | Selenium | JMeter, LoadRunner, OWASP ZAP |

---

## III. BLACK BOX TESTING ⭐ TRỌNG TÂM

### 1. Định nghĩa:
**Black Box Testing** là phương pháp test **KHÔNG cần biết code bên trong**. Tester chỉ quan tâm đến **Input → Expected Output** mà không biết internal logic.

### 2. Đặc điểm:
- Dựa trên **requirements/specifications**
- Không cần biết programming
- Tester và Developer có thể làm **độc lập**
- Focus vào **behavior** của system

### 3. Kỹ thuật Black Box Testing:

#### 🔹 a) Equivalence Partitioning (EP) - Phân lớp tương đương
**Ý tưởng**: Chia input thành các **nhóm tương đương**, test 1 giá trị đại diện cho mỗi nhóm.

**Ví dụ**: Ô nhập tuổi (1-120 hợp lệ)
| Partition | Range | Valid? | Test Value |
|-----------|-------|--------|------------|
| P1 | < 1 (ví dụ: -5, 0) | Invalid | 0 |
| P2 | 1 - 120 | Valid | 50 |
| P3 | > 120 (ví dụ: 121, 999) | Invalid | 150 |

→ Chỉ cần 3 test cases thay vì test tất cả giá trị!

#### 🔹 b) Boundary Value Analysis (BVA) - Phân tích giá trị biên
**Ý tưởng**: Bugs thường xảy ra ở **biên** (boundary) → test các giá trị biên.

**Ví dụ**: Ô nhập tuổi (1-120)
| Test Value | Expected | Type |
|-----------|----------|------|
| 0 | Invalid | Below lower boundary |
| 1 | Valid | Lower boundary |
| 2 | Valid | Just above lower boundary |
| 119 | Valid | Just below upper boundary |
| 120 | Valid | Upper boundary |
| 121 | Invalid | Above upper boundary |

#### 🔹 c) Decision Table Testing
**Ý tưởng**: Dùng bảng quyết định cho logic phức tạp có nhiều **conditions** và **actions**.

**Ví dụ**: Discount policy
| Condition | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|-----------|--------|--------|--------|--------|
| VIP Member | Yes | Yes | No | No |
| Order > 500k | Yes | No | Yes | No |
| **Discount** | **30%** | **20%** | **10%** | **0%** |

→ 4 test cases cho tất cả combinations

#### 🔹 d) State Transition Testing
**Ý tưởng**: Test các **trạng thái** và **chuyển đổi** giữa chúng.

**Ví dụ**: ATM PIN
```
State 1: First Attempt → Wrong PIN → State 2: Second Attempt
State 2: Second Attempt → Wrong PIN → State 3: Third Attempt  
State 3: Third Attempt → Wrong PIN → State 4: Account Locked
State 1/2/3: Correct PIN → Access Granted
```

#### 🔹 e) Error Guessing
- Dựa trên **kinh nghiệm** của tester
- Đoán các lỗi có thể xảy ra
- VD: Nhập special characters, empty fields, SQL injection, boundary values

### 4. White Box vs Black Box vs Gray Box:

| Tiêu chí | Black Box | White Box | Gray Box |
|-----------|-----------|-----------|----------|
| Knowledge | Không biết code | Biết code | Biết một phần |
| Focus | Functionality | Code structure | Cả hai |
| Ai test | Tester | Developer | Cả hai |
| Level | System/UAT | Unit | Integration |
| Techniques | EP, BVA | Code coverage, Path testing | - |

---

## IV. REGRESSION TESTING ⭐ TRỌNG TÂM

### 1. Định nghĩa:
**Regression Testing** là việc **re-test** lại các chức năng đã hoạt động tốt trước đó, sau khi có **thay đổi** (bug fix, new feature, code refactor) để đảm bảo thay đổi **không gây ra bug mới**.

### 2. Khi nào cần Regression Testing?
- Sau khi **fix bug**
- Sau khi **thêm feature mới**
- Sau khi **refactor code**
- Sau khi **thay đổi configuration**
- Sau khi **upgrade platform/database**

### 3. Regression Test Strategies:
1. **Retest All**: Chạy lại tất cả test cases → Tốn thời gian nhưng an toàn nhất
2. **Regression Test Selection**: Chọn test cases liên quan đến thay đổi
3. **Test Case Prioritization**: Ưu tiên test cases quan trọng (risk-based)
4. **Hybrid**: Kết hợp Selection + Prioritization

### 4. Regression Testing Best Practices:
- **Automate** regression tests (dùng Selenium, Cypress...)
- Chạy **sau mỗi build** (CI/CD)
- **Maintain** test suite - thêm/xóa test cases phù hợp
- Ưu tiên test **critical paths** trước

### 5. Retesting vs Regression Testing:

| Tiêu chí | Retesting | Regression Testing |
|-----------|-----------|-------------------|
| Mục đích | Verify bug đã fix | Verify không có side effects |
| Test case | Cùng test case đã fail | Các test case khác |
| Scope | Bug cụ thể | Broader scope |
| Automation | Thường manual | Nên automation |

---

## V. CÁC LOẠI TEST KHÁC QUAN TRỌNG

### Smoke Testing vs Sanity Testing:

| Tiêu chí | Smoke Testing | Sanity Testing |
|-----------|--------------|----------------|
| Mục đích | Build có stable không? | Specific functionality OK? |
| Scope | Broad/Shallow | Narrow/Deep |
| Khi nào | Sau mỗi build mới | Sau minor changes |
| Ai test | Dev/Tester | Tester |
| Alias | Build Verification Test | Subset of Regression |

### Alpha Testing vs Beta Testing:

| Tiêu chí | Alpha Testing | Beta Testing |
|-----------|--------------|--------------|
| Nơi test | In-house (công ty) | Real user environment |
| Ai test | Internal team | End users |
| Giai đoạn | Trước Beta | Trước release |
| Bugs | Nhiều hơn | Ít hơn |
| Feedback | Internal | External |

### Integration Testing Approaches:
1. **Big Bang**: Integrate tất cả modules cùng lúc → test
2. **Top-Down**: Test từ module cao nhất xuống (dùng Stubs)
3. **Bottom-Up**: Test từ module thấp nhất lên (dùng Drivers)
4. **Sandwich/Hybrid**: Kết hợp Top-Down + Bottom-Up

### Stubs vs Drivers:
- **Stub**: Module giả thay thế module cấp dưới (chưa develop)
- **Driver**: Module giả thay thế module cấp trên (chưa develop)

---

## VI. CÂU HỎI VÀ TRẢ LỜI (Q&A)

### ❓ Q1: Non-Functional Testing là gì? Cho ví dụ.
**✅ Trả lời:**
> Non-Functional Testing kiểm tra **"phần mềm hoạt động như thế nào"** thay vì "làm gì". Bao gồm:
> - **Performance**: Response time < 3s, hỗ trợ 1000 concurrent users
> - **Security**: Chống SQL Injection, XSS, bảo mật data
> - **Usability**: Giao diện dễ sử dụng, accessible
> - **Compatibility**: Chạy trên Chrome, Firefox, Safari, mobile
> - **Reliability**: Uptime 99.9%, recovery sau crash
>
> Ví dụ thực tế: Chức năng Login hoạt động đúng (Functional) ✅, nhưng mất 30 giây để load (Non-Functional) ❌.

### ❓ Q2: Phân biệt Load Testing, Stress Testing, Spike Testing?
**✅ Trả lời:**
> - **Load Testing**: Test với **expected load** → VD: 1000 users như dự kiến
> - **Stress Testing**: Test **vượt giới hạn** → VD: 10000 users (gấp 10) để tìm breaking point
> - **Spike Testing**: Test **tải đột ngột** → VD: 100 → 5000 → 100 users trong vài phút
>
> Tất cả thuộc Performance Testing. Tool phổ biến: **JMeter, LoadRunner, Gatling**.

### ❓ Q3: Black Box Testing là gì? Kể tên các kỹ thuật.
**✅ Trả lời:**
> Black Box Testing test phần mềm **KHÔNG cần biết internal code**, chỉ dựa trên **input → expected output** theo specifications.
>
> Các kỹ thuật:
> 1. **Equivalence Partitioning**: Chia input thành nhóm tương đương, test 1 đại diện/nhóm
> 2. **Boundary Value Analysis**: Test giá trị biên (min-1, min, min+1, max-1, max, max+1)
> 3. **Decision Table**: Bảng quyết định cho logic phức tạp
> 4. **State Transition**: Test chuyển đổi trạng thái
> 5. **Error Guessing**: Đoán lỗi dựa trên kinh nghiệm
>
> Ví dụ EP + BVA cho ô nhập tuổi (1-120): Test 0, 1, 2, 50, 119, 120, 121

### ❓ Q4: Regression Testing là gì? Khi nào và tại sao cần làm?
**✅ Trả lời:**
> Regression Testing là **re-test** các chức năng đã hoạt động tốt sau khi có thay đổi (bug fix, new feature) để đảm bảo **không phát sinh bug mới**.
>
> **Khi nào**: Sau mỗi bug fix, thêm feature, refactor code, upgrade system.
>
> **Tại sao**: Thay đổi ở module A có thể ảnh hưởng module B do dependencies. VD: Fix bug login có thể ảnh hưởng module logout hoặc session management.
>
> **Best practice**: Nên **automate** regression test vì phải chạy lại nhiều lần. Ưu tiên test **critical paths** và **areas affected** by changes.

### ❓ Q5: Smoke Testing vs Sanity Testing?
**✅ Trả lời:**
> - **Smoke Test**: Test **rộng nhưng nông** (broad/shallow) để verify build có stable không? VD: Có mở được app không? Có login được không? Các main features có crash không?
> - **Sanity Test**: Test **hẹp nhưng sâu** (narrow/deep) để verify specific functionality sau minor change. VD: Sau khi fix bug search → test kỹ tất cả scenarios liên quan search.
>
> → Smoke test trước, nếu pass mới sanity test.

### ❓ Q6: Nêu 7 nguyên tắc testing (ISTQB)?
**✅ Trả lời:**
> 1. **Testing shows presence of defects**: Chứng minh có bug, KHÔNG chứng minh không bug
> 2. **Exhaustive testing is impossible**: Không thể test hết → risk-based approach
> 3. **Early testing**: Test sớm → chi phí fix thấp hơn
> 4. **Defect clustering**: 80% bugs ở 20% modules (Pareto)
> 5. **Pesticide paradox**: Cùng test cases lặp lại → không tìm bug mới → cần update
> 6. **Testing is context-dependent**: Test khác nhau tùy context (web vs mobile vs embedded)
> 7. **Absence-of-errors fallacy**: Không bug ≠ đáp ứng user needs

### ❓ Q7: Equivalence Partitioning và Boundary Value Analysis khác gì?
**✅ Trả lời:**
> - **EP**: Chia input thành nhóm tương đương, chọn 1 giá trị đại diện mỗi nhóm
> - **BVA**: Focus vào các giá trị biên vì bugs hay xảy ra ở boundary
>
> VD: Input age 18-60:
> - EP: 3 groups {<18, 18-60, >60} → Test: 10, 30, 70
> - BVA: 6 values → Test: 17, 18, 19, 59, 60, 61
>
> → **Thực tế**: Dùng kết hợp cả EP + BVA cho coverage tốt nhất.

### ❓ Q8: Cho ví dụ viết test case dùng Decision Table?
**✅ Trả lời:**
> VD: Hệ thống tính phí ship:
> - Điều kiện 1: Thành viên VIP? (Yes/No)
> - Điều kiện 2: Đơn hàng > 500k? (Yes/No)
>
> | | TC1 | TC2 | TC3 | TC4 |
> |--|-----|-----|-----|-----|
> | VIP | Y | Y | N | N |
> | > 500k | Y | N | Y | N |
> | **Free Ship** | ✅ | ✅ | ✅ | ❌ |
>
> → 4 test cases cover hết tất cả combinations, không thiếu không thừa.

---
