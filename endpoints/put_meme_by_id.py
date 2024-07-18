import allure
import requests
from endpoints.base_api import BaseApi
from tests.data.url import base_url


class PutMeme(BaseApi):
    @allure.step('Change meme information')
    def change_meme_by_id(self, token, payload, meme_id):
        headers = {"Authorization": token}
        self.response = requests.put(
            url=f'{base_url}/meme/{meme_id}',
            json=payload,
            headers=headers
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = {"error": self.response.text}
