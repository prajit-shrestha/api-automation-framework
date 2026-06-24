from utils.api_client import APIClient
import json

client = APIClient()
def test_update_user():
    update_data = {
        "name": "Prajit Shrestha",
        "job":"QA automation"
    }
    res = client.put("/api/users/796",update_data)

    print(json.dumps(res.json(), indent=4))

    assert res.status_code == 200
    assert res.json()["name"] == "Prajit Shrestha"
    assert res.json()["job"] == "QA automation"