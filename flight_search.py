from dotenv import load_dotenv
import requests
import os

from requests import HTTPError

load_dotenv()
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ['AMADEUS_API_KEY']
        self._api_secret = os.environ['API_SECERT']
        self._token = self._get_new_token()
       

    def _get_new_token(self):
        self.post_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'

        }
        self.amadeus_params = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret,

        }
        self.get_token = requests.post(self.post_url,data=self.amadeus_params,headers=self.headers)
        return self.get_token.json()['access_token']
    def _get_iatacode(self,city):

            self.cities = city
            self.get_url = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
            self.params = {
                'keyword':city.upper(),

            }
            self.headers = {
                'Authorization': f'Bearer {self._token}',

            }
            self.iata_codes_json = requests.get(url=self.get_url,params=self.params,headers=self.headers)
            try :
             self.iatacodes = self.iata_codes_json.json()['data'][0]['iataCode']
             print(self.iatacodes)
             return self.iatacodes
            except IndexError:
               print(f"The code failed because of {IndexError} ")
            except KeyError:
                print(f'the code faild because of {KeyError}')





