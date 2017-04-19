print('''\

------Variable Scope------
 
Just like the values in our program's variables are forgotten 
after the program ends, variables created inside the function 
are forgotten after the execution leaves the function. Not only 
that, but when execution is inside the function, we cannot change 
the variables outside of the function, or variables inside other 
functions. The variable's scope is this range that variables can
be modified in. The only variables that we can use inside a 
function are the ones we create inside of the function (or the 
parameter variables, described later). That is, the scope of the 
variable is inside in the function's block. The scope of variables
created outside of functions is outside of all functions in the program.
    
 
Not only that, but if we have a variable named spam created outside 
of a function, and we create a variable named spam inside of the 
function, the Python interpreter will consider them to be two separate
variables. That means we can change the value of spam inside the 
function, and this will not change the spam variable that is outside 
of the function. This is because these variables have different scopes,
the global scope and the local scope.


------Global Scope and Local Scope------

We have names for these scopes. The scope outside of all functions is 
called the global scope. The scope inside of a function is called the 
local scope. The entire program has only one global scope, and each 
function has a local scope of its own. Scopes are also called namespaces.


Variables defined in the global scope can be read outside and inside 
functions, but can only be modified outside of all functions. Variables 
defined in a function's local scope can only be read or modified inside
that function.

Specifically, we can read the value of global variables from the local 
scope, but attempting to change the value in a global variable from the 
local scope will leave the global variable unchanged. What Python actually 
does is create a local variable with the same name as the global variable. 
But Python will consider these to be two different variables.

Also, global variables cannot be read from a local scope if you modify 
that variable inside the local scope. For example, if you had a variable 
named spam in the global scope but also modified a variable named spam in 
the local scope (say, with an assignment statement) then the name "spam" 
can only refer to the local scope variable.


------THE PROBLEM OF SHADOWING-------------------------------------------------
Reading the value of global variables is not a problem in general, but one thing 
may make it problematic. If a local variable or parameter exists with the same 
name as the global variable you want to access, you can't do it directly. The 
global variable is shadowed by the local one.
If needed, you can still gain access to the global variable by using the function 
globals, a close relative of vars, which returns a dictionary with the global 
variables. (locals returns a dictionary with the local variables.)

>>> x = 1
>>> def change_global():
global x
x = x + 1
>>> change_global()
>>> x
2



''')

print("#01")
def _a():
    x=99
    print(x)
x=42
print(x)
_a()
print(x)
print()




print("#02")
def _sayhello(name):
    print("Hello! "+name)
print("Hello! Jay!")
Alice="Bob"
_sayhello(Alice)
_sayhello("Tom")
print('''\

The value in the Alice variable and the string 'Tom' are arguments. 
The name variable in _sayHello() is a parameter. The difference between 
arguments and parameters is that arguments are the values passed in a 
function call, and parameters are the local variables that store the 
arguments. It might be easier to just remember that the thing in between 
the parentheses in the def statement is an parameter, and the thing in 
between the parentheses in the function call is an argument.

''')
#local namespace -> global namespace -> build-in namespace
    

    