import requests

from services.auth.helper.authorization_helper import AuthorizationHelper
from services.auth.model.login import Login
from services.auth.model.register import RegisterRequests, RegisterResponse, LoginResponse

from utils.api_utils import ApiUtils


class AuthService:
    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils
        self.authorization_helper = AuthorizationHelper(self.api_utils)

    def register_user(self, register_user: RegisterRequests):
        response = self.authorization_helper.post_register(register_user.model_dump(by_alias=True,
                                                                                    exclude_defaults=True))
        return RegisterResponse(**response.json())

    def login_user(self, login_user: Login):
        response = self.authorization_helper.post_login(login_user.model_dump(by_alias=True,
                                                                              exclude_defaults=True))
        return LoginResponse(**response.json())


    def get_info_user(self,id_or_email_user:str) -> requests.Response:
        response = self.authorization_helper.get_info(id_or_email_user)
        return response




