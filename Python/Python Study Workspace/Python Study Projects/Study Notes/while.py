print('''
-------------------------------------------------------------------------

The while statement allows you to repeatedly execute a block of 
statements as long as a condition is true. A while statement is 
an example of what is called a looping statement. A while statement 
can have an optional else clause

The else block is executed when the while loop condition becomes 
False - this may even be the first time that the condition is checked. 
If there is an else clause for a while loop, it is always executed 
unless you break out of the loop with a break statement

-------------------------------------------------------------------------

"return" may only occur syntactically nested in a function definition,
not within a nested class definition.

Notice that the condition for the while loop is simply the Boolean 
value True. That means the only way execution will ever leave this 
loop is by executing a break statement (which leaves the loop) or 
a return statement (which leaves the entire function). Such a loop 
is called an infinite loop, because it will loop forever (unless it 
reaches a break statement)

-------------------------------------------------------------------------
''')
def a():
    while True:
        print("loop")
        return        
a()

print('''
---------------------------------------------------------------------
''')

m = 1
while m < 3:
    print(m)
    m = m+1
else:
    print("done")
    
print('''----------------------------------------------------------------------
empty string evaluates to false.
a string with one space character is not empty,not false.

''')
name = '' # (empty string)
while not name:    
    print("empty string")
    break

name_1 = ' ' # (space character)
while not name_1 or name_1.isspace():
    print("space character_V1")
    break

while not name.strip():
    print("space character_V2")
    break
    

print('''======while true/break================================================
''')
    
# V1
# word = "dummy value"
# while word:
#     word = input("Enter a word: ")
#     print("'dummy value' version",word)

# V2
# word = input("Enter a word: ")
# while word:
#     print(word)
#     word = input("Enter a word: ")
    
# V3
while True:
    word = input("Enter a word: ")
    if not word:
        break
    print("'while True/break' version",word)










