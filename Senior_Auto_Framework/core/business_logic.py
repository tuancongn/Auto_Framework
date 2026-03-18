class MathLogic:
    @staticmethod
    def classify_triangle(a: float, b: float, c: float) -> str:
        """Phân loại tam giác dựa trên 3 cạnh"""
        if a <= 0 or b <= 0 or c <= 0:
            return "Invalid"
        if a + b <= c or a + c <= b or b + c <= a:
            return "Not a triangle"
        if a == b == c:
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isosceles"
        else:
            return "Scalene"

    @staticmethod
    def calculate_age(birth_year: int, current_year: int = 2026) -> str:
        """Tính tuổi từ năm sinh"""
        if birth_year < 1900 or birth_year > current_year:
            return "Invalid birth year"
        age = current_year - birth_year
        if age < 18:
            return "Underage"
        elif age <= 60:
            return "Working age"
        else:
            return "Retirement age"

class BusinessLogic:
    @staticmethod
    def calculate_electricity_bill(kwh: float) -> int:
        """Tính tiền điện dựa trên các bậc thang.
        Bậc 1 (0-50): 1806
        Bậc 2 (51-100): 1866
        Bậc 3 (101-200): 2167
        """
        if kwh < 0:
            return -1 # Invalid
        
        total = 0
        rates = [(50, 1806), (50, 1866), (100, 2167), (float('inf'), 2729)]
        remaining = kwh
        
        for limit, rate in rates:
            if remaining <= 0:
                break
            units = min(remaining, limit)
            total += units * rate
            remaining -= units
            
        return int(total)
