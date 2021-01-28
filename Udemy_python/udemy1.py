import pymysql
server=pymysql.connect("localhost","root","root","person")
cursor=server.cursor()
sql="insert into customer values('lailu',600);"
cursor.execute(sql)
server.commit()