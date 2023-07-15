#!/usr/bin/

'''
from book chapter 2, page 25 
'''

#1. variables. id() shows the memory location
a=b=c=5
id(a)
id(b)
id(c)
#above gives same result
a=6
id(a)
#result diff, as a now using another memory location

#2.keywords cannot be used as var name. keyword list is available like this:
import keyword
print(keyword.kwlist)
#['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#3. datatypes : str, int, float, bool, none
#get the type of a var:
price=3.4
print( type(price))
#or
print( "price is ", type(price))

#mutable and immutable datatype(p.27)


