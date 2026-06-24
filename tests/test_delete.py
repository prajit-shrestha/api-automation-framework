from utils.api_client import APIClient
import json

client = APIClient()
def test_delete():
    res = client.delete("/api/users/796")

    print(res)
    assert res.status_code == 204
    assert res.text == ""