import requests
import allure

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    @allure.step("GET request to {endpoint}")
    def get(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, **kwargs)
        allure.attach(f"URL: {url}\nResponse Code: {response.status_code}\nResponse Body: {response.text}", 
                      name="Response Details", attachment_type=allure.attachment_type.TEXT)
        return response

    @allure.step("POST request to {endpoint}")
    def post(self, endpoint, data=None, json=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data, json=json, **kwargs)
        allure.attach(f"URL: {url}\nPayload: {json}\nResponse Code: {response.status_code}\nResponse Body: {response.text}", 
                      name="Response Details", attachment_type=allure.attachment_type.TEXT)
        return response
