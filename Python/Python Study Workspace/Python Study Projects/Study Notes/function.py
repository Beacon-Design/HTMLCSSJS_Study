print('''------dir function--------------------------------------------------
dir function lists variables assigned in th caller's scope when
called with no argument.it returns a list of all the attributes
available for any object passed to it.


''')
print(dir())
a=12
print(dir())
def _def_x_():
    return
print(dir())
import random
print(dir())
del a
print(dir())
print()
print('''
A note on del - this statement is used to delete a variable/name 
and after the statement has run, in this case del a, you can no 
longer access the variable a - it is as if it never existed 
before at all.
''')
x = "string"
for i in dir(x):
    print(i)

print()
print(dir(dict))

print("\n\n------Recursion--------------------------------------------------------")
def factorial(n):
    result = n
    for i in range(1,n):
        result = result*i
    return result

def factorial1(n):
    if n == 1:
        return 1
    else:
        return n*factorial1(n-1) 