from tests.test_main import client
from faker import Faker

faker = Faker()


def test_add_account_200(client):
    request_body = dict(username=faker.name(), login=faker.name())
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 200


def test_add_account_400_on_invalid_name(client):
    request_body = dict(login=faker.name())
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 400


def test_add_account_400_missing_login(client):
    request_body = dict(username=faker.name())
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 400
