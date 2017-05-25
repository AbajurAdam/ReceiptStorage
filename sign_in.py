#!C:\Users\Ergan\AppData\Local\Programs\Python\Python36-32\python
import conf
import cgi
import cgitb
import json
import requests


# python3 best !
# Paladins gey
# url = "http://localhost/mysql.py"
form = cgi.FieldStorage()
usn = form.getvalue('username')
pw = form.getvalue('password')
id = conf.curs.execute("select id from user where user_name='" +
                       str(usn) + "' and password='" + str(pw) + "'")
r = conf.curs.fetchall()

print("Content-type: text/html\r\n\r\n")
if not r:
    x = '{"result": false}'
    print(x)

else:
    for row in r:
        x = '{"result":' + str(row[0]) + '}'
        print(x)
