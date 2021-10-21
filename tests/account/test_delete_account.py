from tests.conftest import client
from tests.mocks import mock_authorization, mock_create_account


def test_delete_account_200(client):
    data = mock_create_account(client)
    response = client.delete(f"/accounts/{data['id']}", headers=mock_authorization())
    assert response.status_code == 200


def test_delete_account_204(client):
    response = client.delete("/accounts/-1", headers=mock_authorization())
    assert response.status_code == 204


def test_delete_account_403(client):
    response = client.delete("/accounts/-1")
    assert response.status_code == 403
