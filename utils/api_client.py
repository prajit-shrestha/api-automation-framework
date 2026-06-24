import requests
from config.config import BASE_URL, HEADERS

class APIClient:

    def get(self, endpoint):
        return requests.get(BASE_URL + endpoint, headers=HEADERS)

    def post(self, endpoint, data):
        return requests.post(BASE_URL + endpoint, json=data, headers=HEADERS)

    def put(self, endpoint, data):
        return requests.put(BASE_URL + endpoint, json=data, headers=HEADERS)

    def delete(self, endpoint):
        return requests.delete(BASE_URL + endpoint, headers=HEADERS)