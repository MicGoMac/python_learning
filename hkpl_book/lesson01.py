#!/usr/bin/

'''
from book page 25 
'''

#variables. id() shows the memory location
a=b=c=5
id(a)
id(b)
id(c)
#above gives same result
a=6
id(a)
#result diff, as a now using another memory location

#keywords cannot be used as var name. keyword list is available like this:
import keyword
print(keyword.kwlist)
#['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
