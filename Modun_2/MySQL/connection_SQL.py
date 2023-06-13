import mysql.connector
# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
print(mydb)
# disconnect from MySQL
mydb.close()
