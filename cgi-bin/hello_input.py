#!/usr/bin/env python3
import cgi

# Get the digits
field = cgi.FieldStorage()
name = field.getfirst("name","")

print("Content-type: text/html")
print("<meta charset=\"utf-8\">")
print()
print("<style>h1,p{text-align:center;}</style>")

if name !="" and name.isalpha():
    print("<br><h1>Hello, {}!</h1>".format(name))
    print("<p><a href='/'>Go to the main menu</a></p>")
else:
    print("<br><h1>Please, input your name!</h1>")
    print("<p><a href='javascript:window.history.back()'>Try again!</a><br>or<br>")
    print("<a href='/'>Go the main menu</a></p>")


