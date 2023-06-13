import mysql.connector
# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "testmysql"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM testmysql_posts ORDER BY ID"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
# disconnect from MySQL
mydb.close()
