import requests
from utils.api_client import APIClient
import json
from config.config import BASE_URL

client = APIClient()
def test_users():
    res = client.get("/api/users?page=2")
    print(json.dumps(res.json(), indent=4))

    assert res.status_code == 200
    assert "data" in res.json()