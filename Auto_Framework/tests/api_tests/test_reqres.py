import pytest
import allure
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client(api_base_url):
    return APIClient(api_base_url)

@allure.feature("User API Tests")
@allure.story("Get User Details")
class TestUserAPI:

    @allure.title("Verify get single user HTTP 200")
    def test_get_single_user(self, api_client):
        response = api_client.get("/users/2")
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        assert data["id"] == 2
        assert data["name"] == "Ervin Howell"

    @allure.title("Verify user not found HTTP 404")
    def test_user_not_found(self, api_client):
        response = api_client.get("/users/23")
        assert response.status_code == 404, "Expected status code 404"
