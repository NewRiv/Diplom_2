import allure
from api.user_api import UserAPI
from utils.assert_helpers import assert_response
from test_data import updated_user


@allure.feature("User Data")
class TestUser:
    @allure.story("Изменение данных пользователя с авторизацией")
    @allure.title("Успешное изменение данных авторизованного пользователя")
    def test_update_user_with_auth(self, register_user):
        user_api = UserAPI()
        token = register_user['accessToken']
        response = user_api.update_user(token, updated_user)
        assert_response(response, 200)

    @allure.story("Изменение данных пользователя без авторизации")
    @allure.title("Ошибка при изменении данных без авторизации")
    def test_update_user_without_auth(self):
        user_api = UserAPI()
        response = user_api.update_user(None, updated_user)
        assert_response(response, 401, "You should be authorised")
