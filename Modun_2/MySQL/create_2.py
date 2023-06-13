import mysql.connector
# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "testmysql"
)
mycursor = mydb.cursor()
# create table pcapmysql_comments
sql_string = """CREATE TABLE IF NOT EXISTS pcapmysql_comments (
ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
post_ID INT NOT NULL,
comment_author VARCHAR(255),
comment_content TEXT,
comment_date DATETIME
)
"""
mycursor.execute(sql_string)
# insert data for table pcapmysql_comments
sql = """INSERT INTO pcapmysql_comments (post_ID, comment_author, comment_content, 
comment_date) 
VALUES (%s, %s, %s, %s)
"""
val = [
("7", "SuperMan", "Good job, thanks.", "2022-10-15 10:46:05"),
("7", "Ahihi", "Good!", "2022-10-15 11:47:06"),
("8", "Huy Nguyễn", "Dễ hiểu.", "2022-10-15 11:48:07")
]
mycursor.executemany(sql, val)
mydb.commit()
# disconnect from MySQL
mydb.close()
