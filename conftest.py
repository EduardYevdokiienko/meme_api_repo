import pytest
from endpoints.post_authorize import PostAuthorize
from endpoints.get_authorize_token import GetAuthorizeToken
from endpoints.get_meme import GetMeme
from endpoints.get_meme_by_id import GetMemeById
from endpoints.post_meme import PostMeme
from endpoints.put_meme_by_id import PutMeme
from endpoints.delete_meme import DeleteMeme
from tests.data import payloads


@pytest.fixture(scope='session')
def auth_token(get_authorize_token_endpoint, post_authorize_endpoint):
    post_authorize_endpoint.post_authorize(payloads.authorize_payload)
    token = post_authorize_endpoint.response_json['token']
    return token


@pytest.fixture(scope='session')
def post_authorize_endpoint():
    return PostAuthorize()


@pytest.fixture(scope='session')
def get_authorize_token_endpoint():
    return GetAuthorizeToken()


@pytest.fixture()
def get_meme_endpoint():
    return GetMeme()


@pytest.fixture()
def get_meme_by_id_endpoint():
    return GetMemeById()


@pytest.fixture()
def post_meme_endpoint():
    return PostMeme()


@pytest.fixture()
def put_meme_by_id_endpoint():
    return PutMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()
