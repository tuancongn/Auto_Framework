# 📘 TỰ LUẬN CODE - BASIC PROGRAMMING

---

## I. CƠ BẢN LẬP TRÌNH (Pseudocode / Python / Java / JavaScript)

### 1. Biến và Kiểu dữ liệu

```python
# Python
name = "FPT Software"      # String
age = 25                    # Integer
salary = 15000000.0         # Float
is_tester = True            # Boolean
```

```java
// Java
String name = "FPT Software";
int age = 25;
double salary = 15000000.0;
boolean isTester = true;
```

```javascript
// JavaScript
let name = "FPT Software";
let age = 25;
let salary = 15000000.0;
let isTester = true;
```

### 2. If-Else (Điều kiện)

```python
# Cấu trúc cơ bản
if condition:
    # do something
elif another_condition:
    # do something else
else:
    # default action
```

```java
// Java
if (condition) {
    // do something
} else if (anotherCondition) {
    // do something else
} else {
    // default action
}
```

### 3. Vòng lặp (Loops)

```python
# For loop
for i in range(1, 11):  # 1 đến 10
    print(i)

# While loop
count = 0
while count < 10:
    print(count)
    count += 1
```

---

## II. BÀI TẬP THƯỜNG GẶP VÀ LỜI GIẢI

### ⭐ Bài 1: Kiểm tra số chẵn / lẻ

```python
def check_even_odd(n):
    if n % 2 == 0:
        print(f"{n} là số CHẴN")
    else:
        print(f"{n} là số LẺ")

# Test
check_even_odd(4)   # Output: 4 là số CHẴN
check_even_odd(7)   # Output: 7 là số LẺ
```

```java
// Java
public static void checkEvenOdd(int n) {
    if (n % 2 == 0) {
        System.out.println(n + " là số CHẴN");
    } else {
        System.out.println(n + " là số LẺ");
    }
}
```

---

### ⭐ Bài 2: Kiểm tra số dương / âm / zero

```python
def check_number(n):
    if n > 0:
        print(f"{n} là số DƯƠNG")
    elif n < 0:
        print(f"{n} là số ÂM")
    else:
        print("Số KHÔNG (zero)")

# Test
check_number(5)    # 5 là số DƯƠNG
check_number(-3)   # -3 là số ÂM
check_number(0)    # Số KHÔNG (zero)
```

---

### ⭐ Bài 3: Tìm số lớn nhất trong 3 số

```python
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Test
print(find_max(10, 25, 15))  # Output: 25
```

```java
// Java
public static int findMax(int a, int b, int c) {
    if (a >= b && a >= c) return a;
    else if (b >= a && b >= c) return b;
    else return c;
}
```

---

### ⭐ Bài 4: Tính điểm xếp loại sinh viên

```python
def grade_student(score):
    if score < 0 or score > 10:
        print("Điểm không hợp lệ!")
    elif score >= 9:
        print("Xuất sắc")
    elif score >= 8:
        print("Giỏi")
    elif score >= 7:
        print("Khá")
    elif score >= 5:
        print("Trung bình")
    else:
        print("Yếu")

# Test
grade_student(9.5)   # Xuất sắc
grade_student(7.0)   # Khá
grade_student(3.0)   # Yếu
grade_student(11)    # Điểm không hợp lệ!
```

---

### ⭐ Bài 5: Kiểm tra năm nhuận

```python
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} là năm nhuận")
    else:
        print(f"{year} KHÔNG phải năm nhuận")

# Test
is_leap_year(2024)  # Năm nhuận
is_leap_year(2023)  # KHÔNG phải
is_leap_year(1900)  # KHÔNG phải (chia hết 100 nhưng không chia hết 400)
is_leap_year(2000)  # Năm nhuận (chia hết 400)
```

---

### ⭐ Bài 6: FizzBuzz (Bài kinh điển)

```python
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Test: fizzbuzz(15)
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
```

---

### ⭐ Bài 7: Tính giai thừa (Factorial)

```python
def factorial(n):
    if n < 0:
        return "Không hợp lệ"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test
print(factorial(5))   # 120 (5! = 5×4×3×2×1)
print(factorial(0))   # 1
```

---

### ⭐ Bài 8: Tính tổng các số từ 1 đến N

```python
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Hoặc dùng công thức: n * (n + 1) / 2
def sum_to_n_formula(n):
    return n * (n + 1) // 2

# Test
print(sum_to_n(10))   # 55
print(sum_to_n(100))  # 5050
```

---

### ⭐ Bài 9: Đếm số chẵn / lẻ trong mảng

```python
def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"Số chẵn: {even_count}, Số lẻ: {odd_count}")

# Test
count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Output: Số chẵn: 5, Số lẻ: 5
```

---

### ⭐ Bài 10: Kiểm tra số nguyên tố

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(7))    # True
print(is_prime(10))   # False
print(is_prime(1))    # False
print(is_prime(2))    # True
```

---

### ⭐ Bài 11: Đảo ngược chuỗi

```python
def reverse_string(s):
    return s[::-1]

# Hoặc dùng vòng lặp:
def reverse_string_loop(s):
    result = ""
    for char in s:
        result = char + result
    return result

# Test
print(reverse_string("FPT Software"))  # "erawtfoS TPF"
```

---

### ⭐ Bài 12: Kiểm tra Palindrome (chuỗi đối xứng)

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Test
print(is_palindrome("madam"))     # True
print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
```

---

### ⭐ Bài 13: Fibonacci

```python
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# Test
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

### ⭐ Bài 14: Tính tiền taxi (If-Else thực tế)

```python
def calculate_taxi_fare(km):
    """
    Bảng giá:
    - 0.5 km đầu: 14,000 VND (giá mở cửa)
    - Từ km 0.5 đến km 30: 14,500 VND/km
    - Trên 30 km: 12,000 VND/km
    """
    if km <= 0:
        return "Khoảng cách không hợp lệ"
    
    fare = 14000  # Giá mở cửa (0.5 km đầu)
    
    if km <= 0.5:
        return fare
    elif km <= 30:
        fare += (km - 0.5) * 14500
    else:
        fare += 29.5 * 14500  # Từ 0.5 đến 30
        fare += (km - 30) * 12000  # Trên 30 km
    
    return int(fare)

# Test
print(calculate_taxi_fare(0.3))   # 14,000
print(calculate_taxi_fare(10))    # 14,000 + 9.5 * 14,500 = 151,750
print(calculate_taxi_fare(50))    # 14,000 + 29.5*14,500 + 20*12,000 = 681,750
```

---

### ⭐ Bài 15: Tính tiền điện (If-Else thực tế)

```python
def calculate_electricity_bill(kwh):
    """
    Bảng giá điện bậc thang:
    - Bậc 1 (0-50 kWh):   1,806 VND/kWh
    - Bậc 2 (51-100 kWh):  1,866 VND/kWh
    - Bậc 3 (101-200 kWh): 2,167 VND/kWh
    - Bậc 4 (201-300 kWh): 2,729 VND/kWh
    - Bậc 5 (301-400 kWh): 3,050 VND/kWh
    - Bậc 6 (>400 kWh):    3,151 VND/kWh
    """
    if kwh <= 0:
        return 0
    
    total = 0
    rates = [
        (50, 1806),
        (50, 1866),
        (100, 2167),
        (100, 2729),
        (100, 3050),
        (float('inf'), 3151)
    ]
    
    remaining = kwh
    for limit, rate in rates:
        if remaining <= 0:
            break
        units = min(remaining, limit)
        total += units * rate
        remaining -= units
    
    return int(total)

# Test
print(f"50 kWh: {calculate_electricity_bill(50):,} VND")    # 90,300
print(f"150 kWh: {calculate_electricity_bill(150):,} VND")  # 291,950
print(f"300 kWh: {calculate_electricity_bill(300):,} VND")  # 706,150
```

---

### ⭐ Bài 16: Máy tính đơn giản (Calculator)

```python
def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Lỗi: Không thể chia cho 0!"
        return num1 / num2
    else:
        return "Lỗi: Toán tử không hợp lệ!"

# Test
print(calculator(10, '+', 5))   # 15
print(calculator(10, '-', 3))   # 7
print(calculator(10, '*', 4))   # 40
print(calculator(10, '/', 3))   # 3.333...
print(calculator(10, '/', 0))   # Lỗi: Không thể chia cho 0!
```

---

### ⭐ Bài 17: Sắp xếp mảng (Bubble Sort)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
# Output: [11, 12, 22, 25, 34, 64, 90]
```

---

### ⭐ Bài 18: Tìm phần tử xuất hiện nhiều nhất

```python
def find_most_frequent(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    max_count = 0
    max_num = arr[0]
    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            max_num = num
    
    return max_num, max_count

# Test
arr = [1, 3, 2, 1, 4, 1, 3, 2, 1]
num, count = find_most_frequent(arr)
print(f"Phần tử {num} xuất hiện nhiều nhất: {count} lần")
# Output: Phần tử 1 xuất hiện nhiều nhất: 4 lần
```

---

### ⭐ Bài 19: Validate Email (đơn giản)

```python
def validate_email(email):
    # Kiểm tra cơ bản
    if '@' not in email:
        return False, "Thiếu ký tự @"
    
    parts = email.split('@')
    if len(parts) != 2:
        return False, "Chỉ được 1 ký tự @"
    
    local, domain = parts
    if len(local) == 0:
        return False, "Phần trước @ trống"
    
    if '.' not in domain:
        return False, "Domain thiếu dấu chấm"
    
    if domain.startswith('.') or domain.endswith('.'):
        return False, "Domain không hợp lệ"
    
    return True, "Email hợp lệ"

# Test
print(validate_email("test@gmail.com"))    # (True, 'Email hợp lệ')
print(validate_email("testgmail.com"))     # (False, 'Thiếu ký tự @')
print(validate_email("@gmail.com"))        # (False, 'Phần trước @ trống')
print(validate_email("test@gmail"))        # (False, 'Domain thiếu dấu chấm')
```

---

### ⭐ Bài 20: Validate Password

```python
def validate_password(password):
    errors = []
    
    if len(password) < 8:
        errors.append("Mật khẩu phải ít nhất 8 ký tự")
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()_+-="
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    
    if not has_upper:
        errors.append("Cần ít nhất 1 chữ HOA")
    if not has_lower:
        errors.append("Cần ít nhất 1 chữ thường")
    if not has_digit:
        errors.append("Cần ít nhất 1 chữ số")
    if not has_special:
        errors.append("Cần ít nhất 1 ký tự đặc biệt")
    
    if errors:
        return False, errors
    return True, ["Mật khẩu hợp lệ!"]

# Test
print(validate_password("Abc@1234"))     # (True, ['Mật khẩu hợp lệ!'])
print(validate_password("abc"))          # (False, ['Mật khẩu phải ít nhất 8 ký tự', ...])
print(validate_password("abcdefgh"))     # (False, ['Cần ít nhất 1 chữ HOA', ...])
```

---

## III. DẠNG BÀI LIÊN QUAN ĐẾN TESTING

### ⭐ Bài 21: Viết hàm kiểm tra tam giác

```python
def classify_triangle(a, b, c):
    """
    Phân loại tam giác dựa trên 3 cạnh.
    Đây là bài test phổ biến cho Tester vì liên quan đến Equivalence Partitioning.
    """
    # Kiểm tra input hợp lệ
    if a <= 0 or b <= 0 or c <= 0:
        return "Không hợp lệ: cạnh phải > 0"
    
    # Kiểm tra có phải tam giác không
    if a + b <= c or a + c <= b or b + c <= a:
        return "Không phải tam giác"
    
    # Phân loại
    if a == b == c:
        return "Tam giác ĐỀU"
    elif a == b or b == c or a == c:
        return "Tam giác CÂN"
    else:
        return "Tam giác THƯỜNG"

# Test
print(classify_triangle(3, 3, 3))    # Tam giác ĐỀU
print(classify_triangle(3, 3, 5))    # Tam giác CÂN
print(classify_triangle(3, 4, 5))    # Tam giác THƯỜNG
print(classify_triangle(1, 2, 10))   # Không phải tam giác
print(classify_triangle(-1, 2, 3))   # Không hợp lệ
```

---

### ⭐ Bài 22: Tính tuổi từ năm sinh

```python
def calculate_age(birth_year):
    current_year = 2026
    
    if birth_year < 1900 or birth_year > current_year:
        return "Năm sinh không hợp lệ"
    
    age = current_year - birth_year
    
    if age < 18:
        category = "Chưa đủ tuổi"
    elif age <= 60:
        category = "Trong độ tuổi lao động"
    else:
        category = "Trên tuổi lao động"
    
    return f"Tuổi: {age} - {category}"

# Test
print(calculate_age(2000))   # Tuổi: 26 - Trong độ tuổi lao động
print(calculate_age(2010))   # Tuổi: 16 - Chưa đủ tuổi
print(calculate_age(1960))   # Tuổi: 66 - Trên tuổi lao động
```

---

### ⭐ Bài 23: Đếm ký tự trong chuỗi

```python
def count_characters(text):
    uppercase = 0
    lowercase = 0
    digits = 0
    spaces = 0
    special = 0
    
    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            digits += 1
        elif char == ' ':
            spaces += 1
        else:
            special += 1
    
    print(f"Chữ hoa: {uppercase}")
    print(f"Chữ thường: {lowercase}")
    print(f"Chữ số: {digits}")
    print(f"Khoảng trắng: {spaces}")
    print(f"Ký tự đặc biệt: {special}")

# Test
count_characters("Hello World 2026!")
# Chữ hoa: 2 (H, W)
# Chữ thường: 8
# Chữ số: 4
# Khoảng trắng: 2
# Ký tự đặc biệt: 1 (!)
```

---

