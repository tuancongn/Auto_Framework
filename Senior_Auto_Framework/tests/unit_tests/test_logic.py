import pytest
import allure
from core.business_logic import MathLogic, BusinessLogic

@allure.feature("FPT Fresher Logic Tests")
@allure.story("Tam giác - Equivalence Partitioning & Boundary Value Analysis")
class TestTriangleLogic:
    
    @allure.title("Kiểm tra các trường hợp bắt lỗi (Invalid)")
    @pytest.mark.parametrize("a, b, c, expected", [
        (0, 5, 5, "Invalid"),    # Boundary Error
        (-1, 5, 5, "Invalid"),   # EP Invalid
        (5, 0, 5, "Invalid"),
        (5, 5, 0, "Invalid")
    ])
    def test_invalid_triangle(self, a, b, c, expected):
        assert MathLogic.classify_triangle(a, b, c) == expected

    @allure.title("Kiểm tra không phải tam giác (tổng 2 cạnh <= cạnh còn lại)")
    @pytest.mark.parametrize("a, b, c, expected", [
        (1, 2, 5, "Not a triangle"),  # 1+2 < 5
        (5, 1, 2, "Not a triangle"),
        (2, 5, 1, "Not a triangle"),
        (2, 2, 4, "Not a triangle")   # 2+2 = 4 (Boundary of Not triangle)
    ])
    def test_not_a_triangle(self, a, b, c, expected):
        assert MathLogic.classify_triangle(a, b, c) == expected

    @allure.title("Kiểm tra các loại tam giác hợp lệ")
    @pytest.mark.parametrize("a, b, c, expected", [
        (5, 5, 5, "Equilateral"), # Đều
        (5, 5, 3, "Isosceles"),   # Cân (a=b)
        (3, 5, 5, "Isosceles"),   # Cân (b=c)
        (5, 3, 5, "Isosceles"),   # Cân (a=c)
        (3, 4, 5, "Scalene")      # Thường (Pythagoras)
    ])
    def test_valid_triangle(self, a, b, c, expected):
        assert MathLogic.classify_triangle(a, b, c) == expected

@allure.feature("FPT Fresher Logic Tests")
@allure.story("Tính tiền điện - BVA (Phân tích giá trị biên)")
class TestElectricityBill:

    @allure.title("Test các giá trị biên của hệ thống điện bậc thang")
    @pytest.mark.parametrize("kwh, expected_bill", [
        (-1, -1),                 # EP Invalid
        (0, 0),                   # BVA: Cạnh dưới cùng
        (50, 50 * 1806),          # BVA: Biên trên của Bậc 1
        (51, 50 * 1806 + 1 * 1866), # BVA: Biên dưới của Bậc 2
        (100, 50 * 1806 + 50 * 1866) # BVA: Biên trên của Bậc 2
    ])
    def test_electricity_boundaries(self, kwh, expected_bill):
        assert BusinessLogic.calculate_electricity_bill(kwh) == expected_bill
