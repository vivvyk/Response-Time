import googlemaps
import pprint
from datetime import datetime
import json
import numpy
import csv
import sys
import time
gmaps = googlemaps.Client(key='AIzaSyAg-loWjdYNw-DkQ45pdh_b37acplX-BNY')

def lessthan(time1, time2):
    if "hours" in time1:
        t1 = int(time1[:time1.index('h') - 1]) * 60 + int(time1[time1.index('s') + 1:time1.index('m')])
    elif "hour" in time1:
        t1 = int(time1[:time1.index('h') - 1]) * 60 + int(time1[time1.index('r') + 1:time1.index('m')])
    else:
        t1 = int(time1[:time1.index('m')])
    if "hours" in time2:
        t2 = int(time2[:time2.index('h') - 1]) * 60 + int(time2[time2.index('s') + 1:time2.index('m')])
    elif "hour" in time2:
        t2 = int(time2[:time2.index('h') - 1]) * 60 + int(time2[time2.index('r') + 1:time2.index('m')])
    else:
        t2 = int(time2[:time2.index('m')])
    return t1 <= t2
    
origin = "3892 Alder Avenue, Freemont, CA"
reader = csv.reader(open("Hospital_General_Information.csv", "rb"), delimiter=",")

states = {}
for i,v in enumerate(reader):
    if i == 0:
        continue
    if v[4] not in states.keys():
        states[v[4]] = [v]
    else:
        states[v[4]].append(v)
    
start = time.time()


travel_time = str(sys.maxint) + "mins"
hospital_name = "ERROR"

for ind, i in enumerate(states[origin[-2:]]):
    print ind
    try:
        directions = gmaps.directions(origin, i[2] + ", " + i[3] + ", " + i[4])
        if lessthan(directions[0]["legs"][0]["duration"]["text"], travel_time):
            travel_time = directions[0]["legs"][0]["duration"]["text"]
            hospital_name = i[1]
    except:
        continue
#     start_location = [directions[0]["legs"][0]["start_location"]["lat"], directions[0]["legs"][0]["start_location"]["lng"]]
#     end_location = [directions[0]["legs"][0]["end_location"]["lat"], directions[0]["legs"][0]["end_location"]["lng"]]
print hospital_name
print travel_time
print time.time() - start, "seconds"