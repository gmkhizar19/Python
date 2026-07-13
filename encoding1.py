import urllib.request
import urllib.parse
import urllib.error


fhndle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')


counts = dict()

for line in fhndle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
