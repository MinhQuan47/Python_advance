import mysql.connector
# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "testmysql"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM testmysql_posts WHERE ID = %s"
adr = ("3", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
# disconnect from MySQL
mydb.close()
