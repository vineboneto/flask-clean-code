import json
from flask.testing import FlaskClient
from flask_jwt_extended import create_refresh_token
from faker import Faker
from tests.conftest import client

faker = Faker()


def test_refresh_token_200(client: FlaskClient):
    refresh_token = create_refresh_token(identity="something_user")
    response = client.post(
        "/accounts/refresh", headers={"Authorization": f"Bearer {refresh_token}"}
    )
    assert response.status_code == 200
