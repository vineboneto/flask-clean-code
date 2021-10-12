from tests.conftest import client
from faker import Faker

faker = Faker()


def test_load_by_id_200(client):
    response = client.get(f"/accounts/{1}")
    assert response.status_code == 200


def test_load_by_id_204(client):
    response = client.get(f"/accounts/{0}")
    assert response.status_code == 204
