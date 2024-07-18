import allure
import requests
from endpoints.base_api import BaseApi
from tests.data.url import base_url


class PostMeme(BaseApi):
    @allure.step('Post a meme')
    def post_meme(self, token, payload):
        headers = {"Authorization": token}
        self.response = requests.post(
            url=f'{base_url}/meme',
            json=payload,
            headers=headers
        )
        try:
            self.response_json = self.response.json()
            meme_id = self.response_json['id']
            updated_by = self.response_json['updated_by']
            return meme_id, updated_by
        except ValueError:
            self.response_json = {"error": self.response.text}
