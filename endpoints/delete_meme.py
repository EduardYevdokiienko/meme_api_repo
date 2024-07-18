import allure
import requests
from endpoints.base_api import BaseApi
from tests.data.url import base_url


class DeleteMeme(BaseApi):
    @allure.step('Delete meme by id')
    def delete_meme_with_id(self, token, meme_id):
        headers = {"Authorization": token}
        self.response = requests.delete(
            url=f'{base_url}/meme/{meme_id}',
            headers=headers
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = {"error": self.response.text}
