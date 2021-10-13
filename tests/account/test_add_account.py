import json
from faker import Faker
from tests.conftest import client

faker = Faker()


def test_add_account_200(client):
    request_body = dict(username=faker.name(), login=faker.name(), password=faker.password())
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 200


def test_add_account_409_conflict_login(client):
    conflict_body = dict(username=faker.name(), login=faker.name(), password=faker.password())
    conflict_response = client.post("/accounts", json=conflict_body)
    request_body = dict(
        username=faker.name(), login=conflict_body["login"], password=faker.password()
    )
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 409


def test_add_account_400_on_invalid_name(client):
    request_body = dict(login=faker.name(), password=faker.password())
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 400


def test_add_account_400_missing_login(client):
    request_body = dict(username=faker.name(), password=faker.password())
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 400


def test_add_account_400_missing_password(client):
    request_body = dict(username=faker.name(), login=faker.name())
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 400
