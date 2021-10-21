from tests.conftest import client
from tests.mocks import mock_authorization, mock_create_account


def test_load_by_id_200(client):
    data = mock_create_account(client)
    response = client.get(f"/accounts/{data['id']}", headers=mock_authorization())
    assert response.status_code == 200


def test_load_by_id_204(client):
    response = client.get(f"/accounts/{0}", headers=mock_authorization())
    assert response.status_code == 204


def test_load_by_id_403(client):
    response = client.get(f"/accounts/{0}")
    assert response.status_code == 403
