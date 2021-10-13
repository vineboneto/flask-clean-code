import json
from tests.conftest import client, mock_authorization
from faker import Faker

faker = Faker()


def test_delete_account_200(client):
    request_body = dict(username=faker.name(), login=faker.name(), password=faker.password())
    response_account = client.post("/accounts", json=request_body)
    data = json.loads(response_account.data)
    response = client.delete(f"/accounts/{data['id']}", headers=mock_authorization())
    assert response.status_code == 200


def test_delete_account_204(client):
    response = client.delete("/accounts/-1", headers=mock_authorization())
    assert response.status_code == 204


def test_delete_account_403(client):
    response = client.delete("/accounts/-1")
    assert response.status_code == 403
