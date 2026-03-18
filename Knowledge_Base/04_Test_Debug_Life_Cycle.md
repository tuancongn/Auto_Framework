# 📘 TEST LIFE CYCLE & BUG/DEFECT LIFE CYCLE

---

## I. STLC - SOFTWARE TESTING LIFE CYCLE

### 1. STLC là gì?
**STLC** là quy trình có hệ thống để thực hiện testing, bắt đầu từ khi nhận requirements đến khi hoàn thành test closure.

### 2. Các giai đoạn STLC:

### Phase 1: Requirement Analysis (Phân tích yêu cầu)
**Input**: Requirements Document (SRS, BRS, FRS)
**Activities**:
- Review requirements để hiểu rõ
- Xác định **testable requirements** và **non-testable requirements**
- Xác định **testing scope**
- Trao đổi với BA/PO nếu có yêu cầu không rõ ràng
- Tạo danh sách câu hỏi (**queries**)
- Xác định loại testing cần thực hiện

**Output**: RTM (Requirement Traceability Matrix), Automation Feasibility Report

### Phase 2: Test Planning (Lập kế hoạch test)
**Input**: Requirements, RTM, Automation Feasibility
**Activities**:
- Xác định **test strategy** (approach, scope, types of testing)
- Ước tính **effort** và **timeline**
- Xác định **resources** (con người, tool, environment)
- Xác định **risk** và **mitigation plan**
- Định nghĩa **Entry/Exit criteria**
- Xác định **test deliverables**

**Output**: **Test Plan Document**

**Test Plan bao gồm:**
1. Test Plan Identifier
2. Introduction
3. Test Items (features to test)
4. Features not to be tested
5. Test Approach / Strategy
6. Pass/Fail Criteria
7. Entry Criteria / Exit Criteria
8. Test Deliverables
9. Test Environment
10. Resource & Schedule
11. Risk & Contingencies
12. Approvals

### Phase 3: Test Case Development (Phát triển test case)
**Input**: Requirements, Test Plan
**Activities**:
- Viết **Test Cases** chi tiết
- Viết **Test Scripts** (nếu automation)
- Chuẩn bị **Test Data**
- Review test cases (peer review)

**Output**: Test Cases, Test Scripts, Test Data

**Test Case Template:**
| Field | Mô tả |
|-------|--------|
| TC ID | Mã định danh duy nhất |
| TC Title | Tên mô tả ngắn gọn |
| Module | Module liên quan |
| Priority | High/Medium/Low |
| Pre-conditions | Điều kiện tiên quyết |
| Test Steps | Các bước thực hiện chi tiết |
| Test Data | Dữ liệu test cụ thể |
| Expected Result | Kết quả mong đợi |
| Actual Result | Kết quả thực tế |
| Status | Pass/Fail/Blocked/Not Run |
| Post-conditions | Trạng thái sau test |

### Phase 4: Test Environment Setup (Thiết lập môi trường test)
**Input**: Test Plan, Environment specs
**Activities**:
- Setup **hardware & software** cho testing
- Setup **test tools**
- Chuẩn bị **test data** trong environment
- **Smoke test** environment

**Output**: Ready Test Environment, Smoke Test Results

### Phase 5: Test Execution (Thực thi test)
**Input**: Test Cases, Test Data, Test Environment
**Activities**:
- **Execute** test cases theo kế hoạch
- So sánh **Actual vs Expected** results
- Log **bugs/defects** cho failed test cases
- **Re-test** sau khi dev fix bugs
- **Regression test** sau mỗi build
- Cập nhật **test status** 

**Output**: Test Execution Results, Bug Reports, Updated RTM

### Phase 6: Test Cycle Closure (Kết thúc test)
**Input**: Test results, Bug reports
**Activities**:
- Đánh giá **Exit Criteria** đã đạt chưa
- Tạo **Test Summary Report**
- Tổng hợp **Test Metrics**
- Lưu trữ **test artifacts** (test cases, reports...)
- **Lessons Learned** meeting
- Đề xuất cải tiến cho dự án sau

**Output**: Test Closure Report, Test Metrics, Lessons Learned

---

## II. ENTRY CRITERIA & EXIT CRITERIA

### Entry Criteria (Điều kiện bắt đầu test):
- ✅ Requirements đã được review và approve
- ✅ Test Plan đã được sign-off
- ✅ Test Cases đã được review
- ✅ Test Environment đã ready
- ✅ Test Data đã sẵn sàng
- ✅ Build đã deploy lên test environment
- ✅ Smoke test đã pass

### Exit Criteria (Điều kiện kết thúc test):
- ✅ Tất cả test cases đã được execute
- ✅ X% test cases pass (ví dụ: 95%)
- ✅ Không có **Critical/Blocker** bugs open
- ✅ Tất cả **High** priority bugs đã fixed & verified
- ✅ Test Summary Report đã hoàn thành
- ✅ PO/Stakeholder đã approve

---

## III. BUG/DEFECT LIFE CYCLE ⭐ TRỌNG TÂM

### 1. Các thuật ngữ:
- **Bug/Defect**: Lỗi trong phần mềm - kết quả thực tế khác kết quả mong đợi
- **Error**: Sai lầm của con người (developer viết code sai)
- **Fault**: Kết quả của Error trong code (code chứa logic sai)
- **Failure**: Khi Fault được thực thi và gây ra hành vi sai

> **Error → Fault → Failure → Defect (được tìm thấy bởi Tester)**

### 2. Bug Life Cycle (Vòng đời Bug):

```
┌──────────┐
│   NEW    │ ← Tester tìm thấy bug và log
└────┬─────┘
     │
     ▼
┌──────────┐     ┌──────────┐
│ ASSIGNED │────►│ REJECTED │ ← Lead/Dev reject (not a bug, duplicate...)
└────┬─────┘     └──────────┘
     │
     ▼
┌──────────┐     ┌──────────┐
│   OPEN   │────►│ DEFERRED │ ← Fix ở phiên bản sau
└────┬─────┘     └──────────┘
     │
     ▼
┌──────────┐     ┌──────────┐
│  FIXED   │────►│ NOT      │
└────┬─────┘     │REPRODUCIBLE│ ← Không tái hiện được
     │           └──────────┘
     ▼
┌──────────┐
│ RETEST   │ ← Tester verify bug fix
└────┬─────┘
     │
    ┌┴──────────┐
    ▼            ▼
┌──────────┐  ┌──────────┐
│ VERIFIED │  │ REOPENED  │ ← Bug chưa fix đúng
└────┬─────┘  └──────────┘
     │              │
     ▼              └──► Quay lại OPEN
┌──────────┐
│  CLOSED  │ ← Bug đã fix thành công
└──────────┘
```

### 3. Chi tiết các trạng thái:

| Status | Mô tả | Ai thực hiện |
|--------|--------|-------------|
| **New** | Bug vừa được log | Tester |
| **Assigned** | Bug assign cho developer | Test Lead/Manager |
| **Open** | Dev bắt đầu analyze bug | Developer |
| **Fixed** | Dev đã sửa bug | Developer |
| **Retest** | Tester verify bug fix | Tester |
| **Verified** | Confirm bug đã fix đúng | Tester |
| **Closed** | Bug hoàn toàn resolved | Tester/Lead |
| **Reopened** | Bug chưa fix đúng hoặc tái hiện | Tester |
| **Rejected** | Không phải bug (working as designed) | Dev/Lead |
| **Deferred** | Fix ở phiên bản sau | Manager/PO |
| **Duplicate** | Trùng với bug đã log | Dev/Lead |
| **Not Reproducible** | Không tái hiện được | Dev |

### 4. Bug Report Template:

| Field | Ví dụ |
|-------|-------|
| **Bug ID** | BUG-001 |
| **Title** | Login failed with valid credentials on Chrome |
| **Module** | Authentication |
| **Environment** | Chrome 120, Windows 11, Test Server |
| **Severity** | Critical |
| **Priority** | High |
| **Steps to Reproduce** | 1. Go to login page → 2. Enter valid email/pass → 3. Click Login |
| **Expected Result** | User logged in, redirected to Dashboard |
| **Actual Result** | Error message "Server Error 500" displayed |
| **Attachments** | Screenshot, Video recording, Log file |
| **Reported By** | Tester Name |
| **Reported Date** | 2026-03-20 |
| **Assigned To** | Developer Name |
| **Status** | New |

### 5. Bug Severity vs Priority:

#### Severity (Mức độ nghiêm trọng - Technical):
| Level | Mô tả | Ví dụ |
|-------|--------|-------|
| **Critical/Blocker** | System crash, data loss, không thể tiếp tục | App crash khi mở, mất dữ liệu |
| **Major/High** | Chức năng chính không hoạt động | Không thể checkout, payment fail |
| **Medium** | Chức năng hoạt động nhưng không đúng | Tính sai giá, sort sai |
| **Minor/Low** | Cosmetic, UI issues | Typo, alignment sai, color sai |

#### Priority (Mức độ ưu tiên - Business):
| Level | Mô tả | Ví dụ |
|-------|--------|-------|
| **Urgent/P1** | Fix ngay lập tức | Production down |
| **High/P2** | Fix trong sprint hiện tại | Core feature broken |
| **Medium/P3** | Fix trong sprint tiếp | Non-critical bug |
| **Low/P4** | Fix khi có thời gian | Minor improvement |

#### ⭐ QUAN TRỌNG - Severity ≠ Priority:

| Scenario | Severity | Priority | Ví dụ |
|----------|----------|----------|-------|
| High Severity + High Priority | Critical | Urgent | Payment gateway crash |
| High Severity + Low Priority | Critical | Low | Crash ở feature ít dùng |
| Low Severity + High Priority | Minor | Urgent | Logo sai trên trang chủ (branding) |
| Low Severity + Low Priority | Minor | Low | Typo ở trang "About Us" |

---

## IV. TEST METRICS

### Các Metrics quan trọng:

```
Test Case Pass Rate = (Passed TCs / Total Executed TCs) × 100%
Test Case Fail Rate = (Failed TCs / Total Executed TCs) × 100%
Defect Density = Total Defects / Size of Software (KLOC)
Defect Leakage = Defects found in Production / Total Defects × 100%
Defect Removal Efficiency = Defects found in Testing / Total Defects × 100%
Test Coverage = (Requirements Tested / Total Requirements) × 100%
Test Execution Rate = (TCs Executed / Total TCs) × 100%
```

---

## V. RTM - REQUIREMENT TRACEABILITY MATRIX

### RTM là gì?
**RTM** là bảng mapping giữa **Requirements** ↔ **Test Cases** để đảm bảo mọi requirement đều được test.

### Ví dụ RTM:
| Req ID | Requirement | TC IDs | Status |
|--------|-------------|--------|--------|
| REQ-01 | User can login | TC-01, TC-02, TC-03 | Covered |
| REQ-02 | User can register | TC-04, TC-05 | Covered |
| REQ-03 | Password reset | TC-06 | Covered |
| REQ-04 | Profile update | - | ❌ NOT Covered |

### Lợi ích RTM:
- Đảm bảo **100% test coverage**
- Phát hiện **requirements chưa được test**
- Track **impact analysis** khi requirement thay đổi

---

## VI. CÂU HỎI VÀ TRẢ LỜI (Q&A)

### ❓ Q1: Mô tả Bug Life Cycle.
**✅ Trả lời:**
> Bug Life Cycle bắt đầu khi Tester tìm thấy bug:
> **New → Assigned → Open → Fixed → Retest → Verified → Closed**
>
> Các nhánh phụ:
> - **Rejected**: Dev xác nhận không phải bug (by design, duplicate)
> - **Deferred**: Tạm hoãn, fix ở version sau
> - **Reopened**: Tester verify thấy bug chưa fix đúng → quay lại Open
> - **Not Reproducible**: Dev không tái hiện được → cần thêm info
>
> Lưu ý: Tester có trách nhiệm **verify** bug fix, không để dev tự close bug.

### ❓ Q2: Severity vs Priority khác nhau thế nào? Cho ví dụ.
**✅ Trả lời:**
> - **Severity** = Mức độ nghiêm trọng **kỹ thuật** (impact lên system)
> - **Priority** = Mức độ ưu tiên fix **từ góc nhìn business**
>
> **Ví dụ quan trọng:**
> - **High Severity + Low Priority**: App crash khi nhấn nút Z → nghiêm trọng nhưng feature Z ít ai dùng → fix sau
> - **Low Severity + High Priority**: Logo công ty hiển thị sai trên homepage → chỉ UI nhưng ảnh hưởng branding → fix ngay
>
> → **Severity do Tester set, Priority do Manager/PO quyết định** dựa trên business needs.

### ❓ Q3: Nêu các giai đoạn của STLC.
**✅ Trả lời:**
> 6 giai đoạn:
> 1. **Requirement Analysis**: Phân tích yêu cầu, xác định testable items
> 2. **Test Planning**: Lập test plan, strategy, estimate, resources
> 3. **Test Case Development**: Viết test cases, chuẩn bị test data
> 4. **Test Environment Setup**: Thiết lập môi trường test
> 5. **Test Execution**: Chạy test, log bugs, retest, regression
> 6. **Test Closure**: Report, metrics, lessons learned
>
> Mỗi phase có **Entry Criteria** (điều kiện bắt đầu) và **Exit Criteria** (điều kiện kết thúc).

### ❓ Q4: Entry Criteria và Exit Criteria là gì?
**✅ Trả lời:**
> - **Entry Criteria**: Prerequisites phải đáp ứng **TRƯỚC** khi bắt đầu testing. VD: Requirements approved, test environment ready, build deployed.
> - **Exit Criteria**: Conditions phải đáp ứng **ĐỂ** kết thúc testing. VD: 95% test cases pass, no critical bugs open, test report completed.
>
> → Nếu Entry Criteria chưa đạt → chưa bắt đầu test (tránh waste effort)
> → Nếu Exit Criteria chưa đạt → chưa release (tránh release sản phẩm lỗi)

### ❓ Q5: Viết bug report cần những thông tin gì?
**✅ Trả lời (Senior-level):**
> Một bug report tốt cần:
> 1. **Title**: Ngắn gọn, rõ ràng, mô tả bug
> 2. **Steps to Reproduce**: Chi tiết từng bước (1, 2, 3...)
> 3. **Expected Result**: Kết quả đúng theo requirement
> 4. **Actual Result**: Kết quả thực tế (sai)
> 5. **Severity & Priority**: Đánh giá mức độ
> 6. **Environment**: Browser, OS, device, URL
> 7. **Attachments**: Screenshot, video, log files
>
> **Tip Senior**: Bug title nên theo format: `[Module] - [What happened] - [Where/When]`
> VD: "Authentication - Login fails with valid credentials - Chrome 120"

### ❓ Q6: Error, Fault, Failure, Defect khác nhau thế nào?
**✅ Trả lời:**
> - **Error**: Sai lầm của CON NGƯỜI (developer nghĩ sai logic)
> - **Fault/Bug**: Kết quả của Error TRONG CODE (code chứa logic sai)
> - **Failure**: Khi Fault được THỰC THI và gây ra hành vi sai (runtime)
> - **Defect**: Fault được TESTER TÌM THẤY và log vào bug tracker
>
> Flow: Error (human mistake) → Fault (in code) → Failure (at runtime) → Defect (found by tester)

### ❓ Q7: Test Plan bao gồm những gì?
**✅ Trả lời:**
> Test Plan gồm:
> 1. **Scope**: Features sẽ test / không test
> 2. **Test Strategy**: Approach, types of testing
> 3. **Entry/Exit Criteria**: Điều kiện bắt đầu/kết thúc
> 4. **Resource Plan**: Con người, tools, environment
> 5. **Schedule**: Timeline, milestones
> 6. **Risk & Mitigation**: Rủi ro và cách xử lý
> 7. **Test Deliverables**: Các output documents
>
> → Test Plan là **sống** (living document), cập nhật khi cần.

### ❓ Q8: RTM là gì? Tại sao cần?
**✅ Trả lời:**
> **RTM (Requirement Traceability Matrix)** là bảng mapping Requirements ↔ Test Cases. 
>
> **Cần RTM vì**:
> - Đảm bảo **100% requirements** đều được test (no gaps)
> - Khi requirement thay đổi → biết cần update **test cases nào** (impact analysis)
> - Khi report → biết **test coverage** bao nhiêu %
> - Khi bug found → trace back **requirement nào** bị ảnh hưởng

---
