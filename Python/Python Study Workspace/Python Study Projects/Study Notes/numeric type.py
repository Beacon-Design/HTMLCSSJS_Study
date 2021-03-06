print('''------A complete inventory of Python's numeric toolbox includes------
Integer and floating-point objects
Complex number objects
Decimal: fixed-precision objects
Fraction: rational number objects
Sets: collections with numeric operations
Booleans: true and false
Built-in functions and modules: round, math, random, etc.
Expressions; unlimited integer precision; bitwise operations; hex, octal, and binary formats
Third-party extensions: vectors, libraries, visualization, plotting, etc.

''')

print('''
Literal                                       Interpretation
1234, -24, 0, 99999999999999                  Integers (unlimited size)
1.23, 1., 3.14e-10, 4E210, 4.0e+210           Floating-point numbers
0o177, 0x9ff, 0b101010                        Octal, hex, and binary literals in 3.X
0177, 0o177, 0x9ff, 0b101010                  Octal, octal, hex, and binary literals in 2.X
3+4j, 3.0+4.0j, 3J                            Complex number literals
set('spam'), {1, 2, 3, 4}                     Sets:2.X and 3.X construction forms
Decimal('1.0'), Fraction(1, 3)                Decimal and fraction extension types
bool(X),True,False                            Boolean type and constants

Integer and floating-point literals
Integers are written as strings of decimal digits. Floating-point numbers have a
decimal point and/or an optional signed exponent introduced by an e or E and
followed by an optional sign. If you write a number with a decimal point or exponent,
Python makes it a floating-point object and uses floating-point (not integer)
math when the object is used in an expression. Floating-point numbers are implemented
as C "doubles" in standard CPython, and therefore get as much precision
as the C compiler used to build the Python interpreter gives to doubles.


Integers in Python 2.X: normal and long
In Python 2.X there are two integer types, normal (often 32 bits) and long (unlimited
precision), and an integer may end in an l or L to force it to become a long
integer. Because integers are automatically converted to long integers when their
values overflow their allocated bits, you never need to type the letter L yourself-
Python automatically converts up to long integer when extra precision is needed.


Integers in Python 3.X: a single type
In Python 3.X, the normal and long integer types have been merged-there is only
integer, which automatically supports the unlimited precision of Python 2.X's separate
long integer type. Because of this, integers can no longer be coded with a
trailing l or L, and integers never print with this character either. Apart from this,
most programs are unaffected by this change, unless they do type testing that
checks for 2.X long integers.


Hexadecimal, octal, and binary literals
Integers may be coded in decimal (base 10), hexadecimal (base 16), octal (base 8),
or binary (base 2), the last three of which are common in some programming domains.
Hexadecimals start with a leading 0x or 0X, followed by a string of hexadecimal
digits (0-9 and A-F). Hex digits may be coded in lower- or uppercase. Octal
literals start with a leading 0o or 0O (zero and lower- or uppercase letter o), followed
by a string of digits (0-7). In 2.X, octal literals can also be coded with just a leading
0, but not in 3.X-this original octal form is too easily confused with decimal, and
is replaced by the new 0o format, which can also be used in 2.X as of 2.6. Binary
literals, new as of 2.6 and 3.0, begin with a leading 0b or 0B, followed by binary
digits (0-1).
Note that all of these literals produce integer objects in program code; they are just
alternative syntaxes for specifying values. The built-in calls hex(I), oct(I), and
bin(I) convert an integer to its representation string in these three bases, and
int(str, base) converts a runtime string to an integer per a given base.


Complex numbers
Python complex literals are written as realpart+imaginarypart, where the imagi
narypart is terminated with a j or J. The realpart is technically optional, so the
imaginarypart may appear on its own. Internally, complex numbers are implemented
as pairs of floating-point numbers, but all numeric operations perform
complex math when applied to complex numbers. Complex numbers may also be
created with the complex(real, imag) built-in call.


Coding other numeric types
As we'll see later in this chapter, there are additional numeric types at the end of
Table 5-1 that serve more advanced or specialized roles. You create some of these
Numeric Type Basics | 135
by calling functions in imported modules (e.g., decimals and fractions), and others
have literal syntax all their own (e.g., sets).

''')