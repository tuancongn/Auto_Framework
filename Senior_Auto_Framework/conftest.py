import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import allure
import os

@pytest.fixture(scope="session")
def api_base_url():
    # Sử dụng JSONPlaceholder thay cho Reqres.in để tránh bị Cloudflare chặn lỗi 403
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="function")
def driver(request):
    """Khởi tạo Chrome webdriver cho mỗi test script và thêm hook chụp ảnh khi lỗi."""
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Đã comment lại để cho phép Tự động bật Browser biểu diễn cho Nhà tuyển dụng xem
    options.add_argument('--window-size=1920,1080')
    
    # Sử dụng Driver Manager (chuẩn Senior/Modern Setup)
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    
    yield driver
    
    # Sau khi test xong, kiểm tra xem test có lỗi (fail) hay không
    if request.node.rep_call.failed:
        # Nếu fail, chụp ảnh màn hình đính kèm vào Allure Report
        allure.attach(driver.get_screenshot_as_png(),
                      name=request.node.name,
                      attachment_type=allure.attachment_type.PNG)
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook của Pytest để lấy trạng thái pass/fail của test function"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
