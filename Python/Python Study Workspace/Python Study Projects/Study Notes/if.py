print('''
if the condition is true, we run a block of statements 
(called the if-block), else we process another block of 
statements (called the else-block). The else clause is optional

''')
print('01')
if True:
    print('true')
print()
if False:
    print("a")
else:
    print('false')
    
print()

choices=dict(
    one='first',
    two='second',
    three='third',
    four='fouth'
    )

v='one'
print(choices[v])

m='ten'
print(choices)
print(choices.get(m,'others'))
print(choices)

print()
print('02')
a,b=1,2
v="true" if a<b else"false"
print(v)


print('''------assertions----------------------------------------------------
------you can require that certain things be true----------------------------

It can be useful to put the assert statement in your program as a checkpoint, 
if you know something must be true for your program to work correctly.
A string may be added after the condition, to explain the assertion:

''')

age = -1
assert 0<age<10,"age must be realistic"


























