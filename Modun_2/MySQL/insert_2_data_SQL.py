import mysql.connector
from datetime import datetime
# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "testmysql"
    )
mycursor = mydb.cursor()
sql = """INSERT INTO testmysql_posts (post_author, post_title, post_content, post_date) 
      VALUES (%s, %s, %s, %s)
      """
now = datetime.now()
formatted_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
val = ("Python PCAP", "Chen Data vao bang", "BKACAD", formatted_datetime)
mycursor.execute(sql, val)
mydb.commit()
# disconnect from MySQL
mydb.close()
