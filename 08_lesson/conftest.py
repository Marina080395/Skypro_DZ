import pytest
import requests

BASE_URL = "https://yougile.ru/api/v2"
TOKEN = None  # токен задаётся динамически в ходе выполнения тестов


@pytest.fixture(scope="session")
def auth_header():
    global TOKEN
    if not TOKEN:
        response = requests.post(BASE_URL + "/auth/login",
        json={"email": "example@example.com", "password": "your_password"})
        TOKEN = response.json().get("token")
    return {"Authorization": f"Bearer {TOKEN}"}
