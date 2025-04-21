import datetime as dt

from FlightRadar24 import FlightRadar24API

fr_api = FlightRadar24API()
bounds = fr_api.get_bounds_by_point(43.230194, 34.187760, 250000)
flights = fr_api.get_flights(bounds=bounds)


def get_flights_information(flights=flights):
    list = []
    for flight in flights:
        details = fr_api.get_flight_details(flight)
        flight.set_flight_details(details)
        record_time = dt.datetime.now().time()
        callsing = flight.callsign
        icao = flight.airline_icao
        model = flight.aircraft_model
        airline = flight.airline_name
        origin_airport = flight.origin_airport_icao
        destination_airport = flight.destination_airport_icao
        latitude = flight.latitude
        longitude = flight.longitude
        info = (record_time, callsing,
                icao, model,
                airline, origin_airport,
                destination_airport,
                latitude, longitude)
        list.append(tuple(info))
    return list
