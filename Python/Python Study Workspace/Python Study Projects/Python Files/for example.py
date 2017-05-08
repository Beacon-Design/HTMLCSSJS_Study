#!/usr/bin/evn python3
# coding:utf-8

def forList():
    s = 0
    x = 1
    for item in [1, 2, 3, 4]:
        s = s + item
        x *= item
    print(s, x)  # s is 10, x is 24
print('\nList: ')
forList()


def forStringTuple():
    s = 'Good!!'
    t = ('How', 'are', 'you', '?')
    for i in s: print(i, end=' ')       # Iterate over a string
    for i in t: print(i, end=' ')       # Iterate over a tuple
    print()
    print()
print('\nString Tuple: ')
forStringTuple()


def forListTuple():
    LT = [(1,2),(3,4),(5,6)]
    for (a,b) in LT:            # Tuple assignment at work
        print(a,b)
print('\nList Tuple: ')
forListTuple()


def forListTupleAssign():
    T = [(1,2),(3,4),(5,6)]
    for both in T:
        a, b = both         # assign manually within the loop to unpack
        print(a, b)
print('\nList Tuple Assign Manually: ')
forListTupleAssign()


def forDict():
    D = {'a':1, 'b':2, 'c':3, 'd':4}
    for key in D:                    # Use dict keys iterator and index
        print(key, D[key])

    print(list(D.items()))           # using the items method

    for (key, value) in D.items():   # Iterate over both keys and values
        print(key, value)
print('\nDictionary:')
forDict()


def NestedStructures():
    ((a, b),c) = ((10, 20), 30)    # Nested sequences work
    print(a,b,c)
    for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
        print(a, b, c)
    for ((a, b), c) in [([21, 22], 23),['XY', 'Z']]:
        print(a, b, c)
print('\nNested Structures: ')
NestedStructures()


def forExtendedSequenceAssignment():
    a, *b, c = (10, 20, 30, 40)              # starred names always are assigned lists
    print(a, b, c)
    for (a, *b, c ) in [(1, 2, 3, 4), (5, 6, 7, 8)]: # in Python 3.X
        print(a, b, c)

    for all in [(51, 52, 53 ,54),(55, 56, 57, 58)]:  # in Python 2.X
        a, b, c = all[0], all[1:3], all[3]           # slicing returns a type-specific result
        print(a, b, c)
print('\nExtended Sequence Assignment: ')
forExtendedSequenceAssignment()


def NestedForLoops():
    itemList = ['aaa', 111, (4, 5), 2.01]       # A set of objects
    keyToSearch = [(4, 5), 3.14]                # Keys to search for

    for key in keyToSearch:                     # For all keys
        for item in itemList:                   # For all items
            if item == key:                     # Check for match
                print(key, 'was found')
                break
        else:
            print(key, 'not found')
print('\nNested for loops: ')
NestedForLoops()


def forInLoops():
    itemList = ['aaa', 111, (4, 5), 2.01]  # A set of objects
    keyToSearch = [(4, 5), 3.14]  # Keys to search for

    for key in keyToSearch:
        if key in itemList:
            print(key, 'was found')
        else:
            print(key, 'not found!')
print("\nfor in loops: ")
forInLoops()


def forIntersection():
    seq1 = 'spam'
    seq2 = 'scam'
    res = []

    for x in seq1:
        if x in seq2:
            res.append(x)
    print(res)
print('\nfor insection: ' )
forIntersection()


# repeat an action a specific number of times.
def forRange():
    for i in range(3):
        print(i, 'python')
print('\nrepeat an action a specific number of times: for range')
forRange()


# shuffle a list, Works on any sequence type
def forShuffleAList():
    L = [1, 2, 3]
    for i in range(len(L)):     # Works on any sequence type
        x = L[i:] + L[:i]
        print(x, end=' ')
print('\nshuffle a list: ')
forShuffleAList()


# Nonexhaustive Traversals range
def skipItems01():
    S = 'abcdefghijk'
    for i in range(0, len(S), 2):
        print(S[i], end=' ')
print('\nNonexhaustive Traversals range skip items:')
skipItems01()


# Nonexhaustive Traversals slice
def skipItems02():
    S = 'abcdefghijk'
    for c in S[::2]:        # slicing makes a copy of the string in both 2.X and 3.X
        print(c, end=' ')
print('\nNonexhaustive Traversals slice skip items: ')
skipItems02()