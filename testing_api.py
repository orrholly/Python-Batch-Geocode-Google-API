import googlemaps
import json, csv, time
import urllib2 as ul
import pandas as pd
import numpy as np

from datetime import datetime

#Client key for google maps
gmaps = googlemaps.Client(key='AIzaSyDNpXx0jnXEWv1OHmdmTkOKPU72Ge1DOxk')

#global for dictionary
dict = {}

#read csv address
fields = ['address']
df = pd.read_csv('warning_two.csv', skipinitialspace=True, usecols=fields)

#this might be faster - keep until later
# for r in df.itertuples():
#     print(r)

# See content in 'address' - keep in case
# addressValue = df.get_value(0,'address')
# print addressValue

#TESTING
# testing hardcoded address string
# addressString = '1600 Amphitheatre Parkway, Mountain View, CA'

#iterate through rows
for index, row in df.iterrows():
    print row['address']
    addressValue = row['address']

    # Geocoding an address - testing one address
    geocode_result = gmaps.geocode(addressValue)

    #convert to json
    j = json.dumps(geocode_result)
    # print j['results']['geometry']['location']['lat']
    # print j

    getLocation = json.loads(j)

    #grab latitude and longitude from json
    longVal = getLocation [0]['geometry']['location']['lng']
    #print longVal
    latVal = getLocation [0]['geometry']['location']['lat']
    # print latVal

    #create dictionary from address, long, and lat
    dict.setdefault('address', []).append(addressValue)
    dict.setdefault('longitude', []).append(longVal)
    dict.setdefault('latitude', []).append(latVal)


#output all values to csv
# print dict
raw_data = dict
df = pd.DataFrame(raw_data, columns = ['address', 'longitude', 'latitude'])
df.to_csv('example.csv')



