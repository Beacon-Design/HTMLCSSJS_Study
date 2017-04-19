#coding=utf-8

print('''
------ Variables ---------------------------------------------------------------

a variable is something which can change. A variable is a way of referring to a 
memory location used by a computer program. A variable is a symbolic name for 
this physical location. This memory location contains values, like numbers, text
or more complicated types. We can use this variable to tell the computer save 
some data in this location or to retrieve some data from this location.

A variable can be seen as a container (or some say a pigeonhole) to store certain
values. While the program is running, variables are accessed and sometimes changed. 
a new value will be assigned to a variable. 

Another remarkable aspect of Python: Not only the value of a variable may change 
during program execution but the type as well. You can assign an integer value 
to a variable, use it as an integer for a while and then assign a string to the 
same variable. 







----Constant Variables----

HANGMANPICS = 50
You may have noticed that HANGMANPICS's name is in all capitals. 
This is the programming convention for constant variables. 
Constants are variables whose values do not change throughout the 
program. Although we can change HANGMANPICS just like any other 
variable, the all-caps reminds the programmer to not write code 
that does so.

Constant variables are helpful for providing descriptions for 
values that have a special meaning. Since the multi-string value 
never changes, there is no reason we couldn't copy this multi-line 
string each time we needed that value. The HANGMANPICS variable 
never varies. But it is much shorter to type HANGMANPICS than it 
is to type that large multi-line string.

Also, there are cases where typing the value by itself may not be 
obvious. If we set a variable eggs = 72, we may forget why we were 
setting that variable to the integer 72. But if we define a constant 
variable DOZEN = 12, then we could set eggs = DOZEN * 6 and by just 
looking at the code know that the eggs variable was set to six dozen.

Like all conventions, we don't have to use constant variables, or 
even put the names of constant variables in all capitals. But doing 
it this way makes it easier for other programmers to understand how 
these variables are used. (It even can help you if you are looking 
at code you wrote a long time ago.)


''')

print("01")
print("x is tuple,immutable")
x=(1,2,3)
print(type(x),x)

print("02")
print('x is list,mutable')
x=[1,2,3]
x.append(4)
x.insert(0,9)
print(type(x),x)

print('03')
x='string'
print(type(x),x[2],x[2:4],x[0::2])

print('04')
a=dict(p=18)
b=dict(p=18)
if a==b:
    print("==,compare value")
if a is b:
    print()
else:
    print("is,compare id,mutable")
print()

print('''------Default Argument Values--------------------------------------
Note that the default argument value should be a constant. More precisely, 
the default argument value should be immutable

*** Only those parameters which are at the end of the parameter list can be 
given default argument values ***

''')
def say(message,time=1):
    print(message*time)
say("hi",3)
print()

def func(a, b=5, c=10):
    print(a,b,c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)
print()

print('''------VarArgs parameters--------------------------------------------
Sometimes you might want to define a function that can take any number 
of parameters, i.e. variable number of arguments, this can be achieved 
by using the stars*

When we declare a starred parameter such as *param, then all the 
positional arguments from that point till the end are collected as a 
tuple called param.

Similarly, when we declare a double-starred parameter such as **param, 
then all the keyword arguments from that point till the end are collected 
as a dictionary called param.

''')
def total(initial=5, *numbers, **keywords):
    print(initial)
    a = numbers
    print(a)
    b = keywords
    print(b)

total(10, 1, 2, 3, vegetables=50, fruits=100)
print()

print('''
*param  :  tuple     (*args)
**param :  dictionary      (**kwargs)  
''')


print('''
Variables are created when they are first assigned values
Variables are replaced with their values when used in expressions
Variables must be assigned before they can be used in expressions.
Variables refer to objects and are never declared ahead of time


>>> x = ["Hello", "world"]
>>> y = x
>>> y[1] = "Python"
>>> x
['Hello', 'Python']
>>> del x
>>> y
['Hello', 'Python']


there is no way to delete values in Python—and you don’t really need to,because 
the Python interpreter does it by itself whenever you don’t use the value anymore
''')
    


   
    
    
    
    
    