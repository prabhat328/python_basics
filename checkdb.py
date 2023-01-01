import mysql.connector as mysql

db = mysql.connect(host = "localhost", user = "Prabhat", passwd = "151103")
cursor = db.cursor()
cursor.execute("use prabhat")
cursor.execute("select * from skills")
for i in cursor:
    print(i)