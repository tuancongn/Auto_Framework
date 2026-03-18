# 📘 CÂU HỎI TÌNH HUỐNG (SITUATIONAL QUESTIONS)

---

## I. TÌNH HUỐNG VỀ BUG & DEFECT

### ❓ Tình huống 1: Bạn tìm thấy bug nhưng Developer nói "It's not a bug, it's working as designed." Bạn xử lý thế nào?

**✅ Trả lời:**
> 1. **Kiểm tra lại SRS/Requirements**: So sánh actual behavior với requirement spec
> 2. **Nếu requirement rõ ràng**: Trích dẫn requirement cụ thể, gửi evidence (screenshot, video) cho Dev
> 3. **Nếu requirement không rõ**: Escalate lên **BA/PO** để clarify requirement
> 4. **Nếu Dev vẫn reject**: Escalate lên **Test Lead/Manager** với full evidence
> 5. **KHÔNG argue trực tiếp** - dùng facts & documents, không dùng cảm xúc
>
> **Key point**: Bug hay không phải bug là decision dựa trên **requirement**, không phải ý kiến cá nhân.

---

### ❓ Tình huống 2: Deadline sắp đến, còn rất nhiều test cases chưa chạy. Bạn làm gì?

**✅ Trả lời:**
> 1. **Risk-Based Testing**: Ưu tiên test cases theo **risk** và **impact**
>    - Critical > High > Medium > Low
>    - Core business flows trước, edge cases sau
> 2. **Báo cáo Test Lead/PM** về tình trạng, đưa ra **risk assessment**
> 3. **Focus vào Smoke + Sanity Testing** cho core features
> 4. **Tạo Test Summary Report** nêu rõ: đã test gì, chưa test gì, risks
> 5. **KHÔNG skip testing** mà không thông báo
> 6. **KHÔNG giảm chất lượng test** - thà test ít mà kỹ
>
> **Key point**: Transparent communication + Risk-based prioritization

---

### ❓ Tình huống 3: Bạn phát hiện bug nghiêm trọng (Critical) gần sát ngày release. Bạn làm gì?

**✅ Trả lời:**
> 1. **Log bug ngay lập tức** với đầy đủ thông tin + evidence
> 2. **Báo cáo trực tiếp** cho Test Lead và PM (không chỉ qua tool)
> 3. **Đánh giá impact**: Bug ảnh hưởng bao nhiêu users? Data loss? Security?
> 4. **Đề xuất options cho team**:
>    - Option A: Fix bug + delay release
>    - Option B: Workaround + release + hotfix sau
>    - Option C: Disable feature + release + fix ở version sau
> 5. **Quyết định là của PM/PO/Management** - Tester provide information & recommendation
>
> **Key point**: Tester có trách nhiệm **report & inform**, không có quyền quyết định release.

---

### ❓ Tình huống 4: Bug "not reproducible" - Dev không tái hiện được. Bạn xử lý thế nào?

**✅ Trả lời:**
> 1. **Verify lại** trên environment của mình - bug có còn không?
> 2. **Kiểm tra environment differences**: OS, browser version, data, config
> 3. **Cung cấp chi tiết hơn**: Exact steps, exact data, exact environment settings
> 4. **Quay video** reproduce bug
> 5. **Thu thập logs**: Browser console, server logs, network calls
> 6. **Thử reproduce trên Dev's environment**: Pair với Dev để debug
> 7. Nếu vẫn không reproduce → **Log environment info** + mark "Cannot Reproduce" nhưng **keep monitoring**
>
> **Key point**: "Cannot reproduce" ≠ "Not a bug". Có thể là intermittent bug do timing, data state, race condition.

---

### ❓ Tình huống 5: Requirement không rõ ràng / thiếu. Bạn làm gì?

**✅ Trả lời:**
> 1. **Liệt kê câu hỏi cụ thể** (không hỏi chung chung "requirement không rõ")
> 2. **Hỏi BA/PO** để clarify
> 3. **Document** câu trả lời và update requirement
> 4. **Nếu không có ai để hỏi**: Viết test case theo cả hai cách hiểu, ghi note assumption
> 5. **KHÔNG giả định** và test theo ý mình mà không confirm
>
> **Key point**: Requirement ambiguity là một loại defect → tìm ra sớm → tiết kiệm chi phí.

---

## II. TÌNH HUỐNG VỀ TEST PROCESS

### ❓ Tình huống 6: Build mới bị lỗi nhiều, Smoke Test fail. Bạn làm gì?

**✅ Trả lời:**
> 1. **KHÔNG tiếp tục test** → tiết kiệm effort
> 2. **Report Smoke Test results** cho Dev Team và Lead
> 3. **Reject build** - yêu cầu Dev fix và deploy build mới
> 4. **Chỉ resume testing** khi build mới pass Smoke Test
>
> **Key point**: Entry Criteria chưa đạt → chưa bắt đầu test execution. Testing trên build lỗi = waste of time.

---

### ❓ Tình huống 7: Dev fix bug này lại gây thêm bug khác. Bạn xử lý thế nào?

**✅ Trả lời:**
> 1. **Log bug mới** (đây là regression bug)
> 2. **Link** bug mới với bug gốc để track dependency
> 3. **Report** cho Dev và Lead
> 4. **Chạy Regression Testing** trên affected areas
> 5. **Phân tích root cause**: Tại sao fix A lại break B? → Review code dependencies
> 6. **Đề xuất**: Cần thêm unit tests cho related modules, cần code review kỹ hơn
>
> **Key point**: Đây chính là lý do cần **Regression Testing** sau mỗi bug fix.

---

### ❓ Tình huống 8: Bạn không đồng ý với priority mà PM đặt cho bug. Bạn xử lý thế nào?

**✅ Trả lời:**
> 1. **Trình bày reasoning** với data: impact analysis, affected users, business logic
> 2. **Cung cấp evidence**: Screenshots, videos, metrics
> 3. **Đề xuất priority** kèm lý do cụ thể
> 4. **Nếu PM vẫn giữ nguyên**: Respect decision, document disagreement
> 5. **KHÔNG tự ý đổi priority** khi PM đã quyết định
>
> **Key point**: Tester có quyền **recommend**, PM/PO có quyền **decide**.

---

### ❓ Tình huống 9: Bạn được giao test một module mà bạn không hiểu business logic. Bạn làm gì?

**✅ Trả lời:**
> 1. **Đọc kỹ requirement documents**: SRS, User Stories, Mockups
> 2. **Hỏi BA/PO** về business flow
> 3. **Tham khảo similar systems**: Nghiên cứu domain knowledge
> 4. **Shadow với experienced team members**: Hỏi senior tester/dev
> 5. **Viết test cases** và nhờ review trước khi execute
> 6. **KHÔNG test khi chưa hiểu** → sẽ miss nhiều scenarios quan trọng
>
> **Key point**: Domain knowledge là yếu tố quan trọng để test hiệu quả.

---

### ❓ Tình huống 10: Bạn phát hiện cùng 1 bug xuất hiện lặp lại nhiều lần dù đã fix. Bạn xử lý thế nào?

**✅ Trả lời (Senior-level):**
> 1. **Log lại** mỗi lần xuất hiện, link đến bug gốc
> 2. **Báo cáo Test Lead và Dev Lead** - đây là systematic issue
> 3. **Yêu cầu Root Cause Analysis (RCA)**: Tại sao bug cứ quay lại?
> 4. **Possible causes**: 
>    - Code không merge đúng branch
>    - Thiếu unit test
>    - Dev fix triệu chứng, không fix root cause
>    - Environment configuration khác nhau
> 5. **Đề xuất**: Tăng unit test coverage, code review, automated regression tests
>
> **Key point**: Recurring bug = deeper problem. Don't just re-test, investigate root cause.

---

## III. TÌNH HUỐNG VỀ TEAMWORK & COMMUNICATION

### ❓ Tình huống 11: Developer "giận" vì bạn log quá nhiều bug. Bạn xử lý thế nào?

**✅ Trả lời:**
> 1. **Giữ professional**: Testing là để cải thiện chất lượng, KHÔNG phải tìm lỗi của cá nhân
> 2. **Communicate privately**: Nói chuyện 1-1, không công khai
> 3. **Giải thích mục đích**: "Tìm bug sớm = fix sớm = tiết kiệm chi phí cho team"
> 4. **Quality ≠ Person**: Bug là lỗi của CODE, không phải lỗi của CON NGƯỜI
> 5. **Đề xuất hợp tác**: "Mình có thể review together trước khi log?"
> 6. **Nếu vẫn conflict**: Escalate lên Lead
>
> **Key point**: Dev và Tester cùng một team, target chung là **deliver quality product**.

---

### ❓ Tình huống 12: Bạn được nhờ test một trang web nhưng KHÔNG có tài liệu requirement. Bạn làm gì?

**✅ Trả lời (Senior-level):**
> 1. **Exploratory Testing**: Test dựa trên kinh nghiệm và domain knowledge
> 2. **Tham khảo similar products**: So sánh với industry standard
> 3. **Checklist-based Testing**: Dùng generic testing checklists
> 4. **Focus vào**:
>    - UI/UX consistency
>    - All links/buttons work
>    - Form validations
>    - Cross-browser compatibility
>    - Error handling
>    - Security basics (SQL injection, XSS)
>    - Performance (page load time)
> 5. **Document findings** và tạo requirement từ observations
> 6. **Hỏi stakeholders** để xác nhận expected behavior
>
> **Key point**: Ad-hoc testing / Exploratory testing là kỹ năng quan trọng khi không có formal requirements.

---

### ❓ Tình huống 13: Sprint sắp kết thúc, Dev deliver feature muộn, bạn không có đủ thời gian test. Bạn xử lý thế nào?

**✅ Trả lời:**
> 1. **Raise concern** trong Daily Standup
> 2. **Negotiate** với SM/PO:
>    - Option A: Feature chuyển sang sprint sau
>    - Option B: Story không match DoD → Incomplete
>    - Option C: Quick smoke test, full test ở next sprint
> 3. **KHÔNG accept story** nếu chưa test đủ
> 4. **Document** trong Sprint Retrospective để improve
>
> **Key point**: Quality > Speed. Untested feature = potential production bug.

---

## IV. TÌNH HUỐNG THỰC TẾ TẠI FPT SOFTWARE

### ❓ Tình huống 14: Khách hàng Nhật yêu cầu test report rất chi tiết. Bạn chuẩn bị report thế nào?

**✅ Trả lời:**
> Khách hàng Nhật thường yêu cầu **evidence-based testing**:
> 1. **Screenshot cho TỪNG test step** (không chỉ result)
> 2. **Test case format chuẩn** (ID, steps, expected, actual, pass/fail)
> 3. **Highlight** phần thay đổi trên screenshot
> 4. **Summary table** với test coverage metrics
> 5. **Tuân thủ format** do khách hàng cung cấp
> 6. **Đúng deadline** - Nhật rất coi trọng punctuality
>
> **Key point**: "Hou-Ren-Sou" (報連相) - Report, Liên lạc, Tham vấn → Văn hóa làm việc Nhật.

---

### ❓ Tình huống 15: Bạn test 1 chức năng, pass tất cả test cases, nhưng khi demo cho khách hàng thì fail. Tại sao?

**✅ Trả lời (Senior-level):**
> **Possible reasons:**
> 1. **Environment difference**: Test env ≠ Demo env (config, data, permissions)
> 2. **Test data difference**: Data trong test env khác production-like data
> 3. **Test coverage gap**: Test cases chưa cover hết scenarios thực tế
> 4. **Timing issue**: Intermittent bug chưa được reproduce
> 5. **Missing edge cases**: Khách hàng dùng khác cách tester dùng
>
> **Lessons learned:**
> - Test trên environment giống production nhất
> - Dry-run trước khi demo
> - Include edge cases và negative testing
> - Exploratory testing bổ sung cho scripted testing

---

## V. CÂU HỎI VỀ BẢN THÂN VÀ CAREER

### ❓ Q: Tại sao bạn chọn nghề Tester?
**✅ Gợi ý trả lời:**
> Tôi đam mê công việc đảm bảo chất lượng phần mềm. Tester không chỉ tìm bug mà còn:
> - **Đại diện cho end-user** - bảo vệ trải nghiệm người dùng
> - **Tư duy phản biện** - luôn đặt câu hỏi "What if?"
> - **Đa dạng** - làm việc với nhiều domain, technology
> - **Impactful** - một bug tìm được sớm có thể tiết kiệm hàng triệu đồng

### ❓ Q: Tester giỏi cần những kỹ năng gì?
**✅ Trả lời:**
> 1. **Analytical Thinking**: Phân tích requirement, design test cases
> 2. **Attention to Detail**: Tỉ mỉ, không bỏ sót
> 3. **Communication**: Viết bug report rõ ràng, communicate với Dev
> 4. **Domain Knowledge**: Hiểu business logic
> 5. **Technical Skills**: SQL, API testing, basic coding, tool usage
> 6. **Curiosity**: Luôn muốn "break" phần mềm, tò mò
> 7. **Patience & Persistence**: Kiên nhẫn với repetitive tasks

---

