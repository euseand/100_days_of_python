from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from constants import ORIGIN_CITY_IATA

sheet = DataManager()
search = FlightSearch()

prices = sheet.get_data()
if not prices[0]["iataCode"]:
    for price in prices:
        iata_code = search.get_code(price["city"])
        price["iataCode"] = iata_code
        sheet.update_data(data=price)

today = datetime.now()
six_months_from_today = today + timedelta(days=180)
for dest in prices:
    flight = search.get_flights(
        ORIGIN_CITY_IATA,
        dest["iataCode"],
        today,
        six_months_from_today,
    )
    if flight:
        if flight.price < dest["lowestPrice"]:
            dest["lowestPrice"] = flight.price
            sheet.update_data(data=dest)
