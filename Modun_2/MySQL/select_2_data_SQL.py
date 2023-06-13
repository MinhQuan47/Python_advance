import mysql.connector
# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "testmysql"
)
mycursor = mydb.cursor()
sql = "SELECT post_author, post_title, post_content FROM testmysql_posts"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print("type of myresult:", type(myresult))
for x in myresult:
    print(x)
# disconnect from MySQL
mydb.close()