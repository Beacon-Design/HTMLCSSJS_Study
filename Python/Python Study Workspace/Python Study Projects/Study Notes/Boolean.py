print('''\
__________________________________________________________

A    and    B               is        Entire statement
True    and    True         is        True
True    and    False        is        False
False   and    True         is        False
False   and    False        is        False

__________________________________________________________

A    or    B                is        Entire statement
True    or    True          is        True
True    or    False         is        True
False   or    True          is        True
False   or    False         is        False

__________________________________________________________

not A                       is        Entire statement
not True                    is        False
not False                   is        True

__________________________________________________________
''')

print('''
--------------------------------
>>> 'a' == ('a' or 'b')                       # ('a' or 'b') return 'a'
True
>>> 'b' == ('a' or 'b')
False
>>> 'a' == ('a' and 'b')                      # ('a' and 'b') return 'b'
False 
>>> 'b' == ('a' and 'b')
True
--------------------------------
>>> 'a' == 'a' or 'a' == 'b'                        # True or False
True
>>> 'b' == 'a' or 'b' == 'b'                        # False or True
True
>>> 'a' == 'a' and 'a' == 'b'                       # True and False
False
>>> 'b' == 'a' and 'b' == 'b'                       # False and True
False
---------------------------------------------------------------------

---When the Python interpreter looks at an or expression, it 
takes the first statement and checks to see if it is true. If 
the first statement is true, then Python returns that object's 
value without checking the second statement;if the first value 
is evaluated as false Python checks the second half and returns 
that value---

---Similarly, for an and expression, Python uses a short circuit 
technique to speed truth value evaluation. If the first statement 
is false then the whole thing must be false, so it returns that 
value. Otherwise if the first value is true it checks the second 
and returns that value.---

---------------------------------------------------------------------

''')

print(bool("a"))
print('''
_________________________________________________________________

True                                   False
1                                      0
Numbers other than zero                The string 'None'
Nonempty strings                       Empty strings
Nonempty lists                         Empty lists
Nonempty dictionaries                  Empty dictionaries
_________________________________________________________________

''')
print(bool(False))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(None))

print(bool([]!=""))
print(bool([]!=False))




