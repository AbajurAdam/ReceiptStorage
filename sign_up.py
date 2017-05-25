#!C:\Users\Ergan\AppData\Local\Programs\Python\Python36-32\python
# sign_up

import conf
import cgi
print("Content-type: text/html\r\n\r\n")
form = cgi.FieldStorage()
usn = form.getvalue('username')
pw = form.getvalue('password')
mail = form.getvalue('mail')
if not str(usn) or str(pw) or str(mail):
    x = '{"result": false}'
    print(x)


conf.curs.execute("insert into user (user_name,password,mail) values('" +
                  str(usn) + "','" + str(pw) + "','" + str(usn) + "')")
