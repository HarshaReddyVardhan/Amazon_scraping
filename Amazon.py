from urllib.request import urlopen
import json
import urllib
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urlpresent = True
url = 'https://www.amazon.com/s?k=mens+sunglasses&ref=nb_sb_noss_2'
if not urlpresent :
    url = input('enter Url : ')
read_url = urlopen(url)
data = json.loads(read_url.read().decode())
total = 0
for item in data['comments']:
    total += int(item['count'])
print(total)
