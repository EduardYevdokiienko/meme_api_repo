import pytest
import allure
from tests.data import payloads


@allure.feature('Authorization')
def test_authorize(auth_token):
    assert auth_token is not None


@allure.feature('Post meme')
@allure.story('Create meme')
@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.parametrize("payload, expected_status", [
    (payloads.new_meme_empty_payload, 200),
    (payloads.payload_with_info, 200),
    (payloads.payload_invalid, 400),
])
def test_create_meme(auth_token, post_meme_endpoint, payload, expected_status):
    post_meme_endpoint.post_meme(auth_token, payload)
    assert post_meme_endpoint.check_status_code_is_(expected_status)


@allure.feature('Get all memes')
@allure.story('Get list of memes')
@pytest.mark.regression
@pytest.mark.positive
def test_get_all_memes(auth_token, get_meme_endpoint):
    get_meme_endpoint.get_all_memes(auth_token)
    assert get_meme_endpoint.check_status_code_is_(200)


@allure.feature('Get meme by ID')
@allure.story('Get a meme')
@pytest.mark.regression
@pytest.mark.positive
def test_get_meme_by_id(auth_token, new_meme, get_meme_by_id_endpoint):
    get_meme_by_id_endpoint.get_meme_by_id(auth_token, new_meme)
    assert get_meme_by_id_endpoint.check_status_code_is_(200)


@allure.feature('Get meme by ID')
@allure.story('Get a meme')
@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.parametrize("meme_id, expected_status", [
    ("invalid_id", 404),
    ("", 404),
])
def test_get_meme_by_invalid_id_parametrize(auth_token, get_meme_by_id_endpoint, meme_id, expected_status):
    get_meme_by_id_endpoint.get_meme_by_id(auth_token, meme_id)
    assert get_meme_by_id_endpoint.check_status_code_is_(expected_status)


@allure.feature('Get meme by ID')
@allure.story('Get a meme')
@pytest.mark.regression
@pytest.mark.negative
def test_get_meme_by_invalid_id(auth_token, get_meme_by_id_endpoint):
    inv_id = 'aaa'
    get_meme_by_id_endpoint.get_meme_by_id(auth_token, inv_id)
    assert get_meme_by_id_endpoint.check_status_code_is_(404)


@allure.feature('Get meme by ID')
@allure.story('Get a meme')
@pytest.mark.regression
@pytest.mark.negative
def test_get_meme_by_empty_id(auth_token, get_meme_by_id_endpoint):
    emp_id = ''
    get_meme_by_id_endpoint.get_meme_by_id(auth_token, emp_id)
    assert get_meme_by_id_endpoint.check_status_code_is_(404)


@allure.feature('Update meme by ID')
@allure.story('change a meme info')
@pytest.mark.regression
@pytest.mark.positive
def test_update_meme_by_id(auth_token, new_meme, put_meme_by_id_endpoint):
    payload = payloads.payload_with_info
    payload['id'] = new_meme
    put_meme_by_id_endpoint.change_meme_by_id(auth_token, new_meme, payload)
    assert put_meme_by_id_endpoint.check_status_code_is_(200)


@allure.feature('Update meme by ID')
@allure.story('Change a meme info with invalid id')
@pytest.mark.regression
@pytest.mark.negative
def test_update_meme_invalid_id(auth_token, put_meme_by_id_endpoint):
    invalid_meme_id = "invalid_id"
    put_meme_by_id_endpoint.change_meme_by_id(auth_token, payloads.payload_with_info, invalid_meme_id)
    assert put_meme_by_id_endpoint.check_status_code_is_(404)


@allure.feature('Update meme by ID')
@allure.story('Change a meme info with valid fields')
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("text", ['what are memes'])
@pytest.mark.parametrize("url", ['www.example.com'])
@pytest.mark.smoke
def test_update_meme_by_id_check_info(auth_token, new_meme, put_meme_by_id_endpoint, text, url):
    payload = payloads.new_meme_empty_payload
    payload['id'] = new_meme
    payload['text'] = text
    payload['url'] = url
    put_meme_by_id_endpoint.change_meme_by_id(auth_token, new_meme, payload)
    assert put_meme_by_id_endpoint.check_response_text_is_(text)
    assert put_meme_by_id_endpoint.check_response_url_is_(url)


@allure.feature('Delete meme by ID')
@allure.story('Delete a meme with invalid id')
@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.parametrize("meme_id, expected_status", [
    ("invalid_id", 404),
    ("", 404),
])
def test_delete_meme_invalid_id(auth_token, delete_meme_endpoint, meme_id, expected_status):
    delete_meme_endpoint.delete_meme_with_id(auth_token, meme_id)
    delete_meme_endpoint.check_status_code_is_(expected_status)


@allure.feature('Delete meme by ID')
@allure.story('Delete a meme with valid id')
@pytest.mark.regression
@pytest.mark.positive
def test_delete_meme(auth_token, new_meme, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme_with_id(auth_token, new_meme)
    delete_meme_endpoint.check_status_code_is_(200)
