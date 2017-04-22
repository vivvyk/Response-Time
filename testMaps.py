import googlemaps
import pprint
from datetime import datetime
import json
gmaps = googlemaps.Client(key='AIzaSyDSPgOMDFfBFW3YvwHHpNdvBSy838l3NBI')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

origin = "3892 Alder Avenue, Freemont, CA"
destination = "454 Tennessee Ln, Palo Alto, CA"

directions = gmaps.directions(origin,destination)

pp = pprint.PrettyPrinter(indent=1)

pp.pprint(directions)
travel_time = directions[0]["legs"][0]["duration"]["text"]
start_location = [directions[0]["legs"][0]["start_location"]["lat"], directions[0]["legs"][0]["start_location"]["lng"]]
end_location = [directions[0]["legs"][0]["end_location"]["lat"], directions[0]["legs"][0]["end_location"]["lng"]]
print(end_location)



'''
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
'''
