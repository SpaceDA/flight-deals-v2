import requests
from flight_data import FlightData
from data_manager import DataManager
import os


kiwi_api_key = os.environ['kiwi_api_key']
AffilID = os.environ['AffilID]
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

data_manager = DataManager()


class FlightSearch:
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apiKey": kiwi_api_key, }
        query = {"term": city_name, "location_types": "city"}
        try:
            r = requests.get(location_endpoint, headers=headers, params=query)
        except:
            print("Site not reachable", location_endpoint)
            exit()
        code = (r.json()['locations'][0]['code'])
        return code


    def check_flights(self, origin_city_code, destination_city_code, from_date, to_date):
        headers = {"apiKey": kiwi_api_key, }
        search = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 8,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "USD",
            "limit": 10,
        }
        r = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=search)

        try:
            data = r.json()['data'][0]
        except IndexError:
            search['max_stopovers'] = 2
            r = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=search)
            data = r.json()['data'][0]

            flight_data = FlightData(
                price=data['price'],
                origin_city=data['route'][0]['cityFrom'],
                origin_airport=data['route'][0]['flyFrom'],
                destination_city=data['route'][1]['cityTo'],
                destination_airport=data['route'][1]['flyTo'],
                date_depart=data['route'][0]['local_departure'].split('T')[0],
                date_return=data['route'][2]['local_departure'].split('T')[0],
                stop_overs=1,
                via_city=data['route'][0]['cityTo'],
                via_airport=data['route'][0]['flyTo'],
                link=data['deep_link']
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                date_depart=data["route"][0]["local_departure"].split("T")[0],
                date_return=data["route"][1]["local_departure"].split("T")[0],
                link=data['deep_link']
            )
            return flight_data

        finally:
            message = f"{flight_data.destination_city}: ${flight_data.price}"
            add = ""
            link = data_manager.short_url(f"{flight_data.link}")
            if flight_data.stop_overs > 0:
                add = f"\nFly via {flight_data.via_city}({flight_data.via_airport})"


            message = message + add + "\n" + link
            print(message)

        return flight_data










