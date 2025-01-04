import requests

from main import response
from utils.api_utils import ApiUtils


class AuthorizationHelper:
    MOVIES_CREATE_ENDPOINT = "/movies"
    POSTER_MOVIES_ENDPOINT = "/movies"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def post_create_movie(self, json) -> requests.Response:
        response = self.api_utils.post(self.MOVIES_CREATE_ENDPOINT, json=json)
        return response

    def get(self, json) -> requests.Response:
        response = self.api_utils.get(self.POSTER_MOVIES_ENDPOINT)
        return response
