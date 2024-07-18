import allure
import requests
from endpoints.base_api import BaseApi
from tests.data.url import base_url


class PostAuthorize(BaseApi):
    @allure.step('Authorization')
    @allure.step('Token generation')
    def post_authorize(self, payload):
        self.response = requests.post(
            url=f'{base_url}/authorize',
            json=payload
        )
        try:
            self.response_json = self.response.json()
            token = self.response_json['token']
            return token
        except ValueError:
            self.response_json = {"error": self.response.text}
