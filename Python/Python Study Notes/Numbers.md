# Python Study Notes



# Numbers



## Numeric Type Basics

In Python, numbers are not really a single object type, but a category of similar types.

A complete inventory of Python’s numeric toolbox includes:

- Integer and floating-point objects



- Complex number objects



- Decimal: fixed-precision objects



- Fraction: rational number objects



- Sets: collections with numeric operations


- Booleans: true and false


- Built-in functions and modules: round, math, random, etc.



- Expressions; unlimited integer precision; bitwise operations; hex, octal, and binary formats



- Third-party extensions: vectors, libraries, visualization, plotting, etc.

  ​



## Numeric Literals

```
Numeric literals and constructors

Literal                                       Interpretation
-----------------------------------           ---------------------------------------------
1234, -24, 0, 99999999999999                  Integers (unlimited size)
1.23, 1., 3.14e-10, 4E210, 4.0e+210           Floating-point numbers
0o177, 0x9ff, 0b101010                        Octal, hex, and binary literals in 3.X
0177, 0o177, 0x9ff, 0b101010                  Octal, octal, hex, and binary literals in 2.X
3+4j, 3.0+4.0j, 3J                            Complex number literals
set('spam'), {1, 2, 3, 4}                     Sets:2.X and 3.X construction forms
Decimal('1.0'), Fraction(1, 3)                Decimal and fraction extension types
bool(X), True, False                          Boolean type and constants
```

### 1. Integer and floating-point literals

整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。

浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x $10^2$= 250） 

> **Integers are written as strings of decimal digits.** 
>
> **Floating-point numbers have a decimal point and/or an optional signed exponent introduced by an e or E and followed by an optional sign.**
>
>  If you write a number with a decimal point or expo-nent, Python makes it a floating-point object and uses floating-point (not integer) math when the object is used in an expression. Floating-point numbers are implemented as C “doubles” in standard CPython, and therefore get as much precision as the C compiler used to build the Python interpreter gives to doubles.

Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。

Integers in Python 2.X: normal and long：

> In Python 2.X there are two integer types, normal (often 32 bits) and long (un-limited precision), and an integer may end in an l or L to force it to become a long integer. Because integers are automatically converted to long integers when their values overflow their allocated bits, you never need to type the letter L yourself—Python automatically converts up to long integer when extra precision is needed.

Integers in Python 3.X: a single type：

> In Python 3.X, the normal and long integer types have been merged—there is only integer, which automatically supports the unlimited precision of Python 2.X’s separate long integer type. Because of this, integers can no longer be coded with a trailing l or L, and integers never print with this character either. Apart from this, most programs are unaffected by this change, unless they do type testing that checks for 2.X long integers.

### 2. Hexadecimal, octal, and binary literals

> Integers may be coded in **decimal (base 10)**, **hexadecimal (base 16)**, **octal (base 8)**, or **binary (base 2)**, the last three of which are common in some programming do-mains. 
>
> **Hexadecimals start with a leading 0x or 0X, followed by a string of hexadecimal digits (0–9 and A–F).** Hex digits may be coded in lower- or uppercase. 
>
> **Octal literals start with a leading 0o or 0O (zero and lower- or uppercase letter o), followed by a string of digits (0–7)**. In 2.X, octal literals can also be coded with just a leading 0, but not in 3.X—this original octal form is too easily confused with decimal, and is replaced by the new 0o format, which can also be used in 2.X as of 2.6. 
>
> **Binary literals**, new as of 2.6 and 3.0, **begin with a leading 0b or 0B, followed by binary digits (0–1)**.
>
> Note that all of these literals produce integer objects in program code; they are just alternative syntaxes for specifying values. The built-in calls hex(I), oct(I), and bin(I) convert an integer to its representation string in these three bases, and int(str, base) converts a runtime string to an integer per a given base.

```
binary, octal, decimal, hexadecimal

binary      (base 2)    (0b101010)
a leading 0b or 0B, followed by binary digits (0–1)
------------------------------------------------------

octal       (base 8)    (0o177)3.X    (0177, 0o177)2.X
(3.X) a leading 0o or 0O (zero and lower/uppercase letter o), followed by a string of digits (0–7).
(2.X) can also be coded with just a leading 0.
------------------------------------------------------

decimal     (base 10)
------------------------------------------------------

hexadecimal (base 16)    (0x9ff)
a leading 0x or 0X, followed by a string of hexadecimal digits (0–9 and A–F)
```

我们可以使用十六进制、八进制、二进制来代表整数：

```
>>> 0x01, 0x10, 0xFF  	    # 十六进制 Hex literals: base 16, digits 0-9/A-F (3.X, 2.X)
(1, 16, 255)

>>> 0o1, 0o20, 0o377           # 八进制 Octal literals: base 8, digits 0-7 (3.X, 2.6+)
(1, 16, 255)

>>> 0b1, 0b10000, 0b11111111   # 二进制 Binary literals: base 2, digits 0-1 (3.X, 2.6+)
(1, 16, 255)
```

The F digits in the hex value, for example, each mean 15 in decimal and a 4-bit 1111 in binary, and reflect powers of 16.

```
>>> 0xFF, (15 * (16 ** 1)) + (15 * (16 ** 0)) 	# How hex/binary map to decimal
(255, 255)
>>> 0x2F, (2 * (16 ** 1)) + (15 * (16 ** 0)) 
(47, 47)
>>> 0xF, 0b1111, (1*(2**3) + 1*(2**2) + 1*(2**1) + 1*(2**0)) 
(15, 15, 15)
```

#### convert integers to other bases’ digit strings

```
>>> oct(64), hex(64), bin(64) 		# Numbers=>digit strings
('0o100', '0x40', '0b1000000')
```

#### converts a string of digits to an integer

```
>>> 64, 0o100, 0x40, 0b1000000 				# Digits=>numbers in scripts and strings
(64, 64, 64, 64)

>>> int('64'), int('100', 8), int('40', 16), int('1000000', 2) 
(64, 64, 64, 64)

>>> int('0x40', 16), int('0b1000000', 2)	 # Literal forms supported too 
(64, 64)
```



### 3. Complex numbers

复数( (complex)) - 复数由实数部分(浮点数)和虚数部分(浮点数)构成，并在虚部增加了j或J的后缀。可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点数。

> For example, the complex number with a real part of 2 and an imaginary part of −3 is written 2 + −3j.

> **Python complex literals are written as realpart+imaginarypart, where the imaginarypart is terminated with a j or J. The realpart is technically optional, so the imaginarypart may appear on its own**. Internally, complex numbers are implemented as pairs of floating-point numbers, but all numeric operations perform complex math when applied to complex numbers. Complex numbers may also be created with the complex(real, imag) built-in call.

```
>>> 1j * 1J 
(-1+0j)
>>> 2 + 1j * 3 
(2+3j)
>>> (2 + 1j) * 3 
(6+3j)
```



### 4. Decimal Type 小数数字

the decimal object, formally known as Decimal. decimals are like floating-point numbers, but they have a fixed number of decimal points. Hence, decimals are fixed-precision floating-point values.

> the decimal type is well suited to representing fixed-precision quantities like sums of money and can help you achieve better numeric accuracy.

floating-point math is less than exact because of the limited space used to store values:

```
>>> 0.1 + 0.1 + 0.1 - 0.3 		# Python 3.3
5.551115123125783e-17
```

with decimals, the result can be dead-on:

```
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') 
Decimal('0.0')
```

**Setting decimal precision globally**

Other tools in the decimal module can be used to set the precision of all decimal num-bers, arrange error handling, and more.

```
>>> import decimal
>>> decimal.Decimal(1) / decimal.Decimal(7) 	# Default: 28 digits
Decimal('0.1428571428571428571428571429')

>>> decimal.getcontext().prec = 4				# Fixed precision
>>> decimal.Decimal(1) / decimal.Decimal(7) 
Decimal('0.1429')

>>> Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3) 	# Closer to 0
Decimal('1.110E-17')
```



### 5. Fraction Type 分数类型

Fraction, which implements a rational number object. It essentially keeps both a numerator and a denominator explicitly, so as to avoid some of the inaccuracies and limitations of floating-point math.

Like decimals, fractions do not map as closely to computer hardware as floating-point numbers. This means their performance may not be as good, but it also allows them to provide extra utility in a standard tool where required or useful.

```
>>> from fractions import Fraction
>>> x = Fraction(1, 3)		# Numerator, denominator
>>> y = Fraction(4, 6)		# Simplified to 2, 3 by gcd
>>> x 
Fraction(1, 3)
>>> y 
Fraction(2, 3)
>>> print(y) 
2/3

>>> x + y 
Fraction(1, 1)
>>> x − y 					# Results are exact: numerator, denominator
Fraction(−1, 3)
>>> x * y 
Fraction(2, 9)
```



### 6. Sets

**the set a collection type—an unordered collection of immutable objects** that supports operations corresponding to mathematical set theory. an item appears only once in a set,

 sets are iterable, can grow and shrink on demand, and may contain a variety of object types，it supports extra operations. 

**不可变对象的一个无序集合，一个项在集合中只能出现一次。**集合可以迭代，可根据需要增长或缩短，能够包含各种对象类型，支持额外操作。

#### Set basics in Python 2.6 and earlier

**make a set object**, pass in a sequence or other iterable object to the built-in set function:

```
>>> x = set('abcde')
>>> y = set('bdxyz')
>>> x 
set(['a', 'c', 'b', 'e', 'd'])		# Pythons <= 2.6 display format

# sets do not have a positional ordering, and so are not sequences
```

support the common mathematical **set operations with expression operators**.

> Note that we can’t perform the following operations on plain sequences like strings, lists, and tuples—we must create sets from them by passing them to set in order to apply these tools:

```
>>> x − y 			# Difference
set(['a', 'c', 'e'])

>>> x | y 			# Union
set(['a', 'c', 'b', 'e', 'd', 'y', 'x', 'z'])

>>> x & y 			# Intersection
set(['b', 'd'])

>>> x ^ y 			# Symmetric difference (XOR)
set(['a', 'c', 'e', 'y', 'x', 'z'])

>>> x > y, x < y 	# Superset, subset
(False, False)

>>> 'e' in x 		# Membership (sets)
True

>>> 'e' in 'Camelot', 22 in [11, 22, 33] 		# But works on other types too
(True, True)
```

the set object provides **method**s

```
>>> z = x.intersection(y)			# Same as x & y
>>> z 
set(['b', 'd'])

>>> z.add('SPAM')					# Insert one item
>>> z 
set(['b', 'd', 'SPAM'])

>>> z.update(set(['X', 'Y']))		# Merge: in-place union
>>> z 
set(['Y', 'X', 'b', 'd', 'SPAM'])

>>> z.remove('b')					# Delete one item
>>> z 
set(['Y', 'X', 'd', 'SPAM'])
```

**As iterable containers**, sets can also be used in operations such as len, for loops, and list comprehensions. Because **they are unordered**, though, they don’t support sequence operations like indexing and slicing:

```
>>> for item in set('abc'): print(item * 3) 
aaa 
ccc 
bbb
```



#### Set literals in Python 3.X and 2.7

a new set literal form

```
the following are equivalent:

set([1, 2, 3, 4]) 	# Built-in call (all)
{1, 2, 3, 4}		# Newer set literals (2.7, 3.X)
```

```
>>> set([1, 2, 3, 4]) 		# Built-in: same as in 2.6
{1, 2, 3, 4}
>>> set('spam') 			# Add all items in an iterable
{'s', 'a', 'p', 'm'}

>>> {1, 2, 3, 4} 			# Set literals: new in 3.X (and 2.7)
{1, 2, 3, 4}
>>> S = {'s', 'p', 'a', 'm'}
>>> S 
{'s', 'a', 'p', 'm'}

>>> S.add('alot')			# Methods work as before
>>> S 
{'s', 'a', 'p', 'alot', 'm'}
```

Note that {} is still a dictionary in all Pythons. Empty sets must be created with the set built-in, and print the same way:

```
>>> S1 - {1, 2, 3, 4} 		# Empty sets print differently
set()
>>> type({}) 				# Because {} is an empty dictionary
<class 'dict'>

>>> S = set()				# Initialize an empty set
>>> S.add(1.23)
>>> S 
{1.23}
```

```
>>> {1, 2, 3} | {3, 4} 
{1, 2, 3, 4}
>>> {1, 2, 3} | [3, 4] 
TypeError: unsupported operand type(s) for |: 'set' and 'list'

>>> {1, 2, 3}.union([3, 4]) 
{1, 2, 3, 4}
>>> {1, 2, 3}.union({3, 4}) 
{1, 2, 3, 4}
>>> {1, 2, 3}.union(set([3, 4])) 
{1, 2, 3, 4}

>>> {1, 2, 3}.intersection((1, 3, 5)) 
{1, 3}
>>> {1, 2, 3}.issubset(range(-5, 5)) 
True
```



#### Immutable constraints and frozen sets 不可变限制和冻结集合

because of their implementation, sets can only contain immutable (a.k.a. “hashable”) object types.

集合只能包含不可变对象类型，列表、字典不能嵌入到集合中，元组可以。

> lists and dictionaries cannot be embedded in sets, but tuples can

```
>>> S
{1.23}
>>> S.add([1, 2, 3]) 				# Only immutable objects work in a set
TypeError: unhashable type: 'list'

>>> S.add({'a':1}) 
TypeError: unhashable type: 'dict'
>>> S.add((1, 2, 3))
>>> S 				# No list or dict, but tuple OK
{1.23, (1, 2, 3)}

>>> S | {(4, 5, 6), (1, 2, 3)} 		# Union: same as S.union(...)
{1.23, (4, 5, 6), (1, 2, 3)}
>>> (1, 2, 3) in S 			# Membership: by complete values
True
>>> (1, 4, 3) in S 
False
```



#### Set comprehensions in Python 3.X and 2.7 集合解析

集合解析运行一个循环并在每次迭代时 收集一个表达式的结果，通过一个循环变量来访问当前的迭代值以用于集合表达式中。通过运行代码创建一个新的集合。

> Set comprehensions run a loop and collect the result of an expression on each iteration; a loop variable gives access to the current iteration value for use in the collection expression. The result is a new set you create by running the code, with all the normal set behavior.

```
>>> {x ** 2 for x in [1, 2, 3, 4]} 		# 3.X/2.7 set comprehension
{16, 1, 4, 9}

In this expression, the loop is coded on the right, and the collection expression is coded on the left (x ** 2) .“Give me a new set containing X squared, for every X in a list.”
"对于列表中的每一个X, 给出包含X的平方的一个新的集合"
```

Comprehensions can also iterate across other kinds of objects：

```
>>> {x for x in 'spam'} 		# Same as: set('spam')
{'m', 's', 'p', 'a'}

>>> {c * 4 for c in 'spam'} 	# Set of collected expression results
{'pppp', 'aaaa', 'ssss', 'mmmm'}
>>> {c * 4 for c in 'spamham'} 
{'pppp', 'aaaa', 'hhhh', 'ssss', 'mmmm'}

>>> S = {c * 4 for c in 'spam'}
>>> S | {'mmmm', 'xxxx'} 
{'pppp', 'xxxx', 'mmmm', 'aaaa', 'ssss'}
>>> S & {'mmmm', 'xxxx'} 
{'mmmm'}
```



### 7. Booleans 布尔型

True and False, are just customized versions of the integers 1 and 0 that print themselves differently

```
>>> type(True) 
<class 'bool'>
>>> isinstance(True, int) 
True
>>> True == 1 		# Same value
True
>>> True is 1 		# But a different object: see the next chapter
False
>>> True or False 	# Same as: 1 or 0
True
>>> True + 4 		# (Hmmm)
5
```















## Python Expression Operators

### Python expression operators and precedence

```
1. Operators lower in the table have higher precedence, and so bind more tightly in mixed expressions.

2. Operators in the same row generally group from left to right when combined (except for exponentiation, which groups right to left, and comparisons, which chain left to right).

3. When you enclose subexpressions in parentheses "()", you override Python’s precedence rules; Python always evaluates expressions in parentheses first before using their results in the enclosing expressions.

-----------------------------------------------------------------------------------------
Python expression operators and precedence

Operators                            Description
----------------------------         ----------------------------------------------------
yield x                              Generator function send protocol
lambda args: expression              Anonymous function generation
x if y else z                        Ternary selection (x is evaluated only if y is true)
x or y                               Logical OR (y is evaluated only if x is false)
x and y                              Logical AND (y is evaluated only if x is true)
not x                                Logical negation
x in y, x not in y                   Membership (iterables, sets)
x is y, x is not y                   Object identity tests
x < y, x <= y, x > y, x >= y         Magnitude comparison, set subset and superset;
x == y, x != y                       Value equality operators
x | y                                Bitwise OR, set union
x ^ y                                Bitwise XOR, set symmetric difference
x & y                                Bitwise AND, set intersection
x << y, x >> y                       Shift x left or right by y bits
x + y                                Addition, concatenation;
x – y                                Subtraction, set difference
x * y                                Multiplication, repetition;
x % y                                Remainder, format;
x / y, x // y                        Division: true and floor
−x, +x                               Negation, identity
~x                                   Bitwise NOT (inversion)
x ** y                               Power (exponentiation)
x[i]                                 Indexing (sequence, mapping, others)
x[i:j:k]                             Slicing
x(...)                               Call (function, method, class, other callable)
x.attr                               Attribute reference
(...)                                Tuple, expression, generator expression
[...]                                List, list comprehension
{...}                                Dictionary, set, set and dictionary comprehensions
```

about version differences and recent additions related to the operators. both Python 2.X and 3.X

> - In Python 2.X, value inequality can be written as either X != Y or X <> Y. In Python 3.X, the latter of these options is removed because it is redundant. In either version, best practice is to use X != Y for all value inequality tests.
>
>
> - In Python 2.X, a backquotes expression \`X` works the same as repr(X) and converts objects to display strings. Due to its obscurity, this expression is removed in Python 3.X; use the more readable str and repr built-in functions, described in “Numeric Display Formats.”
> - The X // Y floor division expression always truncates fractional remainders in both Python 2.X and 3.X. The X / Y expression performs true division in 3.X (retaining remainders) and classic division in 2.X (truncating for integers). 
> - The syntax [...] is used for both list literals and list comprehension expressions. The latter of these performs an implied loop and collects expression results in a new list. 
> - The syntax (...) is used for tuples and expression grouping, as well as generator expressions—a form of list comprehension that produces results on demand, instead of building a result list. The parentheses may sometimes be omitted in all three contexts.
> - The syntax {...} is used for dictionary literals, and in Python 3.X and 2.7 for set literals and both dictionary and set comprehensions. 
> - The yield and ternary if/else selection expressions are available in Python 2.5 and later. The former returns send(...) arguments in generators; the latter is shorthand for a multiline if statement. yield requires parentheses if not alone on the right side of an assignment statement.
> - Comparison operators may be chained: X < Y < Z produces the same result as X < Y and Y < Z.
> - In recent Pythons, the slice expression X[I:J:K] is equivalent to indexing with a slice object: X[slice(I, J, K)].
> - In Python 2.X, magnitude comparisons of mixed types are allowed, and convert numbers to a common type, and order other mixed types according to type names. In Python 3.X, nonnumeric mixed-type magnitude comparisons are not allowed and raise exceptions; this includes sorts by proxy.
> - Magnitude comparisons for dictionaries are also no longer supported in Python 3.X (though equality tests are); comparing sorted(aDict.items()) is one possible replacement.

Python 解释器可以作为一个简单的计算器，您可以在解释器里输入一个表达式，它将输出表达式的值。

### 加法 `+`

```
>>> 2 + 2
4
```

### 减法 `-`

```
>>> 4 - 2
2
```

### 乘法 `*` 

```
>>> 5 * 6
30
```

**注意：**在不同的机器上浮点运算的结果可能会不一样。

### 除法 `/` 

在整数除法中，除法 `/` 总是返回一个浮点数。(Python 3.X)

两个操作数都是整数，执行截断的整数除法；否则执行浮点除法保留余数。(Python 2.X)

```
Python 3.X

>>> 6 / 3    # 整数除法返回浮点型
2.0
>>> 17 / 3  
5.666666666666667
```

```
Python 2.X

>>> 7 / 2
3
>>> 7.0 / 2
3.5
```

### Floor division `//`  

只得到整数的结果，省略结果的小数部分 (available in both Python 2.X and 3.X)：

```
Python 2.X and 3.X

>>> 17 // 3  # 整数除法返回向下取整后的结果 returns an integer for integer operands
5
>>> 17.0 // 3    #returns a float for float operands
5.0
```

支持两个Python版本

If your programs depend on truncating integer division, use // in both 2.X and 3.X as just mentioned. If your programs require floating-point results with remainders for integers, use float to guarantee that one operand is a float around a / when run in 2.X:

```
X = Y // Z			# Always truncates, always an int result for ints in 2.X and 3.X
X = Y / float(Z)	# Guarantees float division with remainder in either 2.X or 3.X
```

Alternatively, you can enable 3.X / division in 2.X with a` __future__` import, rather than forcing it with float conversions:

```
>>> from __future__ import division		# Enable 3.X "/" behavior
>>> 10 / 4
2.5
>>> 10 // 4 							# Integer // is the same in both
2

This special from statement applies to the rest of your session when typed interactively like this, and must appear as the first executable line when used in a script file (and alas, we can import from the future in Python, but not the past; insert something about talking to “the Doc” here...).
```

### Floor versus truncation

```
>>> import math
>>> math.floor(2.5) 	# Closest number below value
2
>>> math.floor(-2.5) 
-3
>>> math.trunc(2.5) 	# Truncate fractional part (toward zero)
2
>>> math.trunc(-2.5) 
-2
```

Python 3.X:

```
Python 3.X

>>> 5 / 2, 5 / −2 
(2.5, −2.5)
>>> 5 // 2, 5 // −2 		# Truncates to floor: rounds to first lower integer
(2, −3)						# 2.5 becomes 2, −2.5 becomes −3

>>> 5 / 2.0, 5 / −2.0 
(2.5, −2.5)
>>> 5 // 2.0, 5 // −2.0	 	# Ditto for floats, though result is float too
(2.0, −3.0)
```

Python 2.X:

```
>>> 5 / 2, 5 / −2 		# Differs in 3.X
(2, −3)
>>> 5 // 2, 5 // −2 	# This and the rest are the same in 2.X and 3.X
(2, −3)

>>> 5 / 2.0, 5 / −2.0 
(2.5, −2.5)
>>> 5 // 2.0, 5 // −2.0 
(2.0, −3.0)
```

If you really want truncation toward zero regardless of sign, you can always run a float division result through math.trunc, regardless of Python version (also see the round built-in for related functionality, and the int built-in, which has the same effect here but requires no import):

Python 3.X:

```
Python 3.X:

>>> import math
>>> 5 / −2 						# Keep remainder
−2.5
>>> 5 // −2 					# Floor below result 
-3
>>> math.trunc(5 / −2) 			# Truncate instead of floor (same as int())
−2
```

Python 2.X:

```
Python 2.X:

>>> import math
>>> 5 / float(−2) 				# Remainder in 2.X
−2.5
>>> 5 / −2, 5 // −2 			# Floor in 2.X 
(−3, −3)
>>> math.trunc(5 / float(−2)) 	# Truncate in 2.X
−2
```

Why does truncation matter?

It’s possible that the nontruncating behavior of / in 3.X may break a significant number of 2.X programs.

```
Python 3.X:
>>> (5 / 2), (5 / 2.0), (5 / −2.0), (5 / −2) 		# 3.X true division
(2.5, 2.5, −2.5, −2.5)

>>> (5 // 2), (5 // 2.0), (5 // −2.0), (5 // −2) 	# 3.X floor division
(2, 2.0, −3.0, −3)

>>> (9 / 3), (9.0 / 3), (9 // 3), (9 // 3.0) 		# Both
(3.0, 3.0, 3, 3.0)
```

```
Python 2.X:
>>> (5 / 2), (5 / 2.0), (5 / −2.0), (5 / −2) 		# 2.X classic division (differs)
(2, 2.5, −2.5, −3)

>>> (5 // 2), (5 // 2.0), (5 // −2.0), (5 // −2) 	# 2.X floor division (same)
(2, 2.0, −3.0, −3)

>>> (9 / 3), (9.0 / 3), (9 // 3), (9 // 3.0) 		# Both
(3, 3.0, 3, 3.0)
```

### How can you truncate and round a floating-point number?

```
>>> int(3.6)			# 方法1：int(N) 省略小数部分
3
>>> int(-3.6)
-3

>>> import math			# 方法2：math.trunc(N) 省略小数部分
>>> math.trunc(3.6)
3
>>> math.trunc(-3.6)
-3

>>> round(3.6)			# 方法3：round(N, digit) 函数做四舍五入
4
>>> round(3.62, 1)
3.6

```







### 余数 `％` 

`％` 操作符返回除法的余数

```
>>> 17 % 3  # ％操作符返回除法的余数
2
```

### 赋值 `=` 

等号 `=` 用于给变量赋值。

```
>>> width = 20
>>> height = 5*9
>>> width * height
900
```

### 幂 `**` 

使用 `**` 操作来进行幂运算：

```
>>> 5 ** 2  # 5 的平方
25
>>> 2 ** 7  # 2的7次方
128
```

变量在使用前必须先"定义"（即赋予变量一个值），否则会出现错误：

```
>>> n   # 尝试访问一个未定义的变量
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```

在交互模式中，最后被输出的表达式结果被赋值给变量 **_ **。(此处， **_ **变量应被用户视为只读变量)。例如：

```
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

### 不同类型的数混合运算

Python automatically converts up to the more complex type within an expression.

> in mixed-type numeric expressions, Python first converts operands up to the type of the most complicated operand, and then performs the math on same-type operands. 
>
> all these mixed-type conversions apply only when mixing numeric types (e.g., an integer and a floating point) in an expression, including those using numeric and comparison operators.

**不同类型的数混合运算时会将整数转换为浮点数：**

```
>>> 40 + 3.14 		# Integer to float, float math/result
43.14
>>> 3 * 3.75 / 1.5
7.5
>>> 7.0 / 2
3.5
```

### 位操作 Bitwise Operations

注意位操作在python这样的高级语言中并不想在C这样的底层语言中那么重要。python中有比字符串等号的编码信息的方法

> bitwise operations are often not as important in a high-level language such as Python as they are in a low-level language such as C. As a rule of thumb, if you find yourself wanting to flip bits in Python, you should think about which language you’re really coding.Python’s lists, dictionaries, and the like provide richer—and usually better—ways to encode information than bit strings, especially when your data’s audience includes readers of the human variety.

```
>>> x = 1		# 1 decimal is 0001 in bits
>>> x << 2		# Shift left 2 bits: 0100
4
>>> x | 2 		# Bitwise OR (either bit=1): 0011 
3
>>> x & 1 		# Bitwise AND (both bits=1): 0001
1
```

## Python 数字类型转换

有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。

- **int(x)** 将x转换为一个整数。
- **float(x)** 将x转换到一个浮点数。
- **complex(x)** 将x转换到一个复数，实数部分为 x，虚数部分为 0。
- **complex(x, y)** 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。

以下实例将浮点数变量 a 转换为整数：

```
>>> a = 1.0
>>> int(a)
1
```





## Variables and Basic Expressions



- 变量在它第一次赋值时创建。			  Variables are created when they are first assigned values. 


- 变量在表达式中使用将被替换为它们的值。 Variables are replaced with their values when used in expressions. 


- 变量在表达式中使用以前必须已赋值。         Variables must be assigned before they can be used in expressions. 


- 变量像对象一样不需要在一开始进行声明。  Variables refer to objects and are never declared ahead of time. 



Python 数字数据类型用于存储数值。

数据类型是不允许改变的,这就意味着如果改变数字数据类型得值，将重新分配内存空间。

以下实例在变量赋值时 Number 对象将被创建：

```
var1 = 1
var2 = 10
```



```
>>> a + 1, a − 1 		 # Addition (3 + 1), subtraction (3 − 1) 
(4, 2)
>>> b * 3, b / 2 		 # Multiplication (4 * 3), division (4 / 2)
(12, 2.0)
>>> a % 2, b ** 2 		 # Modulus (remainder), power (4 ** 2)
(1, 16)
>>> 2 + 4.0, 2.0 ** b    # Mixed-type conversions
(6.0, 16.0)
```



在Python中，变量不需要预声明，但在使用前，至少要赋一次值。

> 这意味着在对其进行运算时要计数器初始化为0，在列表后添加元素前，要初始化列表为一个空列表。



您也可以使用del语句删除一些数字对象的引用。

del语句的语法是：

```
del var1[,var2[,var3[....,varN]]]]
```

您可以通过使用del语句删除单个或多个对象的引用，例如：

```
del var
del var_a, var_b
```



## Comparisons: Normal and Chained



```
>>> 1 < 2 	# Less than 
True
>>> 2.0 >= 1 	# Greater than or equal: mixed-type 1 converted to 1.0 
True
>>> 2.0 == 2.0 		# Equal value 
True
>>> 2.0 != 2.0 		# Not equal value
False
```

```
>>> X < Y < Z 	# Chained comparisons: range tests
True
>>> X < Y and Y < Z 
True
>>> 1 < 2 < 3.0 < 4 
True
>>> 1 > 2 > 3.0 > 4 
False
```

```
>>> 1 == 2 < 3 		# Same as: 1 == 2 and 2 < 3 
False				# Not same as: False < 3 (which means 0 < 3, which is true!)
```

```
>>> 1.1 + 2.2 == 3.3 			# Shouldn't this be True?...
False
>>> 1.1 + 2.2					# Close to 3.3, but not exactly: limited precision 
3.3000000000000003
>>> int(1.1 + 2.2) == int(3.3)  # OK if convert: see also round, floor, trunc ahead 
True							# Decimals and fractions (ahead) may help here too

This stems from the fact that floating-point numbers cannot represent some values exactly due to their limited number of bits
```









## 数学函数

| 函数                                       | 返回值 ( 描述 )                               |
| ---------------------------------------- | ---------------------------------------- |
| [abs(x)](http://www.runoob.com/python3/python3-func-number-abs.html) | 返回数字的绝对值，如abs(-10) 返回 10                 |
| [ceil(x)](http://www.runoob.com/python3/python3-func-number-ceil.html) | 返回数字的上入整数，如math.ceil(4.1) 返回 5           |
| cmp(x, y)                                | 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 **Python 3 已废弃** 。使用 **使用 (x>y)-(x<y)** 替换。 |
| [exp(x)](http://www.runoob.com/python3/python3-func-number-exp.html) | 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045 |
| [fabs(x)](http://www.runoob.com/python3/python3-func-number-fabs.html) | 返回数字的绝对值，如math.fabs(-10) 返回10.0          |
| [floor(x)](http://www.runoob.com/python3/python3-func-number-floor.html) | 返回数字的下舍整数，如math.floor(4.9)返回 4           |
| [log(x)](http://www.runoob.com/python3/python3-func-number-log.html) | 如math.log(math.e)返回1.0,math.log(100,10)返回2.0 |
| [log10(x)](http://www.runoob.com/python3/python3-func-number-log10.html) | 返回以10为基数的x的对数，如math.log10(100)返回 2.0     |
| [max(x1, x2,...)](http://www.runoob.com/python3/python3-func-number-max.html) | 返回给定参数的最大值，参数可以为序列。                      |
| [min(x1, x2,...)](http://www.runoob.com/python3/python3-func-number-min.html) | 返回给定参数的最小值，参数可以为序列。                      |
| [modf(x)](http://www.runoob.com/python3/python3-func-number-modf.html) | 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。   |
| [pow(x, y)](http://www.runoob.com/python3/python3-func-number-pow.html) | x**y 运算后的值。                              |
| round(x [,n\])                           | 返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。        |
| [sqrt(x)](http://www.runoob.com/python3/python3-func-number-sqrt.html) | 返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j |



## 随机数函数

随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。

Python包含以下常用随机数函数：

| 函数                                       | 描述                                       |
| ---------------------------------------- | ---------------------------------------- |
| [choice(seq)](http://www.runoob.com/python3/python3-func-number-choice.html) | 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。 |
| [randrange ([start,\] stop [,step])](http://www.runoob.com/python3/python3-func-number-randrange.html) | 从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1        |
| [random()](http://www.runoob.com/python3/python3-func-number-random.html) | 随机生成下一个实数，它在[0,1)范围内。                    |
| seed([x\])                               | 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。 |
| [shuffle(lst)](http://www.runoob.com/python3/python3-func-number-shuffle.html) | 将序列的所有元素随机排序                             |
| [uniform(x, y)](http://www.runoob.com/python3/python3-func-number-uniform.html) | 随机生成下一个实数，它在[x,y]范围内。                    |



## 三角函数

Python包括以下三角函数：

| 函数                                       | 描述                                    |      |
| ---------------------------------------- | ------------------------------------- | ---- |
| [acos(x)](http://www.runoob.com/python3/python3-func-number-acos.html) | 返回x的反余弦弧度值。                           |      |
| [asin(x)](http://www.runoob.com/python3/python3-func-number-asin.html) | 返回x的反正弦弧度值。                           |      |
| [atan(x)](http://www.runoob.com/python3/python3-func-number-atan.html) | 返回x的反正切弧度值。                           |      |
| [atan2(y, x)](http://www.runoob.com/python3/python3-func-number-atan2.html) | 返回给定的 X 及 Y 坐标值的反正切值。                 |      |
| [cos(x)](http://www.runoob.com/python3/python3-func-number-cos.html) | 返回x的弧度的余弦值。                           |      |
| [hypot(x, y)](http://www.runoob.com/python3/python3-func-number-hypot.html) | 返回欧几里德范数 sqrt(x*x + y*y)。             |      |
| [sin(x)](http://www.runoob.com/python3/python3-func-number-sin.html) | 返回的x弧度的正弦值。                           |      |
| [tan(x)](http://www.runoob.com/python3/python3-func-number-tan.html) | 返回x弧度的正切值。                            |      |
| [degrees(x)](http://www.runoob.com/python3/python3-func-number-degrees.html) | 将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0 |      |
| [radians(x)](http://www.runoob.com/python3/python3-func-number-radians.html) | 将角度转换为弧度                              |      |



## 数学常量

| 常量   | 描述                   |
| ---- | -------------------- |
| pi   | 数学常量 pi（圆周率，一般以π来表示） |
| e    | 数学常量 e，e即自然常数（自然常数）。 |



## 更多

### 3种方法计算平方根

there are three ways to compute square roots in Python: using a module function, an expression, or a built-in function

```
>>> import math
>>> math.sqrt(144)		# Module
12.0
>>> 144 ** .5			# Expression
12.0
>>> pow(144, .5)		# Built-in
12.0
```

### NumPy