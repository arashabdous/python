from urllib.request import urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML

api_url = 'http://maps.googleapis.com/maps/api/geocode/xml?'

address = input('Enter location: ')
url = api_url + ENCODE({'sensor': 'false', 'address': address})
print('\nRetrieving location for:', address)
data = OPEN(url).read()
tree = XML.fromstring(data)

res = tree.findall('result')

lat = res[0].find('geometry').find('location').find('lat').text
lng = res[0].find('geometry').find('location').find('lng').text

lat = float(lat)
lng = float(lng)

location = res[0].find('formatted_address').text


print(location)
print('Latitude: ',lat)
print('Longitude: ',lng)


