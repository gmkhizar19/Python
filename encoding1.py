import urllib.request
import urllib.parse
import urllib.error


fhndle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhndle:
    print(line.decode().strip())
