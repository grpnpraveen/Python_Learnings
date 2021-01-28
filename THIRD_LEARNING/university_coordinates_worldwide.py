import sqlite3 as sq
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
conn=sq.connect("unistycordinates.sqlite")
cur=conn.cursor()
api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

fh=open("where.data","r")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
i=1
cur.execute("drop table if exists places")
cur.execute('''create table places(sno int,name text,lat int,lng int)''')
for line in fh:
	address=line.strip()
	parms = dict()
	parms['address'] = address
	parms['key'] = api_key
	url = serviceurl + urllib.parse.urlencode(parms)
	print('Retrieving', url)
	uh = urllib.request.urlopen(url, context=ctx)
	data=uh.read().decode()
	try:

		js=json.loads(data)
		lat=js["results"][0]["geometry"]["location"]["lat"]
		lng=js["results"][0]["geometry"]["location"]["lng"]
		cur.execute('''insert into places values(?,?,?,?) ''',(i,address,lat,lng))
		i=i+1
	except:
		js=None



conn.commit()
