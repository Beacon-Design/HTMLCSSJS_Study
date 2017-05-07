#!/usr/bin/evn python3
# coding:utf-8

def forList():
    s = 0
    x = 1
    for item in [1, 2, 3, 4]:
        s = s + item
        x *= item
    print(s, x)  # s is 10, x is 24
print('List: ')
forList()


def forStringTuple():
    s = 'Good!!'
    t = ('How', 'are', 'you', '?')
    for i in s: print(i, end=' ')       # Iterate over a string
    for i in t: print(i, end=' ')       # Iterate over a tuple
    print()
    print()
print('String Tuple: ')
forStringTuple()


def forListTuple():
    LT = [(1,2),(3,4),(5,6)]
    for (a,b) in LT:            # Tuple assignment at work
        print(a,b)
print('List Tuple: ')
forListTuple()


def forListTupleAssign():
    T = [(1,2),(3,4),(5,6)]
    for both in T:
        a, b = both         # assign manually within the loop to unpack
        print(a, b)
print('List Tuple Assign Manually: ')
forListTupleAssign()


def forDict():
    D = {'a':1, 'b':2, 'c':3, 'd':4}
    for key in D:                    # Use dict keys iterator and index
        print(key, D[key])

    print(list(D.items()))           # using the items method

    for (key, value) in D.items():   # Iterate over both keys and values
        print(key, value)
print('Dictionary:')
forDict()


def NestedStructures():
    ((a, b),c) = ((10, 20), 30)    # Nested sequences work
    print(a,b,c)
    for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
        print(a, b, c)
    for ((a, b), c) in [([21, 22], 23),['XY', 'Z']]:
        print(a, b, c)
print(('Nested Structures: '))
NestedStructures()


def forExtendedSequenceAssignment():
    a, *b, c = (10, 20, 30, 40)              # starred names always are assigned lists
    print(a, b, c)
    for (a, *b, c ) in [(1, 2, 3, 4), (5, 6, 7, 8)]: # in Python 3.X
        print(a, b, c)

    for all in [(51, 52, 53 ,54),(55, 56, 57, 58)]:  # in Python 2.X
        a, b, c = all[0], all[1:3], all[3]           # slicing returns a type-specific result
        print(a, b, c)
print('Extended Sequence Assignment: ')
forExtendedSequenceAssignment()