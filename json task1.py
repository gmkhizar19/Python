import json
import urllib.request
import urllib.parse

url = input("Enter location: ")
if len(url) < 1:
    url = "http://dr-chuck.net"

print("Retrieving", url)
try:
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    print(f"Retrieved {len(data)} characters")
except Exception as e:
    print("Error retrieving data:", e)
    quit()

try:
    info = json.loads(data)
except Exception as e:
    print("Error parsing JSON:", e)
    quit()

comments_list = info.get("comments", [])
total_count = len(comments_list)
total_sum = 0

for item in comments_list:
    total_sum += int(item.get("count", 0))

print("Count:", total_count)
print("Sum:", total_sum)
