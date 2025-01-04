from http.client import responses

import requests
from utils.api_utils import ApiUtils


class AuthorizationHelper:
    REGISTER_ENDPOINT = "/register"
    LOGIN_ENDPOINT = "/login"
    LOGOUT_ENDPOINT = "/logout"
    CONFIRM_ENDPOINT = "/confirm"
    INFO_ENDPOINT = "/USER/"


    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def post_register(self, json) -> requests.Response:
        response = self.api_utils.post(self.REGISTER_ENDPOINT, json=json)
        return response

    def post_login(self, json) -> requests.Response:
        response = self.api_utils.post(self.LOGIN_ENDPOINT, json=json)
        return response


    def get_logout(self) -> requests.Response:
        response = self.api_utils.get(self.LOGOUT_ENDPOINT)
        return response

    def get_confirm(self) -> requests.Response:
        response = self.api_utils.get(self.CONFIRM_ENDPOINT)
        return response

    def get_info(self,id_or_email_user:str) -> requests.Response:
        response = self.api_utils.get(self.INFO_ENDPOINT + id_or_email_user)
        return response