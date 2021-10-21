import pytest
from flask.testing import FlaskClient
from src.main.config import config_by_name
from src.main.app import create_app


@pytest.fixture(scope="session")
def client() -> FlaskClient:
    app = create_app()
    app.config.from_object(config_by_name["test"])
    with app.test_client() as client:
        yield client
