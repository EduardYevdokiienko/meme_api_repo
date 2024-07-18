import allure
import requests
from endpoints.base_api import BaseApi
from tests.data.url import base_url


class GetAuthorizeToken(BaseApi):
    @allure.step('Token check')
    def get_authorize_token(self, token):
        headers = {"Authorization": token}
        self.response = requests.get(
            url=f'{base_url}/authorize/{token}',
            headers=headers
        )
        try:
            self.response_json = self.response.json()
            self.token = self.response_json['token']
            return token
        except ValueError:
            self.response_json = {"error": self.response.text}
