# test_users_auth_mocked.py
import pytest
import requests
import responses

BASE_URL = "https://127.0.0.1:8000/users"


@pytest.fixture
def mocked_responses():
    """Provides a fresh responses mock for each test."""
    with responses.RequestsMock() as rsps:
        yield rsps


def test_users_unauthorized_mocked(mocked_responses):
    """
    Mocked server:
      - Request: /users?username=admin&password=admin
      - Response: 401 with empty text
    """

    mocked_responses.add(
        method=responses.GET,
        url=BASE_URL,
        match=[
            responses.matchers.query_param_matcher({
                "username": "admin",
                "password": "admin",
            })
        ],
        body="",          # empty text response
        status=401
    )

    response = requests.get(BASE_URL, params={
        "username": "admin",
        "password": "admin"
    })

    assert response.status_code == 401
    assert response.text == ""


def test_users_authorized_mocked(mocked_responses):
    """
    Mocked server:
      - Request: /users?username=admin&password=qwerty
      - Response: 200 with empty text
    """

    mocked_responses.add(
        method=responses.GET,
        url=BASE_URL,
        match=[
            responses.matchers.query_param_matcher({
                "username": "admin",
                "password": "qwerty",
            })
        ],
        body="",          # empty text response
        status=200
    )

    response = requests.get(BASE_URL, params={
        "username": "admin",
        "password": "qwerty"
    })

    assert response.status_code == 200
    assert response.text == ""
