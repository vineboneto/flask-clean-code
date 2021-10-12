import json
from tests.conftest import client
from faker import Faker

faker = Faker()


def test_update_account_200(client):
    request_body = dict(username=faker.name(), login=faker.name())
    response = client.put("/accounts/1", json=request_body)
    assert response.status_code == 200


def test_update_account_409_conflict_login(client):
    conflict_body = dict(username=faker.name(), login=faker.name(), password=faker.password())
    client.post("/accounts", json=conflict_body)
    to_update_body = dict(username=faker.name(), login=faker.name(), password=faker.password())
    to_update_response = client.post("/accounts", json=to_update_body)
    response_body = dict(username=faker.name(), login=conflict_body["login"])
    data = json.loads(to_update_response.data)
    response = client.put(f"/accounts/{data['id']}", json=response_body)
    assert response.status_code == 409


def test_update_account_200_conflict_login_with_same_id(client):
    to_update_body = dict(username=faker.name(), login=faker.name(), password=faker.password())
    to_update_response = client.post("/accounts", json=to_update_body)
    response_body = dict(username=faker.name(), login=to_update_body["login"])
    data = json.loads(to_update_response.data)
    response = client.put(f"/accounts/{data['id']}", json=response_body)
    assert response.status_code == 200


def test_update_account_204(client):
    request_body = dict(username=faker.name(), login=faker.name())
    response = client.put("/accounts/-1", json=request_body)
    assert response.status_code == 204


def test_update_account_400_on_invalid_name(client):
    request_body = dict(login=faker.name())
    response = client.put("/accounts/1", json=request_body)
    assert response.status_code == 400


def test_update_account_400_missing_login(client):
    request_body = dict(username=faker.name())
    response = client.put("/accounts/1", json=request_body)
    assert response.status_code == 400
