#!/usr/bin/env python
import cgi

print ('Content-type:text/html\n\n')
print ("<html>\n<body>")
print ("<div style=\"width: 100%; font-size: 40px; font-weight: bold; text-align: center;\">")
print ("zhang tie html zai zhe</div>")
form = cgi.FieldStorage()
if form.getvalue('html'):
        html = form.getvalue('html')

print ("\n</body>\n</html>")
