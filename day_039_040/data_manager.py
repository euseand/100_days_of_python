import requests

from constants import SHEETY_URL, SHEETY_TOKEN


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = SHEETY_URL
        self.token = SHEETY_TOKEN
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_data(self):
        response = requests.get(
            self.url,
            headers=self.headers)
        return response.json()["prices"]

    def update_data(self, data):
        body = {
            "price": {
                "iataCode": data["iataCode"],
                "lowestPrice": data["lowestPrice"]
            }
        }
        response = requests.put(
            f"{self.url}/{data['id']}",
            json=body,
            headers=self.headers)
        return response.status_code
