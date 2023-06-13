import mysql.connector
# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "testmysql"
    )
mycursor = mydb.cursor()
sql = """INSERT INTO testmysql_posts (post_author, post_title, post_content, 
post_date) 
      VALUES ("Python PCAP", "Ket noi Python voi MySQL", "BKACAD", now())
      """
mycursor.execute(sql)
mydb.commit()
# disconnect from MySQL
mydb.close()
