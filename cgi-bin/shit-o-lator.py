#!/usr/bin/env python3
import cgi

# Get the digits
field = cgi.FieldStorage()
dig1 = field.getfirst("dig1","")
dig2 = field.getfirst("dig2","")
oper = field.getvalue("oper","")

print("Content-type: text/html")
print("<meta charset=\"utf-8\">")
print()
print("<style>h1,p{text-align:center;}</style>")

# Check the zero
def zero_check(dig2):
    if oper == '/' and dig2 == '0':
        print("<br><h1>You can't divide on zero!</h1>")
        print("<p><a href='javascript:window.history.back()'>Try again!</a><br>or<br>")
        print("<a href='/'>Go the main menu</a></p>")
        return False
    else:
        return True

# Check the digits
def digit_check(dig, dig2):
    if zero_check(dig2):
        try:
            float(dig)
            float(dig2)
            return (True)
        except (ValueError):
            print("<br><h1>Please, input the digits!</h1>")
            print("<p><a href='javascript:window.history.back()'>Try again!</a><br>or<br>")
            print("<a href='/'>Go the main menu</a></p>")                

# Output the result
def output(summ):
    if summ - int(summ) == 0:
        print("<br><br><h1>The result is: {}</h1>".format(int(summ)))
        print("<p><a href='javascript:window.location = document.referrer;'>Try again!</a><br>or<br>")
        print("<a href='/'>Go to the main menu</a></p>")    
    else:
        print("<br><br><h1>The result is: {0:.2f}</h1>".format(summ))
        print("<p><a href='javascript:window.location = document.referrer;'>Try again!</a><br>or<br>")
        print("<a href='/'>Go to the main menu</a></p>")    

# Calculate the digits
if digit_check(dig1,dig2):
    try:
        oper_kind = {'+': float(dig1) + float(dig2),
                    '-': float(dig1) - float(dig2),
                    '*': float(dig1) * float(dig2),
                    '/': float(dig1) / float(dig2)}
        for n in oper_kind:
            if n == oper:
                summ = oper_kind[n]
                output(summ)
    except (ZeroDivisionError):
        oper_kind = {'+': float(dig1) + float(dig2),
                    '-': float(dig1) - float(dig2),
                    '*': float(dig1) * float(dig2)}
        for n in oper_kind:
            if n == oper:
                summ = oper_kind[n]
                output(summ)
