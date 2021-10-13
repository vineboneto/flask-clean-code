from flask.testing import FlaskClient
from faker import Faker
from werkzeug.datastructures import Headers
from tests.conftest import client, mock_authorization

faker = Faker()


def test_load_by_id_200(client: FlaskClient):
    response = client.get(f"/accounts/{1}", headers=mock_authorization())
    assert response.status_code == 200


def test_load_by_id_204(client):
    response = client.get(f"/accounts/{0}", headers=mock_authorization())
    assert response.status_code == 204


def test_load_by_id_403(client):
    response = client.get(f"/accounts/{0}")
    assert response.status_code == 403
