import mysql.connector
# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "testmysql"
    )
mycursor = mydb.cursor()
sql = """INSERT INTO testmysql_posts 
    (post_author, post_title, post_content,post_date) 
     VALUES (%s, %s, %s, %s)
     """
val = [
        ("Python PCAP", "Python to MySQL 1", 
        "Nội dung bài số 1", "2022-10-12 19:46:05"),
        ("Python PCAP", "Python to MySQL 2", 
        "Nội dung bài số 2", "2022-10-12 19:47:06"),
        ("Python PCAP", "Python to MySQL 3", 
        "Nội dung bài số 3", "2022-10-12 19:48:07"),
        ("Python PCAP", "Python to MySQL 4", 
        "Nội dung bài số 4", "2022-10-12 19:49:08"),
        ("Python PCAP", "Python to MySQL 5", 
        "Nội dung bài số 5", "2022-10-12 19:50:09")
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) was inserted.")
# disconnect from MySQL
mydb.close()