import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        time.sleep(0.5) # Để chậm lại để nhìn thấy click
        element.click()

    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        time.sleep(0.5) # Chậm lại để nhìn thấy gõ phím
        for char in text:
            element.send_keys(char)
            time.sleep(0.1) # Gõ từng chữ cho giống human thật
        time.sleep(0.5)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_element_visible(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
