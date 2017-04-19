print('''
------immutable-------------------------------------------
------sequence(in,not in expression)(index)(slice)-------

print always ends with an invisible "new line" character

''')
print("---#01------x.format()-------------------------------------------")
print("python 3 code")
#n=12
print("this is a {} string".format(12))

print("this is {0} and {1} = {2}".format(1,2,3))
print()
print("python 2 code")
print("this is a %s string"%12)
print('%s, eggs, and %s' % ('spam', 'SPAM!'))
print('%d %s %g you' % (1, 'spam', 4.0),"\n\n")


print('''
------String formatting type codes-----------------------------------------------------------

Code    Meaning
s       String (or any object's str(X) string)
r       Same as s, but uses repr, not str
c       Character (int or str)
d       Decimal (base-10 integer)
i       Integer
u       Same as d (obsolete: no longer unsigned)
o       Octal integer (base 8)
x       Hex integer (base 16)
X       Same as x, but with uppercase letters
e       Floating point with exponent, lowercase
E       Same as e, but uses uppercase letters
f       Floating-point decimal
F       Same as f, but uses uppercase letters
g       Floating-point e or f
G       Floating-point E or F
%       Literal % (coded as %%)

%[(keyname)][flags][width][.precision]typecode

*  Provide a key name for indexing the dictionary used on the right side of the expression

*  List flags that specify things like left justification (-), numeric sign (+), a blank before
positive numbers and a - for negatives (a space), and zero fills (0)

*  Give a total minimum field width for the substituted text

*  Set the number of digits (precision) to display after a decimal point for floatingpoint
numbers


''')


print()

print("---#02------Raw String:----------------------------------------------")
print("--------------------by prefixing r or R to the string-------------")
print(r'''
NOTE:Always use raw strings when dealing with regular expressions. 
Otherwise, a lot of backwhacking may be required. For example, 
backreferences can be referred to as '\\1' or r'\1'.

''')

S = 'A\0B\0C'
print(len(S))
# \0, a binary zero byte, does not terminate string
print(S)

print("12345",end="abc")
print(r'''
end=""---->string appended after the last value,
           default a new line
''')
print(r""" ''' three single-quotes:
Within the multi-line string, 
Python ignores the indentation rules it 
normally has for where blocks end;
 ' and " are free to use in three single-quotes    
""")



print(r'''
Escape Character       Actually Printed 
\                       
\\                      \
\'                      '
\"                      "
\n                      newline   
\t                      tab
\a                      Bell
\b                      Backspace
\f                      Formfeed
\r                      Carriage return
\v                      Vertical tab
\xhh                    Character with hex value hh (exactly 2 digits)
\ooo                    Character with octal value ooo (up to 3 digits)
\0                      Null: binary 0 character (doesn't end string)
\N{ id }                Unicode database ID
\uhhhh                  Unicode character with 16-bit hex value
\Uhhhhhhhh              Unicode character with 32-bit hex valuea
\other                  Not an escape (keeps both \ and other) 


The \Uhhhh... escape sequence takes exactly eight hexadecimal digits (h); 
both \u and \U are recognized only in Unicode string literals
in 2.X, but can be used in normal strings (which are Unicode) in 3.X. 
In a 3.X bytes literal, hexadecimal and octal escapes denote the byte
with the given value; in a string literal, these escapes denote a Unicode 
character with the given code-point value


''')
s1 = b"a\0b\0c"
print(s1,len(s1))
s2 = b"\001\002\x03"
print(s2,len(s2),"\n\n")





print("---#03------ .replace/ -------------------------------------------")
print("boo".replace("oo","xx"))
print("------changing string---------------------------------------------")
X = "spam"
X = X + "SPAM!"
print(X)
X = X[:4] + "Burger" +X[-1]
print(X,"\n\n")

print("---#04------ .lower()/ .upper()/ .reverse()/ .split()/ .isalpha()--------------------------------\n")
print("String".lower())
print("String".upper())
a = "String"
print(a.upper())
b=[1,2,3,"book","egg"]

b.reverse()
print(b)

c = "ant baboon bager bat bear beaver".split()
print(c)
d = "a,s,d,f,g,h,"
d.split(",")
print(d,"\n")
# The "split" occurs wherever a space occurs in the string.

print("big".isalpha())
print("big1".isalpha(),"\n")
# S.isalpha() -> bool 
# Return True if all characters in S are alphabetic
# and there is at least one character in S, False otherwise.

print("---#05------ .startswith()/ in/ .find()/ .replace()/ .join-------------------------\n")

name = "apple"
if name.startswith("app"):
    print("name.startswith 'app' ")
#      S.startswith(prefix[, start[, end]]) -> bool
#  |      
#  |      Return True if S starts with the specified prefix, False otherwise.
#  |      With optional start, test S beginning at that position.
#  |      With optional end, stop comparing S at that position.
#  |      prefix can also be a tuple of strings to try.

if "a" in name:
    print(" 'a' in name")
    # The in operator is used to check if a given string is 
    # a part of the string

if name.find("pp") != -1:
    print(name.find("pp"))
    print("pp in name")
    # it returns the offset of the passed-in substring, 
    # or -1 if it is not present

newname = name.replace("pp","XX")
print(name)
print(newname)   
    # S.replace(old, new[, count]) -> str
    # Return a copy of S with all occurrences of substring
    # old replaced by new.If the optional argument count is
    # given, only the first count occurrences are replaced
    

delimiter = '_'
mylist = ["a","b","c"]
print(delimiter.join(mylist),"\n\n")
#  join the items of a sequence with the string acting as a 
#  delimiter between each item of the sequence and returns a 
#  bigger string generated from this


print("------ ord()/ chr()---------------------------------")
print(ord("a"))
print(chr(97))

print("\n____________________________________________________________________________")
print('''\n______(immutable)______________________________________________________
you can't change a string by assigning to one of its
positions, but you can always build a new one and assign it to 
the same name
''')
print("------#01---(slice)---------------------------------------------------------")
s = "apple"
n = "x"+ s[1:]
print(n,"\n")

print("------#02---(list;join)---------------------------------------------------------")
w1 = "book"
k1 = list(w1)
print(k1)
k1[1] = "x"
print(k1)
p1 = "".join(k1)
print(p1) 

print("------#03---(bytearray)--------------------------------------------------------")
m1 = bytearray(b"book")
print(type(m1),m1)
m1.extend(b"egg")
print(m1)
n1 = m1.decode()
print(n1)
print('''
The bytearray supports in-place changes for text, but only for text whose characters
are all at most 8-bits wide (e.g., ASCII). All other strings are still immutable-bytear
ray is a distinct hybrid of immutable bytes strings (whose b'...' syntax is required in
3.X and optional in 2.X) and mutable lists (coded and displayed in [])


''')
      

print('''------exec---------------------------------------------------------------
------The statement for executing a string is exec-----------------------------

The exec statement is mainly useful when you build the code string on the fly. 
And if the string is built from parts that you get from other places, and 
possibly from the user, you can rarely be certain of exactly what it will contain. 
So to be safe, you give it a dictionary, which will work as a namespace for it.

''')
exec ("print('hi')")

from math import sqrt
scope = {}
exec ("sqrt = 4",scope)
print(sqrt(9))
print(scope['sqrt'])

print('''------eval-------------------------------------------------------------
------A built-in function that is similar to exec is eval (for "evaluate").-----
''')
print(eval("1+1")) 

































