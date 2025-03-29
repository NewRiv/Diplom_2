import requests
from test_data import register_url, login_url, logout_url, refresh_token_url, user_url


class AuthAPI:
    def __init__(self):
        self.timeout = 10

    def register(self, email=None, password=None, name=None):
        data = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(register_url, json=data)
        return response

    def login(self, email, password):
        data = {"email": email, "password": password}
        return requests.post(login_url, json=data)

    def logout(self, refresh_token):
        data = {"token": refresh_token}
        return requests.post(logout_url, json=data)

    def refresh_token(self, refresh_token):
        data = {"token": refresh_token}
        return requests.post(refresh_token_url, json=data)

    def delete_user(self, token):
        headers = {"Authorization": token}
        response = requests.delete(user_url, headers=headers)
        return response
