import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = input("Enter: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html parser")

# retrive all of the anchor tags

tag = soup('a')
for tags in tag:
    print(tag.get("href", None))
