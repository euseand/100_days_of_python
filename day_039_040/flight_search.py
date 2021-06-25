import requests

from flight_data import FlightData
from constants import FS_API_KEY, FS_URL


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.url = FS_URL
        self.key = FS_API_KEY
        self.headers = {
            "apikey": self.key
        }

    def get_code(self, city_name):
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(
            f"{self.url}/locations/query",
            params=query,
            headers=self.headers
        )
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def get_flights(self, origin, destination, start, end):
        query = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": start.strftime("%d/%m/%Y"),
            "date_to": end.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(
            f"{self.url}/v2/search/",
            params=query,
            headers=self.headers
        )

        try:
            data = response.json()["data"][0]
            print(data)
        except IndexError:
            print(f"No flights found for {destination}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data
