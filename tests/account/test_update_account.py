from tests.test_main import client
from faker import Faker

faker = Faker()


def test_update_account_200(client):
    request_body = dict(username=faker.name(), login=faker.name())
    response = client.put("/accounts/1", json=request_body)
    print(response.data)
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
