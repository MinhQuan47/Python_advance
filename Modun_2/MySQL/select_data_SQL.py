import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testmysql"
)
mycursor = mydb.cursor()
# Select * From data 
sql = "SELECT * FROM testmysql_posts"
mycursor.execute(sql)
myresut = mycursor.fetchall()
# fuc fetchall() return list row data 
for x in myresut:
    print(x)
mydb.close()