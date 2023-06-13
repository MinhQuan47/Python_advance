import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testmysql"
)
mycursor = mydb.cursor()
sql = "DELETE FROM testmysql_posts WHERE ID = %s"
# Delete row 5
adr = ("5",) 
mycursor.execute(sql,adr)
mydb.commit()
print(mycursor.rowcount,"record(s) deleted")
mydb.close()