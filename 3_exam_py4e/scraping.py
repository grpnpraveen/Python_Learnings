
import urllib.error, urllib.request, urllib.parse
from bs4 import BeautifulSoup
url = input("Enter URL: ")
count = int(input("Times: "))
pos = int(input("Position: "))-1

print("retriving:"+url)
for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    tag = tags[pos].get('href',None)
    url = tag
    # name = tags[pos].contents[0]
    print("retriving:"+url)
# print(name)
# http://py4e-data.dr-chuck.net/known_by_Fikret.html
