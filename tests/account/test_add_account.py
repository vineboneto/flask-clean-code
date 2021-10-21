from faker import Faker
from tests.conftest import client
from tests.mocks import mock_account

faker = Faker()


def test_add_account_200(client):
    response = client.post("/accounts", json=mock_account())
    assert response.status_code == 200


def test_add_account_409_conflict_login(client):
    conflict_body = mock_account()
    client.post("/accounts", json=conflict_body)
    request_body = mock_account(dict(login=conflict_body["login"]))
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 409


def test_add_account_400_on_invalid_name(client):
    request_body = dict(login=faker.name(), password=faker.password(), roles=[faker.name()])
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 400


def test_add_account_400_missing_login(client):
    request_body = dict(username=faker.name(), password=faker.password(), roles=[faker.name()])
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 400


def test_add_account_400_missing_password(client):
    request_body = dict(username=faker.name(), login=faker.name(), roles=[faker.name()])
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 400


def test_add_account_400_missing_roles(client):
    request_body = dict(username=faker.name(), login=faker.name(), password=faker.password())
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 400
