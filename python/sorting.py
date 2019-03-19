#!C:\Program Files\Python37\python
def String(a):
    words=a.split()
    words.sort()
    x=" ".join(words)
    print(x)




import cgi
print("Context-type:text/html\n")
print("<html>")
print("<head> <title> My first CGI program </title>")
print("</head>")
print("<body>")
form=cgi.FieldStorage()
a=form.getvalue("String")
#!print('<h1> Hello'+name+'Thanks for using my screen!</h1><br/>')
print("<form method=""post"" action='Sort.py'>")
print('<p>Enter the String: <input type="text" name="String"/></p>')
print('<input type="submit" value="submit"/>')
print('<br>')
print('<br>')
print('</body>')
print("</html>")
print("\n")
       
String(a)
