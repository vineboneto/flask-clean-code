import json
from tests.test_main import client
from faker import Faker

faker = Faker()


def test_add_account_200(client):
    request_body = dict(username=faker.name(), login=faker.name(), password=faker.password())
    response_account = client.post("/accounts", json=request_body)
    data = json.loads(response_account.data)
    response = client.delete(f"/accounts/{data['id']}")
    assert response.status_code == 200


def test_add_account_400_on_invalid_name(client):
    response = client.delete("/accounts/-1")
    assert response.status_code == 204
