import allure
import requests
from endpoints.base_api import BaseApi
from tests.data.url import base_url


class GetMeme(BaseApi):
    @allure.step('Get all memes')
    def get_all_memes(self, token):
        headers = {"Authorization": token}
        self.response = requests.get(
            url=f'{base_url}/meme',
            headers=headers
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = {"error": self.response.text}
