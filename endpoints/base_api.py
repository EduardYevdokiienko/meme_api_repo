import allure
import requests
from pydantic import BaseModel
from endpoints.schemas import TokenGetResponse, ResponseSchema, ResponseSchemaFull


class BaseApi:
    response: requests.Response
    response_json: dict
    token: str
    headers: dict
    meme_id: str
    updated_by: str
    error: str
    token_valid_response: TokenGetResponse
    valid_response: ResponseSchema
    response_data: ResponseSchemaFull

    @allure.step('Check status code')
    def check_status_code_is_(self, code):
        return self.response.status_code == code

    @allure.step('Check response text')
    def check_response_text_is_(self, text):
        return self.response_json['text'] == text

    @allure.step('Check response url')
    def check_response_url_is_(self, url):
        return self.response_json['url'] == url

    @allure.step('Check response value')
    def check_response_value_is_(self, value):
        return self.response_json['id'] == value
