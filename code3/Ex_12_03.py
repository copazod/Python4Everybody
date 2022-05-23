import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Data collection
link = input ('Enter URL: ')
line = int(input('Enter position: '))
count = int(input('Enter count: '))

print('Retrieving: %s' % link)

for i in range(0,count):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')

    ps = 0
    for tag in tags:
        ps = ps + 1
        if ps == line:
            print('Retrieving: %s' % str(tag.get('href', None)))
            link = str(tag.get('href', None))
            ps = 0
            break
