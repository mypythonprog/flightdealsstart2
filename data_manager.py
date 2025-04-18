import requests
from dotenv import load_dotenv
import os
load_dotenv()
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.url = None
        self.params = None
        self.sheety_get_response = None
        self.put_url = None
        self.put_updated = None
        self.sheety_get_url = os.environ["SHEET_URL"]#"https://api.sheety.co/bcf987a1c159769edbdbe962054dcb39/copyOfFlightDeals/prices"

    def sheet_data(self):
        self.sheety_get_response = requests.get(url=self.sheety_get_url)
        return self.sheety_get_response.json()
    def iata_code_updater(self,ids):
        self.params = {'price':{
        'iataCode':ids['iataCode'],
        }
        }
        self.put_updated = requests.put(url=f"{self.sheety_get_url}/{ids['id']}",json=self.params)




