import urllib.error,urllib.parse,urllib.request
from bs4 import BeautifulSoup

url=input("ENTER THE WEBSITE URL:")

html=urllib.request.urlopen("http://data.pr4e.org/romeo.txt").read()
soup=BeautifulSoup(html,'html.parser')

print(soup)
To get anchor links from web data

tags=soup('a')

for tag in tags:
    print(tag.get('href',None))
