from flask.testing import FlaskClient
from faker import Faker
from tests.conftest import client

faker = Faker()


def test_login_200(client: FlaskClient):
    new_account = dict(username=faker.name(), login=faker.name(), password="1234")
    print(new_account["password"])
    client.post("/accounts", json=new_account)
    body = dict(login=new_account["login"], password=new_account["password"])
    response = client.post("/accounts/login", json=body)
    assert response.status_code == 200
