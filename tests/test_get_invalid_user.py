import json

from utils.api_client import APIClient

client = APIClient()

def test_get_invalid_user():
    res = client.get('/api/user/999')

    assert res.status_code == 404