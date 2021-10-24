from flask_jwt_extended import create_access_token
from faker import Faker


def make_faker():
    return Faker()


def mock_authorization():
    token = create_access_token("something_user")
    headers = {"Authorization": f"Bearer {token}"}
    return headers


def mock_account(account: dict = {}):
    account = {
        "username": make_faker().name(),
        "password": make_faker().password(),
        "roles": [make_faker().name()],
        "login": make_faker().name(),
        **account,
    }
    return account


def mock_create_account(client):
    request_body = mock_account(dict(login=make_faker().name()))
    response_account = client.post("/accounts", json=request_body)
    data = response_account.json
    return data
