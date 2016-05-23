
'''
google_geocode_nyu.py
Author: Holly Orr
Date: 5/19/2016

Description: Uses googlemaps package to apply Google API key when requests exceed Google's
2500 daily limit. Reads fda_id and addresses from csv and writes fda_id, addresses, lat and long to
a new csv.

googlemaps from https://github.com/googlemaps/google-maps-services-python
This code and readme available at https://github.com/nyu-mhealth/Geocode-Google-APIKey-Python
'''

# packages
import googlemaps
import json, csv, time
import urllib2 as ul
import pandas as pd
import numpy as np
import datetime

# Global Variables*********************************

#csv to read from
inCSV = 'address_7001_end.csv'
#csv to write to
outCSV = 'geocode_7001_end.csv'

#Client key for google maps
gmaps = googlemaps.Client(key='AIzaSyDNpXx0jnXEWv1OHmdmTkOKPU72Ge1DOxk')

#Dictionary
dict = {}

# get run start time
start = datetime.datetime.now()
print "Start time: " + str(start)

#read csv address
fields = ['fda_id', 'address']
df = pd.read_csv(inCSV, skipinitialspace=True, usecols=fields)

#iterate through rows of read csv
for index, row in df.iterrows():
    idValue = row['fda_id']
    addressValue = row['address']

    # Geocode address
    geocode_result = gmaps.geocode(addressValue)

    #if array is empty, which means address does not exist and can't be geocoded, give values of 0
    if not geocode_result:
        longVal = 0
        latVal = 0
    else:
        #convert to json
        j = json.dumps(geocode_result)
        getLocation = json.loads(j)
        #grab latitude and longitude from json
        longVal = getLocation [0]['geometry']['location']['lng']
        latVal = getLocation [0]['geometry']['location']['lat']

    #create dictionary from address, long, and lat
    dict.setdefault('fda_id', []).append(idValue)
    dict.setdefault('address', []).append(addressValue)
    dict.setdefault('longitude', []).append(longVal)
    dict.setdefault('latitude', []).append(latVal)
    print idValue, addressValue, longVal, latVal

#output all values to csv
raw_data = dict
df = pd.DataFrame(raw_data, columns = ['fda_id','address', 'longitude', 'latitude'])
df.to_csv(outCSV)

# get run end time
done = datetime.datetime.now()
print "End time: " + str(done)

