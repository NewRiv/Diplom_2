import allure
import pytest
from api.auth_api import AuthAPI
from test_data import valid_user, existing_user, invalid_user
from utils.assert_helpers import assert_response
from utils.helpers import generate_unique_email


@allure.feature("Authentication")
class TestAuth:
    @allure.story("Создание уникального пользователя")
    @allure.title("Регистрация нового уникального пользователя")
    def test_create_unique_user(self):
        auth_api = AuthAPI()
        email = generate_unique_email()
        response = auth_api.register(email, valid_user['password'], valid_user['name'])
        assert_response(response, 200)

    @allure.story("Создание пользователя, который уже зарегистрирован")
    @allure.title("Попытка регистрации уже существующего пользователя")
    def test_create_existing_user(self):
        auth_api = AuthAPI()
        response = auth_api.register(existing_user['email'], existing_user['password'], existing_user['name'])
        assert_response(response, 403, "User already exists")

    @allure.story("Создание пользователя без одного из обязательных полей")
    @allure.title("Регистрация пользователя с отсутствующим полем")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, missing_field):
        auth_api = AuthAPI()
        user_data = valid_user.copy()
        user_data.pop(missing_field)
        response = auth_api.register(**user_data)
        assert_response(response, 403, "Email, password and name are required fields")

    @allure.story("Логин под существующим пользователем")
    @allure.title("Успешный вход существующего пользователя")
    def test_login_existing_user(self):
        auth_api = AuthAPI()
        response = auth_api.login(existing_user['email'], existing_user['password'])
        assert_response(response, 200)

    @allure.story("Логин с неверным логином и паролем")
    @allure.title("Ошибка входа с неверными учетными данными")
    def test_login_invalid_user(self):
        auth_api = AuthAPI()
        response = auth_api.login(invalid_user['email'], invalid_user['password'])
        assert_response(response, 401, "email or password are incorrect")