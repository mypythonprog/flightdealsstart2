#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
sheet_data = DataManager()
sheets_data = sheet_data.sheet_data()['prices']
ge_token = FlightSearch()
for data in sheets_data:
    if data['iataCode'] == '':

        iata_codes = FlightData(data)
    ge_token._get_iatacode(data['city'])
    sheet_data.iata_code_updater(data)




print(sheets_data)


