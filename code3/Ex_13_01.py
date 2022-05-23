import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
html = urllib.request.urlopen(url, context=ctx)
data = html.read()

print('Retrieving', url)
print('Retrieved', len(data), 'characters')


tree = ET.fromstring(data)
counts = tree.findall('comments/comment')

num=list()

for item in counts:
    x = item.find('count').text
    #print(x)

    n = int(x)
    num.append(n)

print('Count: ', len(counts))
print(sum(num))
