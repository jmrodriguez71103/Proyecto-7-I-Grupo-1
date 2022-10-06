import mysql.connector as mysql


HOST = "34.134.244.239"

DATABASE = "mydb"

USER = "root"

PASSWORD = "Megustaredes321*"



mydb = mysql.connect(host= HOST, database= DATABASE, user= USER, password= PASSWORD)

c = mydb.cursor()

c.execute("show databases")

for x in c:
    print (x)
