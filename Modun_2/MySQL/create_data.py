# create connection to MySQL
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""

)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE  IF NOT EXISTS datasql")
# disconnect from MySQL
mydb.close()