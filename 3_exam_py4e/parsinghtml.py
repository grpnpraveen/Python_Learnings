import urllib.error,urllib.parse,urllib.request
from bs4 import BeautifulSoup
url=input("enter url:")
data=urllib.request.urlopen(url).read()
soup=BeautifulSoup(data,"html.parser")
tags=soup('span')
a=list()
count=0
for tag in tags:
    a.append(int(tag.text))
for j in a:
    count=count+j
print(count)
