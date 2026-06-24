from utils.api_client import APIClient
from data.test_data import LOGIN_DATA

def test_login(client):
    res = client.post("/api/login",LOGIN_DATA )

    token = res.json()["token"]
    assert res.status_code == 200
    assert token in res.json()["token"]


