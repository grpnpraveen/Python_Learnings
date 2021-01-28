import json
import urllib.error, urllib.request, urllib.parse
url=input("entre the url:")
html=urllib.request.urlopen(url).read()
data=json.loads(html)
x=data['comments']
a=list()
count=0
for i in x:
    a.append(int(i['count']))
for i in a:
    count=i+count
print(count)
# http://py4e-data.dr-chuck.net/comments_42.json
