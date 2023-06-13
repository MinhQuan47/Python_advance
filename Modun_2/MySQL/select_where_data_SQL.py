import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testmysql"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM testmysql_posts WHERE ID = '2' "
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mydb.close()