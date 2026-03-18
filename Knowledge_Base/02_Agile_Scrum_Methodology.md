# 📘 AGILE & SCRUM METHODOLOGY

---

## I. AGILE LÀ GÌ?

### Định nghĩa:
**Agile** là một **phương pháp luận (methodology)** phát triển phần mềm dựa trên phát triển lặp (iterative) và tăng dần (incremental), nơi yêu cầu và giải pháp phát triển thông qua sự hợp tác giữa các team tự tổ chức.

### Agile Manifesto (4 Giá trị cốt lõi):
1. **Individuals and Interactions** > Processes and Tools
2. **Working Software** > Comprehensive Documentation
3. **Customer Collaboration** > Contract Negotiation
4. **Responding to Change** > Following a Plan

### 12 Agile Principles (Tóm tắt):
1. Ưu tiên thỏa mãn khách hàng qua delivery sớm và liên tục
2. Chào đón thay đổi yêu cầu, kể cả muộn
3. Deliver working software thường xuyên (tuần → tháng)
4. Business và Developer làm việc cùng nhau hàng ngày
5. Xây dựng dự án quanh những cá nhân có động lực
6. Giao tiếp trực tiếp (face-to-face) là hiệu quả nhất
7. Working software là thước đo chính
8. Phát triển bền vững (sustainable pace)
9. Chú ý kỹ thuật và thiết kế tốt
10. Simplicity - tối đa hóa công việc không cần làm
11. Team tự tổ chức tạo ra kiến trúc/thiết kế tốt nhất
12. Regularly reflect và điều chỉnh

---

## II. SCRUM FRAMEWORK

### 1. Scrum là gì?
**Scrum** là một **framework** trong Agile, giúp team phát triển, delivery và duy trì sản phẩm phức tạp thông qua các sprint ngắn.

### 2. Ba trụ cột của Scrum (3 Pillars):
- **Transparency** (Minh bạch): Mọi thứ phải visible cho tất cả
- **Inspection** (Kiểm tra): Thường xuyên kiểm tra tiến độ
- **Adaptation** (Thích ứng): Điều chỉnh khi phát hiện vấn đề

### 3. Scrum Roles (Vai trò):

#### 🔵 Product Owner (PO)
- Quản lý **Product Backlog**
- Xác định **priority** cho các features
- Đại diện cho **stakeholders/khách hàng**
- Quyết định **what** (làm cái gì)

#### 🔴 Scrum Master (SM)
- **Servant-leader** cho team
- Loại bỏ **impediments** (trở ngại)
- Đảm bảo team tuân thủ **Scrum process**
- KHÔNG phải là project manager
- Tạo điều kiện cho các **Scrum events**

#### 🟢 Development Team (Dev Team)
- **Cross-functional** (đa chức năng): dev, tester, designer...
- **Self-organizing** (tự tổ chức)
- Kích thước lý tưởng: **3-9 người**
- Quyết định **how** (làm như thế nào)

### 4. Scrum Artifacts (Tạo phẩm):

#### 📋 Product Backlog
- Danh sách **tất cả** features, requirements, bugs, improvements
- Được **PO quản lý** và sắp xếp **priority**
- Là tài liệu **sống** (living document), luôn được cập nhật
- Items thường viết dưới dạng **User Stories**

#### 📝 Sprint Backlog
- Tập con của Product Backlog được **chọn cho sprint hiện tại**
- Bao gồm plan để deliver **Sprint Goal**
- Chỉ **Dev Team** mới được modify

#### 📦 Product Increment
- Tổng của tất cả Product Backlog items **hoàn thành** trong sprint
- Phải đáp ứng **Definition of Done (DoD)**
- Phải ở trạng thái **potentially shippable** (có thể release)

### 5. Scrum Events (Sự kiện):

#### 🔄 Sprint
- Timebox: **1-4 tuần** (thường 2 tuần)
- Tạo ra **Increment** có thể release
- Không thay đổi Sprint Goal trong sprint
- Sprint mới bắt đầu ngay sau sprint cũ kết thúc

#### 📅 Sprint Planning
- Timebox: **Max 8 giờ** cho sprint 1 tháng
- Trả lời: **What** (làm gì trong sprint này?) và **How** (làm như thế nào?)
- Output: **Sprint Backlog + Sprint Goal**

#### 🗣️ Daily Standup (Daily Scrum)
- Timebox: **Max 15 phút**
- Hàng ngày, cùng thời gian, cùng địa điểm
- 3 câu hỏi:
  1. Hôm qua tôi đã làm gì?
  2. Hôm nay tôi sẽ làm gì?
  3. Có trở ngại (impediment) gì không?

#### 🔍 Sprint Review
- Timebox: **Max 4 giờ** cho sprint 1 tháng
- **Demo** sản phẩm cho stakeholders
- Thu thập **feedback**
- Cập nhật Product Backlog

#### 🔄 Sprint Retrospective
- Timebox: **Max 3 giờ** cho sprint 1 tháng
- Team tự đánh giá: **What went well? What didn't? How to improve?**
- Tạo **action items** cho sprint tiếp
- Xảy ra **SAU Sprint Review, TRƯỚC Sprint Planning tiếp**

---

## III. USER STORIES & ESTIMATION

### User Story Format:
```
As a [user role],
I want [feature/capability],
So that [benefit/value].
```

### Ví dụ:
```
As a customer,
I want to search products by name,
So that I can find what I need quickly.
```

### Acceptance Criteria:
- Điều kiện cụ thể để story được coi là **Done**
- Viết theo format **Given-When-Then**

```
Given: I am on the product search page
When: I enter "laptop" in the search bar and click Search
Then: All products containing "laptop" in the name are displayed
And: Results are sorted by relevance
```

### Story Point Estimation:
- Dùng **Fibonacci sequence**: 1, 2, 3, 5, 8, 13, 21
- Đo **effort**, không phải thời gian
- Dùng **Planning Poker** để estimate
- **Velocity** = Tổng story points hoàn thành trong sprint

---

## IV. KANBAN (So sánh với Scrum)

| Tiêu chí | Scrum | Kanban |
|-----------|-------|--------|
| Iteration | Sprint cố định | Continuous flow |
| Roles | PO, SM, Dev Team | Không bắt buộc |
| Planning | Sprint Planning | Không bắt buộc |
| WIP Limit | Sprint backlog | Per column |
| Change | Không đổi trong sprint | Bất kỳ lúc nào |
| Board | Reset mỗi sprint | Persistent |
| Metrics | Velocity | Lead time, Cycle time |

---

## V. CÂU HỎI VÀ TRẢ LỜI (Q&A)

### ❓ Q1: Agile là gì? Nêu các giá trị cốt lõi.
**✅ Trả lời:**
> Agile là methodology phát triển phần mềm theo hướng lặp và tăng dần. 4 giá trị cốt lõi trong Agile Manifesto:
> 1. Con người và tương tác hơn quy trình và công cụ
> 2. Phần mềm hoạt động hơn tài liệu đầy đủ
> 3. Hợp tác với khách hàng hơn đàm phán hợp đồng
> 4. Phản hồi thay đổi hơn tuân theo kế hoạch
>

### ❓ Q2: Scrum có những vai trò nào? Mô tả từng vai trò.
**✅ Trả lời:**
> 3 vai trò chính:
> - **Product Owner**: Quản lý Product Backlog, quyết định priority, đại diện stakeholders. Là người nói "WHAT" (làm cái gì).
> - **Scrum Master**: Servant-leader, loại bỏ impediments, đảm bảo Scrum process. KHÔNG phải project manager.
> - **Development Team**: Cross-functional, self-organizing, 3-9 người. Bao gồm cả Dev và Tester. Quyết định "HOW".
>
> → Lưu ý: **Tester là một phần của Dev Team** trong Scrum, tham gia tất cả activities.

### ❓ Q3: Sprint là gì? Các events trong Sprint?
**✅ Trả lời:**
> Sprint là iteration có timebox 1-4 tuần, thường 2 tuần. Mỗi sprint tạo ra potentially shippable increment. 
> 
> Các events:
> 1. **Sprint Planning** (max 8h): Chọn items từ Product Backlog, tạo Sprint Backlog
> 2. **Daily Standup** (max 15 phút): Sync hàng ngày, 3 câu hỏi
> 3. **Sprint Review** (max 4h): Demo cho stakeholders, thu feedback
> 4. **Sprint Retrospective** (max 3h): Team tự improvement
>
> Thứ tự: Planning → Daily Standups → Review → Retrospective → Next Sprint Planning

### ❓ Q4: Daily Standup gồm những câu hỏi gì?
**✅ Trả lời:**
> 3 câu hỏi:
> 1. **Hôm qua** tôi đã hoàn thành gì?
> 2. **Hôm nay** tôi sẽ làm gì?
> 3. Có **impediment** (trở ngại) nào không?
>
> Lưu ý: Max 15 phút, standing (đứng), không phải report meeting mà là **sync meeting** cho team. Nếu có vấn đề cần thảo luận sâu → "parking lot" để discuss sau.

### ❓ Q5: Sprint Retrospective khác Sprint Review thế nào?
**✅ Trả lời:**

| Tiêu chí | Sprint Review | Sprint Retrospective |
|-----------|--------------|---------------------|
| Mục đích | Demo sản phẩm | Cải tiến quy trình |
| Người tham gia | Team + Stakeholders | Chỉ Scrum Team |
| Focus | Product (WHAT) | Process (HOW) |
| Output | Updated Backlog | Action Items |
| Khi nào | Cuối sprint | Sau Review |
| Câu hỏi | Làm được gì? Thiếu gì? | Tốt gì? Xấu gì? Cải thiện gì? |

### ❓ Q6: Product Backlog vs Sprint Backlog?
**✅ Trả lời:**
> - **Product Backlog**: Toàn bộ wish-list của sản phẩm, do PO quản lý, living document
> - **Sprint Backlog**: Subset của Product Backlog cho sprint hiện tại, do Dev Team quản lý
>
> Ví dụ: Product Backlog có 100 items → Sprint Planning chọn 10 items phù hợp capacity → Sprint Backlog = 10 items đó + plan thực hiện.

### ❓ Q7: User Story là gì? Cho ví dụ.
**✅ Trả lời:**
> User Story là cách mô tả requirement từ góc nhìn end-user. Format:
> *"As a [role], I want [feature], so that [benefit]"*
>
> Ví dụ: *"As a customer, I want to reset my password via email, so that I can access my account when I forget my password."*
>
> Acceptance Criteria (Given-When-Then):
> - Given: I am on the login page
> - When: I click "Forgot Password" and enter my email
> - Then: I receive a password reset link within 5 minutes

### ❓ Q8: Definition of Done (DoD) là gì?
**✅ Trả lời:**
> DoD là **checklist tiêu chí** mà một work item phải đáp ứng để được coi là "hoàn thành". DoD được team thống nhất và áp dụng consistently. Ví dụ:
> - Code đã được review
> - Unit tests pass 100%
> - Integration tests pass
> - Code đã merge vào main branch
> - Documentation cập nhật
> - PO đã accept
>
> → DoD khác Acceptance Criteria: AC cho từng story, DoD cho tất cả stories.

### ❓ Q9: Velocity là gì? Tại sao quan trọng?
**✅ Trả lời:**
> **Velocity** = Tổng Story Points hoàn thành trong 1 sprint. Ví dụ: Sprint 1 = 20 points, Sprint 2 = 25 points, Sprint 3 = 22 points → Average Velocity = 22.3 points.
>
> **Quan trọng vì**:
> - Giúp **estimate** capacity cho sprint tiếp theo
> - Giúp **predict** khi nào release
> - Track **team performance** theo thời gian
> - KHÔNG dùng để **so sánh** giữa các team

### ❓ Q10: Burndown Chart là gì?
**✅ Trả lời:**
> Burndown Chart hiển thị **lượng công việc còn lại** theo thời gian trong sprint.
> - Trục X: Thời gian (ngày)
> - Trục Y: Story Points / Tasks còn lại
> - **Ideal line**: Đường thẳng giảm đều từ tổng xuống 0
> - **Actual line**: Đường thực tế
>
> Nếu actual > ideal → team đang chậm tiến độ
> Nếu actual < ideal → team đang nhanh hơn dự kiến

---

## VI. VAI TRÒ CỦA TESTER TRONG AGILE/SCRUM

### Tester trong Agile Team:
1. **Sprint Planning**: Estimate test effort, identify risks
2. **During Sprint**: Viết test cases, execute test, report bugs
3. **Daily Standup**: Report tiến độ test
4. **Sprint Review**: Demo test results
5. **Retrospective**: Đề xuất cải tiến test process

### Agile Testing Practices:
- **TDD (Test-Driven Development)**: Viết test trước, code sau
- **BDD (Behavior-Driven Development)**: Test dựa trên behavior
- **Continuous Testing**: Test liên tục trong CI/CD
- **Exploratory Testing**: Test không theo script, dựa trên kinh nghiệm
- **Pair Testing**: 2 người test cùng nhau

### Testing Quadrants:

```
         Business-Facing
              |
   Q2         |        Q3
 Automated    | Manual
 Functional   | Exploratory
 Tests        | Usability
              | UAT
 -------------|-------------
   Q1         |        Q4
 Automated    | Tools
 Unit Tests   | Performance
 Component    | Security
 Tests        | 
              |
        Technology-Facing
```

---
