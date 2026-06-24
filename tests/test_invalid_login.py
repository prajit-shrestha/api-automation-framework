import json

from utils.api_client import APIClient

client = APIClient()

invalid_data = {
    "email": "Prajit shrestha",
    "password": "Prajit123",
}
def test_invalid_login():
    res = client.post("/api/login",invalid_data)
    print(json.dumps(res.json(), indent=4))
    assert res.status_code == 400