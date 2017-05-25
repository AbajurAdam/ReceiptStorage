#!C:\Users\Ergan\AppData\Local\Programs\Python\Python36-32\python
import MySQLdb
# config file for database connection
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="receiptstorage")
curs = db.cursor()
