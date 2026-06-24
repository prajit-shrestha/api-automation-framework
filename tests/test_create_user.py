from utils.api_client import APIClient
from data.test_data import USER_DATA
import json

client = APIClient()
def test_create_user():
    res = client.post("/api/users",USER_DATA)
    print(json.dumps(res.json(), indent=4))

    assert res.status_code == 201
    assert res.elapsed.total_seconds() < 2