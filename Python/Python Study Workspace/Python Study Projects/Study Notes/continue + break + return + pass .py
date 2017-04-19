# coding=utf-8

print('''=======================================================================
a loop simply executes a block until its condition becomes false, or until it 
has used up all sequence elements. But sometimes you may want to interrupt the 
loop, to start a new iteration (one "round" of executing the block), 
or to simply end the loop
''')



print('''------The Continue Statement-------------------------------------------------
The continue statement is used to tell Python to skip the rest of 
the statements in the current loop block and to continue to the next 
iteration of the loop.


''')
a="this is a string"
for i in a:
    if i == "s":
        continue
    print(i,end="")

print()
print()
print('''------The Break Statement----------------------------------------------

The break statement is used to break out of a loop statement i.e. 
stop the execution of a looping statement, even if the loop condition 
has not become False or the sequence of items has not been completely 
iterated over.

An important note is that if you break out of a for or while loop, 
any corresponding loop else block is not executed


''')
a="this is a string"
for i in a:
    if i == "s":
        break
    print(i,end="")
print()
print()
print('''------The Return Statement---------------------------------------------

The return statement is used to return from a function i.e. break out of 
the function. We can optionally return a value from the function as well.

Note that a return statement without a value is equivalent to return None. 
None is a special type in Python that represents nothingness. For example, 
it is used to indicate that a variable has no value if it has a value of 
None.

_________________________________________________________________________________

"return" may only occur syntactically nested in a function definition,
not within a nested class definition.

Notice that the condition for the while loop is simply the Boolean 
value True. That means the only way execution will ever leave this 
loop is by executing a break statement (which leaves the loop) or 
a return statement (which leaves the entire function). Such a loop 
is called an infinite loop, because it will loop forever (unless it 
reaches a break statement)

''')
def a():
    while True:
        print("loop,return")
        return        
a()
print()


print('''------Pass--------------------------------------------------------
The pass statement is used in Python to indicate an empty block of statements.

''')
def some_function():
    pass

