import mysql.connector as sql
db=sql.connect(
host="localhost",
user="root",
password="root",
database="imagestore"
)
cursor=db.cursor()
fhand=open("Farm.jpg","rb")
file=fhand.read()
cursor.execute("create table if not exists test(id int primary key,name varchar(200))")
state1="insert into test values(%s,%s)"
val1=(1,"prav")
val2=[(2,'nav'),(3,'rav'),(4,'pras')]
cursor.execute(state1,val1)
cursor.executemany(state1,val2)
db.commit()

print(cursor.rowcount," row inserted")

# print("1 record inserted, ID:", mycursor.lastrowid)
# ---------------------------------------------------------------
# mycursor = mydb.cursor()
#
# mycursor.execute("SELECT * FROM customers")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)
# ------------------------------------------------------------
# mycursor.execute("SELECT * FROM customers")
#
# myresult = mycursor.fetchone()
#
# print(myresult)
# ---------------------------------------------------------------------
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
