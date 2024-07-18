import allure
import requests
from endpoints.base_api import BaseApi
from tests.data.url import base_url


class GetMemeById(BaseApi):
    @allure.step('Get meme by ID')
    def get_meme_by_id(self, token, meme_id):
        headers = {"Authorization": token}
        self.response = requests.get(
            url=f'{base_url}/meme/{meme_id}',
            headers=headers
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = {"error": self.response.text}
