#!C:\Program Files\Python37\python
def calculate(a,b,op):
 
  if(op=='Addition'):
    print("sum is",int(a)+int(b))

  elif(op=='subtraction'):
    print("sub is",int(a)-int(b))

  elif(op=='multiplication'):
    print("mul is",int(a)*int(b))

  elif(op=='modulus'):
    print("mul is",int(a)%int(b))

import cgi
print  ("content-type:text/html\n")
print("<html>")
print("<head> <title>My Second cgi program</title>")
print("</head>")
print("<body>")
form=cgi.FieldStorage()
a=form.getvalue("first")
a=form.getvalue("second")
op=form.getvalue("opeartion")
print('<form method="post" action="1.py">')
print('<p>enter first number: <input type="text" name="first"/></p>')
print('<p>enter second number: <input type="text" name="second"/></p>')
print('<p>select opeartion:</p><select name="opration"><option>Addition</option><option>Subtraction</option><option>multiplication</option><option>modulus</option></select>')
print('<input type="submit" value="submit"/>')
print('<br>')
print('<br>')
print("</body>")
print("</html>")

print("\n")

 

