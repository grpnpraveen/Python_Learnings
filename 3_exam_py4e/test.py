import urllib.error,urllib.parse,urllib.request
from bs4 import BeautifulSoup
url=input("enter url:")
count=int(input("enter the count :"))
position=int(input("enter the position:"))
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,"html.parser")
tags=soup('a')
for tag in tags:
    print(tag.get("href"))

#
# http://py4e-data.dr-chuck.net/known_by_Cephas.html
# http://py4e-data.dr-chuck.net/known_by_Fikret.html
