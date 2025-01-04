import json

import curlify
import requests
from requests import Session

from utils.json_utils import JsonUtils
from logger.logger import Logger


def log_response(func):
    def _log_response(*args, **kwargs) -> requests.Response:
        response = func(*args, **kwargs)
        Logger.info(f"Request: {curlify.to_curl(response.request)}")
        body = json.dumps(response.json(), indent=2) if JsonUtils.is_json(response.text) else response.text
        Logger.info(f"Response status_code='{response.status_code}', elapsed_time='{response.elapsed}'\n\n{body}\n")
        return response

    return _log_response


class ApiUtils:
    def __init__(self, url, headers=None):
        if headers is None:
            headers = {}
        self.session = Session()
        self.session.headers.update(headers)
        self.url = url

    @log_response
    def update_headers(self, headers) -> None:
        self.session.headers.update(headers)

    @log_response
    def get(self, url_endpoints, **kwargs) -> requests.Response:
        response = self.session.get(self.url + url_endpoints, **kwargs)
        return response

    @log_response
    def post(self, url_endpoints, data=None, json=None, **kwargs) -> requests.Response:
        response = self.session.post(self.url + url_endpoints, data, json, **kwargs)
        return response

    @log_response
    def put(self, url_endpoints, data=None, **kwargs) -> requests.Response:
        response = self.session.put(self.url + url_endpoints, data, **kwargs)
        return response

    @log_response
    def patch(self, url_endpoints, data=None, **kwargs) -> requests.Response:
        response = self.session.patch(self.url + url_endpoints, data, **kwargs)
        return response

    @log_response
    def delete(self, url_endpoints, **kwargs) -> requests.Response:
        response = self.session.get(self.url + url_endpoints, **kwargs)
        return response
