import pytest
from api.auth_api import AuthAPI
from test_data import valid_user, ingredients_url
import requests
import random

@pytest.fixture(scope="function")
def register_user():
    auth_api = AuthAPI()
    user_data = valid_user.copy()
    email = f"test-{random.randint(0, 10000)}@example.com"
    response = auth_api.register(email, user_data['password'], user_data['name'])
    token = response.json().get('accessToken')
    yield {"email": email, "accessToken": token}
    auth_api.delete_user(token)     # Удаление пользователя после теста


@pytest.fixture(scope="session")
def ingredients():
    """Фикстура запрашивает ингредиенты один раз перед всеми тестами"""
    response = requests.get(ingredients_url)
    assert response.status_code == 200, "Не удалось получить ингредиенты"
    return response.json()['data']
