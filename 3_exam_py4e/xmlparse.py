import xml.etree.ElementTree as ET
import urllib.error, urllib.request, urllib.parse

url=input("entre the url:")
html=urllib.request.urlopen(url).read()
m=ET.fromstring(html)
lst=m.findall('comments/comment')
s=list()
count=0
for item in lst:
    s.append(int(item.find('count').text))
for u in s:
    count=u+count
print(count)
