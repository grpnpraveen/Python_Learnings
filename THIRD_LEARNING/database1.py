import sqlite3 as sql
conn=sql.connect("123.sqlite")
cur=conn.cursor()
cur.execute("drop table if exists info")
cur.execute('''create table info(email TEXT,count INTEGER)''')
fh=open(r"D:\programs\python\THIRD_LEARNING\mbox-short.txt")
for line in fh:
    if not line.startswith("From: "): continue
    pieces=line.split()
    email=pieces[1]
    cur.execute('''select count from info where email=?''',(email,))
    row=cur.fetchone()
    if row is None:
        cur.execute('''insert into info(email,count) values(?,1)''',(email,))
    else:
        cur.execute('''update info set count=count+1 where email=?''',(email,))

pop='''select email,count from info order by count desc limit 10'''

for ps in cur.execute(pop):
    print(ps[0],ps[1])
conn.commit()
