import mysql.connector
# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "testmysql"
    )
mycursor = mydb.cursor()
sql_string = """CREATE TABLE IF NOT EXISTS testmysql_posts (
                ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                post_author VARCHAR(255),
                post_title TEXT,
                post_content TEXT,
                post_date DATETIME
                )
                """
mycursor.execute(sql_string)
# disconnect from MySQL
mydb.close()
