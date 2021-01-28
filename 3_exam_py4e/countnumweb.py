import urllib.parse,urllib.error,urllib.request
import re
from bs4 import BeautifulSoup
y=list()
# uh=urllib.request.urlopen('http://py4e-data.dr-chuck.net/regex_sum_948558.txt')
uh=urllib.request.urlopen("https://spatialpoint.com/desktop/mapinfo-anysite/")
# soup=BeautifulSoup(uh,"html.parser")
# fhand=open("online.txt","w")
# fhand.writelines(str(soup))

for line in uh:
    print(line.decode().strip())



# for line in uh:
#     x=line.decode().strip()
#     z=re.findall("[0-9]+",x)
#     for p in z:
#          p=int(p)
#          y.append(p)
# count=0
# for i in y:
#     count=i+count
# print(count)
