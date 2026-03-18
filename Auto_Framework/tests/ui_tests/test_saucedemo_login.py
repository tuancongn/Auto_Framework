import pytest
import allure
import json
import os
from pages.login_page import LoginPage

# Đọc Data-Driven Testing (DDT) từ file JSON
def get_test_data():
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    with open(os.path.join(base_path, 'data', 'test_data.json')) as f:
        return json.load(f)

test_data = get_test_data()

@allure.feature("Web UI Tests")
@allure.story("SauceDemo Login Form")
class TestLogin:

    @allure.title("Verify successful login with standard user")
    @pytest.mark.ui
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        
        user = test_data["valid_login"]
        login_page.login(user["username"], user["password"])
        
        # Verify URL sau khi login thành công
        assert "inventory.html" in driver.current_url, "Login failed, not redirect to inventory page"

    @allure.title("Verify login failures with invalid credentials")
    @pytest.mark.ui
    @pytest.mark.parametrize("invalid_user", test_data["invalid_login"])
    def test_invalid_login(self, driver, invalid_user):
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.login(invalid_user["username"], invalid_user["password"])
        
        actual_error = login_page.get_error_message()
        assert actual_error == invalid_user["expected_error"], f"Expected error '{invalid_user['expected_error']}' but got '{actual_error}'"
