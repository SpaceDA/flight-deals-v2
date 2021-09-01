class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, price, origin_city, origin_airport, destination_city,
                 destination_airport, date_depart, date_return,stop_overs=0, via_city="", via_airport="", link=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_cityå
        self.destination_airport = destination_airport
        self.date_depart = date_depart
        self.date_return = date_return
        self.stop_overs = stop_overs
        self.via_city = via_city
        self.via_airport = via_airport
        self.link = link
