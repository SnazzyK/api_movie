import os

import pytest

from services.auth.auth_service import AuthService
from services.auth.model.login import Login
from utils.api_utils import ApiUtils

AUTH_URL = "https://auth.dev-cinescope.store"
MOVIE_URL = "https://api.dev-cinescope.store"


@pytest.fixture(scope="session", autouse=False)
def api_utils_anonym_auth():
    api_utils_anonym = ApiUtils(url=AUTH_URL)
    yield api_utils_anonym


@pytest.fixture(scope="session", autouse=False)
def auth(api_utils_anonym_auth):
    auth_service = AuthService(api_utils=api_utils_anonym_auth)
    yield auth_service

@pytest.fixture(scope="session", autouse=False)
def api_utils_super_admin_movie(api_utils_anonym_auth):
    email = "test-admin@mail.com"
    password = "KcLMmxkJMjBD1"

    auth_service = AuthService(api_utils=api_utils_anonym_auth)
    login_user = Login(email=email, password=password)
    login_response = auth_service.login_user(login_user)

    api_utils_super_admin = ApiUtils(url=AUTH_URL,
                                     headers={"Authorization": f"Bearer {login_response.access_token}"})
    yield api_utils_super_admin

@pytest.fixture(scope="session", autouse=False)
def movie_service_super_admin(api_utils_super_admin_movie):
    auth_new = AuthService(api_utils=api_utils_super_admin_movie)
    yield auth_new