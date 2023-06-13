import mysql.connector
# create connection to MySQL
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database = "testmysql"
)
mycursor = mydb.cursor()
# create table pcapmysql_posts
sql_string = """CREATE TABLE IF NOT EXISTS pcapmysql_posts (
ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
post_author VARCHAR(255),
post_title TEXT,
post_content TEXT,
post_date DATETIME
)
"""
mycursor.execute(sql_string)
# insert data for table pcapmysql_posts
sql = """INSERT INTO pcapmysql_posts (post_author, post_title, post_content, 
post_date) 
VALUES (%s, %s, %s, %s)
"""
val = [
("Huy Nguyễn", "Kết nối MySQL", "Cách kết nối MySQL sử dụng Python", 
"2022-10-15 19:46:05"),
("Huy Nguyễn", "Insert data vào table", "Sử dụng câu lệnh INSERT INTO", 
"2022-10-15 19:47:06"),
("Huy Nguyễn", "Drop table", "Xóa table trong MySQL", "2022-10-15 19:48:07")
]
mycursor.executemany(sql, val)
mydb.commit()
# disconnect from MySQL
mydb.close()
