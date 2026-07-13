import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# User inputs
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count):
    print('Retrieving:', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')

    target_tag = tags[position - 1]

    url = target_tag.get('href', None)

print('Retrieving:', url)

last_name = target_tag.text
print(f"\nThe answer to the assignment for this execution is '{last_name}'.")
