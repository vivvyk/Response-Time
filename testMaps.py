'''
Created on Apr 21, 2017

@author: roop
'''
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyDSPgOMDFfBFW3YvwHHpNdvBSy838l3NBI")
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

print directions_rest
