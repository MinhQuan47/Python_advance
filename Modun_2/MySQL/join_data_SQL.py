import mysql.connector
# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "testmysql"
)
mycursor = mydb.cursor()
sql = """SELECT
pcapmysql_posts.ID,
pcapmysql_posts.post_title,
pcapmysql_comments.comment_author,
pcapmysql_comments.comment_content
FROM pcapmysql_posts
INNER JOIN pcapmysql_comments ON pcapmysql_posts.ID = 
pcapmysql_comments.post_ID
"""
mycursor.execute(sql)
myresult = mycursor.fetchall()
print("Displaying ID, Post Title, Comment Author and Comment Content:")
for x in myresult:
    print(x)
# disconnect from MySQL
mydb.close()
