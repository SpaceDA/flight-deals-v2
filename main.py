import datetime
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager



ORIGIN_IATA = "MCO"
# create object from data_manager
data_manager = DataManager()
# save destination data as variable in main.py
sheet_data = data_manager.get_destination_data()

#if the IATA code is blank, loop through the destination data, use the FlightSearch class to access the get_destination
#_data to update each row's IATA data in the sheet_data.

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"]=flight_search.get_destination_code(row['city'])


#now that we have updated IATA codes in local sheet_data, we need to update the data_manager attribute to talk to the
#sheety API -> google sheets
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

flight_search = FlightSearch()

tomorrow = datetime.now() + timedelta(days=1)
end_date = datetime.now() + timedelta(days=180)


for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_IATA,
        destination['iataCode'],
        tomorrow,
        end_date
    )

    if flight != None and flight.price < destination['lowestPrice']:
        notification = NotificationManager()
        short_url = data_manager.short_url(flight.link)
        message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-" \
                  f"{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport} from" \
                  f" {flight.date_depart} to {flight.date_return}"

        if flight.stop_overs > 0:
            message += f"\nFlight has one layover in {flight.via_city}-{flight.via_airport}."

        message += f"\n{short_url}"
        print(message)

        notification.send_email(message, data_manager.get_users())





        #notification.send_alert(message)

