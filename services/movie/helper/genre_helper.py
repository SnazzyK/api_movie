from utils.api_utils import ApiUtils


class GenreHelper:
    GENRES_ENDPOINT = "/genres"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def post_genre(self, json):
        response = self.api_utils.post(self.GENRES_ENDPOINT, json=json)
        return response
