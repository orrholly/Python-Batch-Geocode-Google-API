import googlemaps
import json, csv, time
import urllib2 as ul
import pandas as pd
import numpy as np

from datetime import datetime
fields = ['address']

df = pd.read_csv('api_test.csv', skipinitialspace=True, usecols=fields)
# See the keys
# print df.keys()
# See content in 'star_name'
# print df.address
addressValue = df.get_value(0,'address')
print addressValue


#Client key for google maps
gmaps = googlemaps.Client(key='AIzaSyDNpXx0jnXEWv1OHmdmTkOKPU72Ge1DOxk')

#TESTING
# testing hardcoded address string
# addressString = '1600 Amphitheatre Parkway, Mountain View, CA'

# Geocoding an address - testing address read from csv
geocode_result = gmaps.geocode(addressValue)

#read csv address


#convert to json
j = json.dumps(geocode_result)
# print j['results']['geometry']['location']['lat']
print j

getLocation = json.loads(j)

#grab latitude and longitude from json
longVal = getLocation [0]['geometry']['location']['lng']
#print longVal
latVal = getLocation [0]['geometry']['location']['lat']
# print latVal


#create dictionary from address, long, and lat
dict = {}
dict.setdefault('address', []).append(addressValue)
dict.setdefault('longitude', []).append(longVal)
dict.setdefault('latitude', []).append(latVal)

print dict
raw_data = dict
df = pd.DataFrame(raw_data, columns = ['address', 'longitude', 'latitude'])
df.to_csv('example3.csv')



