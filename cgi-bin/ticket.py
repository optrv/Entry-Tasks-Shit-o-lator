#!/usr/bin/env python3
import cgi

# Get a number of the ticket
field = cgi.FieldStorage()
number = field.getfirst("number","")

print("Content-type: text/html")
print("<meta charset=\"utf-8\">")
print()
print("<style>h1,p{text-align:center;}</style>")

# Check whether the ticket is a lucky
def if_lucky(num):
    counter, sum1, sum2 = 0, 0, 0
    for n in num:
        if counter < 3:
            sum1 += int(n)
        else:
            sum2 += int(n)
        counter += 1
    if sum1 == sum2:
        print("<br><h1>{} - is happy ticket!<br>Congrats! ;)</h1>".format(number))
        print("<p><a href='javascript:window.location = document.referrer;'>Try again!</a><br>or<br>")
        print("<a href='/'>Go the main menu</a></p>")
    else:
        print("<br><h1>{} - isn't happy ticket... Sorry. :[</h1>".format(number))
        print("<p><a href='javascript:window.location = document.referrer;'>Try again!</a><br>or<br>")
        print("<a href='/'>Go the main menu</a></p>")
        
# Check whether the number of the ticket is correct
if len(number) == 6 and number.isdigit():
    if_lucky(number)
else:
    print("<br><h1>Please, input 6 digits!</h1>")
    print("<p><a href='javascript:window.location = document.referrer;'>Try again!</a><br>or<br>")
    print("<a href='/'>Go the main menu</a></p>")
