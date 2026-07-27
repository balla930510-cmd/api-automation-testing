import requests

from config.config import BASE_URL
from config.config import HEADERS


class APIClient:

    def get(self, endpoint):

        return requests.get(
            BASE_URL + endpoint,
            headers=HEADERS
        )

    def post(self, endpoint, payload):

        return requests.post(
            BASE_URL + endpoint,
            json=payload,
            headers=HEADERS
        )

    def put(self, endpoint, payload):

        return requests.put(
            BASE_URL + endpoint,
            json=payload,
            headers=HEADERS
        )

    def delete(self, endpoint):

        return requests.delete(
            BASE_URL + endpoint,
            headers=HEADERS
        )