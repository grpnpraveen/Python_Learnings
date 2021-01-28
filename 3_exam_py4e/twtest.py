import urllib.error,urllib.parse,urllib.request
import ssl
from twurl import augment

print("*calling twitter...........")
url=augment('http://api.twitter.com/1.1/statuses/user-timeline.json',{'screen_name':'praveen','count':'2'})
print(url)
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

connection=urllib.request.urlopen(url,context=ctx)
data=connection.read()
print(data)
headers=dict(connection.getheaders())
print(headers)
