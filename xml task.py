import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter location: ")
if len(url) < 1:
    url = "http://dr-chuck.net"

print(f"Retrieving {url}")

try:
    response = urllib.request.urlopen(url)
    data = response.read()
    print(f"Retrieved {len(data)} characters")

    # Parse the XML data
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')

    total_sum = 0
    count_items = 0

    for item in counts:
        total_sum += int(item.text)
        count_items += 1

    print(f"Count: {count_items}")
    print(f"Sum: {total_sum}")

except Exception as e:
    print(f"Error retrieving or parsing data: {e}")
