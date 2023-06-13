import mysql.connector
# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "testmysql"
)
mycursor = mydb.cursor()
sql = "UPDATE testmysql_posts SET post_author = 'Huy Nguyễn' WHERE ID = '1'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
# disconnect from MySQL
mydb.close()
