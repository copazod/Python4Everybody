import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
html = urllib.request.urlopen(url, context=ctx)
data = html.read().decode()

print('Retrieving', url)
print('Retrieved', len(data), 'characters')

info = json.loads(data)
#type: how json converts info in python,in this case it was in dict
#print(type(info))
#to convert info in list
#print(type(info['comments']))


# len = How many dicts in list/info['comments']
print('User count:', len(info['comments']))

num=list()
for item in info['comments']:
    x = (int(item['count']))
    num.append(x)

print(sum(num))
    
