import os
import pytest
from flask.testing import FlaskClient
from flask_jwt_extended import create_access_token
from src.main.config import config_by_name
from src.main.app import create_app
from collections import namedtuple


@pytest.fixture(scope="session")
def client() -> FlaskClient:
    app = create_app()
    app.config.from_object(config_by_name["test"])
    with app.test_client() as client:
        yield client


def mock_authorization():
    token = create_access_token("something_user")
    headers = {"Authorization": f"Bearer {token}"}
    return headers
