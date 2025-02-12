import requests
from faker import Faker

from services.auth.auth_service import AuthService
from services.auth.helper.authorization_helper import AuthorizationHelper
from services.auth.model.login import Login
from services.auth.model.register import RegisterResponse, RegisterRequests
from utils.api_utils import ApiUtils

fake = Faker()
EMAIL_USER = fake.email()
PASSWORD_USER = "123VaKaNa21!@1"

EMAIL_ADMIN = "test-admin@mail.com"
PASSWORD_ADMIN = "KcLMmxkJMjBD1"


class TestCreateUser:
    def test_create_user(self, api_utils_anonym_auth):
        auth_helper = AuthorizationHelper(api_utils=api_utils_anonym_auth)
        response = auth_helper.post_register({"email": fake.email(),
                                              "fullName": f"{fake.first_name()} {fake.last_name()}",
                                              "password": PASSWORD_USER,
                                              "passwordRepeat": PASSWORD_USER})

        assert response.status_code == response.status_code, \
            (f"Wrong status code. Actual: '{response.status_code}',"
             f" but expected: '{requests.status_codes.codes.unauthorized}'")


class TestCreateUser2:

    def test_create_user(self, auth,movie_service_super_admin):
        auth_helper = AuthorizationHelper(api_utils=auth)


        user_data = RegisterRequests(email=EMAIL_USER,
                                     full_name=f"{fake.first_name()} {fake.last_name()}",
                                     password=PASSWORD_USER,
                                     password_repeat=PASSWORD_USER)

        create_user = auth.register_user(user_data)



        login_user_data = Login(email=EMAIL_USER,
                                password=PASSWORD_USER)
        login_user = auth.login_user(login_user_data)

        get_info = movie_service_super_admin.get_info_user(EMAIL_USER)

        assert get_info.status_code == get_info.status_code, \
        (f"Wrong status code. Actual: '{get_info.status_code}',"
         f" but expected: '{requests.status_codes.codes.unauthorized}'")





class TestGetInfoUser:
    def test_get_info(self, movie_service_super_admin):

        # login_user_data = Login(email=EMAIL_ADMIN,
        #                         password=PASSWORD_ADMIN)
        # login_user = movie_service_super_admin.login_user(login_user_data)
        get_info = movie_service_super_admin.get_info_user(EMAIL_USER)



        assert get_info.status_code == get_info.status_code, \
            (f"Wrong status code. Actual: '{get_info.status_code}',"
             f" but expected: '{requests.status_codes.codes.unauthorized}'")
