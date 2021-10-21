import json
from faker import Faker
from tests.conftest import client
from tests.mocks import mock_account, mock_authorization, mock_create_account

faker = Faker()


def test_update_account_200(client):
    account = mock_create_account(client)
    print(account)
    response = client.put(f"/accounts/{account['id']}", json=account, headers=mock_authorization())
    assert response.status_code == 200


def test_update_account_409_conflict_login(client):
    conflict_account = mock_create_account(client)
    to_update_account = mock_create_account(client)
    response_body = mock_account(dict(login=conflict_account["login"]))
    response = client.put(
        f"/accounts/{to_update_account['id']}", json=response_body, headers=mock_authorization()
    )
    assert response.status_code == 409


def test_update_account_200_conflict_login_with_same_id(client):
    to_update_account = mock_create_account(client)
    response_body = mock_account(dict(login=to_update_account["login"]))
    response = client.put(
        f"/accounts/{to_update_account['id']}", json=response_body, headers=mock_authorization()
    )
    assert response.status_code == 200


def test_update_account_204(client):
    request_body = mock_account()
    response = client.put("/accounts/-1", json=request_body, headers=mock_authorization())
    assert response.status_code == 204


def test_update_account_400_on_invalid_username(client):
    account = mock_account()
    del account["username"]
    response = client.put("/accounts/1", json=account, headers=mock_authorization())
    assert response.status_code == 400


def test_update_account_400_missing_login(client):
    account = mock_account()
    del account["login"]
    response = client.put("/accounts/1", json=account, headers=mock_authorization())
    assert response.status_code == 400


def test_update_account_400_missing_roles(client):
    account = mock_account()
    del account["roles"]
    response = client.put("/accounts/1", json=account, headers=mock_authorization())
    assert response.status_code == 400


def test_update_account_403(client):
    account = mock_account()
    response = client.put("/accounts/1", json=account)
    assert response.status_code == 403
