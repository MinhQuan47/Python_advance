import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testmysql"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM testmysql_posts"
mycursor.execute(sql)
myresult = mycursor.fetchone()
print(myresult)
mydb.close()