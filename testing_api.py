import googlemaps
import json, csv

from datetime import datetime


# gmaps = googlemaps.Client(key='AIzaSyDNpXx0jnXEWv1OHmdmTkOKPU72Ge1DOxk')
# address = 'Constitution Ave NW & 10th St NW, Washington, DC'
# lat, lng = gmaps.address_to_latlng(address)
# print lat, lng

#Client key for google maps
gmaps = googlemaps.Client(key='AIzaSyDNpXx0jnXEWv1OHmdmTkOKPU72Ge1DOxk')

# Geocoding an address - testing one address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#convert to json
j = json.dumps(geocode_result)
# print j['results']['geometry']['location']['lat']
print j

getLocation = json.loads(j)
print getLocation [0]['geometry']['location']['lat']

#print geocode_result[0]
# jsonParsed = json.dumps(geocode_result)
# print jsonParsed
#convertJson = json.loads(geocode_result)
# dict(x.split(':') for x in jsonParsed.split(':'))




#latParsed = convertJ
# son['geometry'][0]['location']['lat']
# print latParsed
# latParsed = jsonParsed['lat']
#print latParsed

# Testing output
#print geocode_result
# print json.dumps(geocode_result, sort_keys=True, indent=4, separators=(',', ': '))
#
# with open('data.json', 'w') as outfile:
#     json.dump(geocode_result, outfile)

