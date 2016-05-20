import googlemaps
import json, csv, time
import urllib2 as ul
import pandas as pd
import numpy as np

from datetime import datetime


#Client key for google maps
gmaps = googlemaps.Client(key='AIzaSyDNpXx0jnXEWv1OHmdmTkOKPU72Ge1DOxk')

#TESTING
# testing hardcoded address string
addressString = '1600 Amphitheatre Parkway, Mountain View, CA'

# Testing Geocoding an address - testing one address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

#read csv address


#convert to json
j = json.dumps(geocode_result)
# print j['results']['geometry']['location']['lat']
print j

getLocation = json.loads(j)
# print getLocation [0]['geometry']['location']['lat']
latVal = getLocation [0]['geometry']['location']['lat']


dict = {}
dict.setdefault('address', []).append(addressString)
dict.setdefault('latitude', []).append(latVal)
print dict
raw_data = dict
df = pd.DataFrame(raw_data, columns = ['address', 'latitude'])
df.to_csv('example3.csv')



