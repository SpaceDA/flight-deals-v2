import requests
from pprint import pprint
import json


SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/32a9ab328d4bc3dc48610ae717111330/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/32a9ab328d4bc3dc48610ae717111330/flightDeals/users"
BITLY_ENDPOINT = "https://api-ssl.bitly.com/v4/shorten"
BITLY_TOKEN = "1ac5ccc98baf086342948642d44bb3b779fbc6c0"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        try:
            headers = {"Authorization": f"Bearer {os.environ['gmail_pw']}"}
            r = requests.get(SHEETY_PRICES_ENDPOINT, headers=headers, timeout=5)
            data = r.json()
        except:
            print("Site not reachable", SHEETY_PRICES_ENDPOINT)
            exit()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        headers = {"Authorization": f"Bearer {os.environ['gmail_pw']}"}
        for city in self.destination_data:
            new_data = {
                "price":
                    {
                        "iataCode": city["iataCode"]
                    }
            }
            r = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=headers,
                json=new_data
            )

    def get_users(self):
        try:
            headers = {"Authorization": f"Bearer {os.environ['gmail_pw']}"}
            r = requests.get(SHEETY_USERS_ENDPOINT, headers=headers, timeout=5)
            users = [user["email"] for user in r.json()["users"]]
            return users
        except:
            print("Site not reachable", SHEETY_PRICES_ENDPOINT)
            exit()

    def short_url(self, url):
        headers = {
            'Authorization': f'Bearer {BITLY_TOKEN}',
            'Content-Type': 'application/json',
        }

        data = {"long_url": url}


        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=json.dumps(data))

        return response.json()['link']



test = DataManager()
test.get_users()

