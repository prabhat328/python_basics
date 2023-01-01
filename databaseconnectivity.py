import mysql.connector as mysql

db = mysql.connect(host = "host_name", user = "username", passwd = "password")
cursor = db.cursor()
cursor.execute("use databasename")
cursor.execute("select * from tablename")
for i in cursor:
    print(i)
