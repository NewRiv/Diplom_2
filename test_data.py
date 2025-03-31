BASE_URL = "https://stellarburgers.nomoreparties.site"
ingredients_url = f"{BASE_URL}/api/ingredients"
register_url = f"{BASE_URL}/api/auth/register"
login_url = f"{BASE_URL}/api/auth/login"
logout_url = f"{BASE_URL}/api/auth/logout"
refresh_token_url = f"{BASE_URL}/api/auth/token"
user_url = f"{BASE_URL}/api/auth/user"
order_url = f"{BASE_URL}/api/orders"

valid_user = {
    "email": "test-user@example.com",
    "password": "testpassword",
    "name": "Test User"
}

existing_user = {
    "email": "existing-user@example.com",
    "password": "existingpassword",
    "name": "Existing User"
}

invalid_user = {
    "email": "invalid-user@example.com",
    "password": "invalidpassword"
}

updated_user = {
    "email": "updated_user_@example.com",
    "password": "newpassword123",
    "name": "UpdatedUser"
}