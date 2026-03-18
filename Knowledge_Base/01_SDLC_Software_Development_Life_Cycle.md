# 📘 SDLC - SOFTWARE DEVELOPMENT LIFE CYCLE

---

## I. TỔNG QUAN VỀ SDLC

### 1. SDLC là gì?
**SDLC (Software Development Life Cycle)** là quy trình có cấu trúc dùng để phát triển phần mềm chất lượng cao, đáp ứng yêu cầu khách hàng, hoàn thành trong thời gian và chi phí ước tính.

### 2. Mục đích của SDLC:
- Cung cấp **framework** có cấu trúc cho việc phát triển phần mềm
- Đảm bảo sản phẩm đáp ứng **yêu cầu khách hàng**
- Kiểm soát **chi phí** và **thời gian**
- Đảm bảo **chất lượng** sản phẩm

---

## II. CÁC GIAI ĐOẠN CỦA SDLC (7 Phases)

### Phase 1: Planning (Lập kế hoạch)
- Xác định phạm vi dự án (scope)
- Ước tính chi phí, nguồn lực, thời gian
- Phân tích khả thi (Feasibility Study)
- Output: **Project Plan, Feasibility Report**

### Phase 2: Requirement Analysis (Phân tích yêu cầu)
- Thu thập yêu cầu từ stakeholders
- Phân tích yêu cầu chức năng (Functional Requirements) và phi chức năng (Non-Functional Requirements)
- Output: **SRS (Software Requirement Specification)**

### Phase 3: Design (Thiết kế)
- **HLD (High Level Design)**: Kiến trúc hệ thống, công nghệ sử dụng, module chính
- **LLD (Low Level Design)**: Thiết kế chi tiết từng module, database schema, API design
- Output: **Design Document (HLD + LLD)**

### Phase 4: Implementation/Coding (Lập trình)
- Viết code dựa trên design document
- Code review
- Unit testing bởi developer
- Output: **Source Code**

### Phase 5: Testing (Kiểm thử)
- Thực hiện các loại test: Unit, Integration, System, UAT
- Tìm và báo cáo bug
- Verify bug fixes
- Output: **Test Reports, Bug Reports**

### Phase 6: Deployment (Triển khai)
- Deploy lên production environment
- Có thể deploy theo giai đoạn (phased deployment)
- Smoke testing sau deploy
- Output: **Deployed System**

### Phase 7: Maintenance (Bảo trì)
- Fix bugs phát sinh từ production
- Enhancement (cải tiến)
- Monitoring và support
- Output: **Updated System, Patch Releases**

---

## III. CÁC MÔ HÌNH SDLC PHỔ BIẾN

### 1. Waterfall Model (Mô hình thác nước)
```
Planning → Requirements → Design → Implementation → Testing → Deployment → Maintenance
```
- **Đặc điểm**: Tuần tự, mỗi phase hoàn thành mới chuyển sang phase tiếp
- **Ưu điểm**: Đơn giản, dễ quản lý, tài liệu rõ ràng
- **Nhược điểm**: Không linh hoạt, khó thay đổi yêu cầu, phát hiện lỗi muộn
- **Phù hợp**: Dự án nhỏ, yêu cầu rõ ràng và ít thay đổi

### 2. V-Model (Verification & Validation)
```
Requirements  ←→  Acceptance Testing
  System Design  ←→  System Testing
    Architecture Design  ←→  Integration Testing
      Module Design  ←→  Unit Testing
            Coding
```
- **Đặc điểm**: Mỗi phase phát triển có phase testing tương ứng
- **Ưu điểm**: Testing được plan sớm, phát hiện lỗi sớm hơn Waterfall
- **Nhược điểm**: Vẫn tuần tự, khó thay đổi yêu cầu
- **Phù hợp**: Dự án yêu cầu chất lượng cao, ít thay đổi

### 3. Iterative Model (Mô hình lặp)
- Phát triển qua nhiều iteration (vòng lặp)
- Mỗi iteration tạo ra phiên bản hoàn chỉnh hơn
- **Ưu điểm**: Linh hoạt, feedback sớm
- **Nhược điểm**: Khó quản lý, chi phí có thể tăng

### 4. Spiral Model (Mô hình xoắn ốc)
- Kết hợp Iterative + Waterfall + Risk Analysis
- 4 phases trong mỗi spiral: Planning, Risk Analysis, Engineering, Evaluation
- **Ưu điểm**: Quản lý risk tốt
- **Nhược điểm**: Chi phí cao, phức tạp
- **Phù hợp**: Dự án lớn, rủi ro cao

### 5. Agile Model
- Phát triển qua nhiều sprint ngắn (2-4 tuần)
- Continuous delivery, feedback liên tục
- **Ưu điểm**: Linh hoạt cao, thích ứng thay đổi
- **Nhược điểm**: Cần team experience, khó estimate
- **Phù hợp**: Dự án yêu cầu thay đổi liên tục

### 6. DevOps Model
- Tích hợp Development + Operations
- CI/CD (Continuous Integration / Continuous Deployment)
- Automation testing, monitoring
- **Ưu điểm**: Release nhanh, phản hồi nhanh
- **Nhược điểm**: Yêu cầu văn hóa và công cụ phù hợp

---

## IV. CÂU HỎI VÀ TRẢ LỜI (Q&A)

### ❓ Q1: SDLC là gì? Liệt kê các giai đoạn chính.
**✅ Trả lời:**
> SDLC là một quy trình có hệ thống để phát triển phần mềm chất lượng cao. Gồm 7 giai đoạn: **Planning → Requirement Analysis → Design → Implementation → Testing → Deployment → Maintenance**. Mỗi giai đoạn có input, output và deliverables rõ ràng. Vai trò của Tester bắt đầu từ phase Requirement Analysis (review SRS) chứ không chỉ ở phase Testing.

### ❓ Q2: So sánh Waterfall và Agile?
**✅ Trả lời:**
| Tiêu chí | Waterfall | Agile |
|-----------|-----------|-------|
| Approach | Tuần tự (Sequential) | Lặp lại (Iterative) |
| Yêu cầu | Cố định từ đầu | Thay đổi liên tục |
| Testing | Sau khi coding xong | Trong mọi sprint |
| Delivery | Cuối dự án | Sau mỗi sprint |
| Feedback | Muộn | Liên tục |
| Documentation | Nặng | Nhẹ, vừa đủ |
| Risk | Phát hiện muộn | Phát hiện sớm |
| Phù hợp | Dự án yêu cầu rõ ràng, ít thay đổi | Dự án cần flexibility |

### ❓ Q3: V-Model khác Waterfall như thế nào?
**✅ Trả lời:**
> V-Model là mở rộng của Waterfall, nhưng **mỗi phase development có phase testing tương ứng** được plan song song. Ví dụ: Requirement → Acceptance Test Plan, System Design → System Test Plan. Điều này giúp phát hiện lỗi sớm hơn Waterfall. Tuy nhiên cả hai đều sequential và không linh hoạt khi yêu cầu thay đổi.

### ❓ Q4: Khi nào nên dùng Waterfall? Khi nào nên dùng Agile?
**✅ Trả lời:**
> - **Waterfall**: Khi requirements rõ ràng, ổn định, không thay đổi. VD: dự án embedded system, banking compliance.
> - **Agile**: Khi requirements có thể thay đổi, cần feedback sớm từ khách hàng, cần delivery nhanh. VD: web/mobile app, startup product.
> - Thực tế tại FPT Software, nhiều dự án dùng **Hybrid** - kết hợp cả hai tùy theo yêu cầu khách hàng Nhật/Mỹ.

### ❓ Q5: Tester tham gia SDLC từ giai đoạn nào?
**✅ Trả lời:**
> Tester tham gia **từ giai đoạn Requirement Analysis**, không phải chỉ ở phase Testing. Cụ thể:
> - **Requirement**: Review SRS, tìm ambiguity, missing requirements
> - **Design**: Review design docs, plan test strategy
> - **Coding**: Prepare test cases, test data
> - **Testing**: Execute tests, report bugs
> - **Deployment**: Sanity/Smoke testing
> - **Maintenance**: Regression testing
>
> → Nguyên tắc: **"Test early, test often"** - Phát hiện bug càng sớm, chi phí fix càng thấp (Cost of Defect tăng theo giai đoạn).

### ❓ Q6: SRS là gì? Tại sao quan trọng với Tester?
**✅ Trả lời:**
> **SRS (Software Requirement Specification)** là tài liệu mô tả chi tiết tất cả yêu cầu chức năng và phi chức năng của phần mềm. Với Tester, SRS là **baseline** để:
> - Viết test cases
> - Xác định expected results
> - Đo test coverage
> - Phát hiện lỗi requirement (thiếu, mâu thuẫn, không rõ ràng)
>
> Nếu SRS không rõ ràng → test case sai → bug escape → chi phí sửa lỗi cao.

### ❓ Q7: Giải thích "Cost of Defect" trong SDLC?
**✅ Trả lời (Senior-level):**
> Chi phí sửa lỗi tăng **gấp 10 lần** mỗi khi chuyển sang giai đoạn tiếp theo:
> - Requirements: **1x**
> - Design: **5x**
> - Coding: **10x**
> - Testing: **20x**
> - Production: **100x** hoặc hơn
>
> → Đây là lý do Tester cần tham gia sớm (Shift-Left Testing) và Testing không chỉ là "tìm bug" mà còn là "ngăn bug phát sinh".

### ❓ Q8: Feasibility Study trong SDLC gồm những gì?
**✅ Trả lời:**
> Feasibility Study đánh giá 5 khía cạnh:
> 1. **Technical Feasibility**: Công nghệ có khả thi không?
> 2. **Economic Feasibility**: Chi phí có hợp lý không?
> 3. **Operational Feasibility**: Hệ thống có vận hành được không?
> 4. **Schedule Feasibility**: Có hoàn thành đúng deadline không?
> 5. **Legal Feasibility**: Có vấn đề pháp lý không?

---
