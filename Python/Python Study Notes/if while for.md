# if 

The Python `if` statement is typical of `if` statements in most procedural languages. It takes the form of an `if` test, followed by one or more optional `elif` (“else if”) tests and a final optional `else` block. The tests and the `else` part each have an associated block of nested statements, indented under a header line. When the `if` statement runs, Python executes the block of code associated with the first test that evaluates to true, or the `else` block if all tests prove false. The general form of an `if` statement looks like this:

```
if test1:			# if test
	statements1 	# Associated block
elif test2:			# Optional elifs
	statements2
else:				# Optional else
	statements3
```

> All parts are optional, except the initial `if` test and its associated statements.

**Examples**:

```
>>> if 1:				# 1 is Boolean true, so this statement’s test always succeeds.
... 	print('true') 
...
true

>>> if not 1:			# To handle a false result
... 	print('true') 
... else:
... 	print('false') 
...
false
```



## Multiway Branching

> If you’ve used languages like C or Pascal, you might be interested to know that there is no switch or case statement in Python that selects an action based on a variable’s value.

**you usually code multiway branching as a series of if/elif tests**

```
>>> choice = 'ham'					# The equivalent if statement
>>> if choice == 'spam': 
... 	print(1.25) 
... elif choice == 'ham': 
... 	print(1.99) 
... elif choice == 'eggs': 
... 	print(0.99) 
... elif choice == 'bacon': 
... 	print(1.10) 
... else:
... 	print('Bad choice') 
...
1.99
```

and **occasionally by indexing dictionaries or searching lists**. Because dictionaries and lists can be built at runtime dynamically, they are sometimes more flexible than hardcoded if logic in your script:

**this dictionary is a multiway branch-indexing on the key choice branches to one of a set of values**

```
>>> choice = 'ham'
>>> print({'spam': 1.25, 			# A dictionary-based 'switch'
... 	   'ham': 1.99, 			# Use has_key or get for default
... 	   'eggs': 0.99, 
... 	   'bacon': 1.10}[choice])
1.99
```

**dictionary defaults can be coded with in expressions, get method calls, or exception catching with the try statement** . All of the same techniques can be used here to code a default action in a dictionary-based multiway branch.

```
>>> branch = {'spam': 1.25, 
... 		  'ham': 1.99, 
... 		  'eggs': 0.99}

>>> print(branch.get('spam', 'Bad choice')) 
1.25
>>> print(branch.get('bacon', 'Bad choice')) 
Bad choice
```

An `in` membership test in an `if` statement can have the same default effect:

```
>>> choice = 'bacon'
>>> if choice in branch:
... 	print(branch[choice]) 
... else:
... 	print('Bad choice') 
...
Bad choice
```

dictionaries can also contain functions to represent more complex branch actions and implement general jump tables. Such functions appear as dictionary values, they may be coded as function names or inline lambdas, and they are called by adding parentheses to trigger their actions.

> ```
> def function(): ... 
> def default(): ...
>
> branch = {'spam': lambda: ..., 		# A table of callable function objects
> 		  'ham': function, 
> 		  'eggs': lambda: ...}
>
> branch.get(choice, default)()
> ```

Although **dictionary-based multiway branching** is useful in programs that deal with more dynamic data, most programmers will probably find that coding an if statement is the most straightforward way to perform multiway branching. As a rule of thumb in coding, **when in doubt, err on the side of simplicity and readability**; it’s the “Pythonic” way.



## Truth Values and Boolean Tests

Python’s Boolean operators are a bit different from their counterparts in languages like C. In Python:

- **All objects have an inherent Boolean true or false value.**


- **Any nonzero number or nonempty object is true.**



- **Zero numbers, empty objects, and the special object `None` are considered false.**



- **Comparisons and equality tests are applied recursively to data structures.**



- **Comparisons and equality tests return `True` or `False` (custom versions of `1` and `0` ).**



- **Boolean `and` and `or` operators return a true or false operand object.**



- **Boolean operators stop evaluating (“short circuit”) as soon as a result is known.**

The `if` statement takes action on truth values, but Boolean operators are used to combine the results of other tests in richer ways to produce new truth values. there are three Boolean expression operators in Python:

```
X and Y 
# Is true if both X and Y are true 

X or Y
# Is true if either X or Y is true

not X
# Is true if X is false (the expression returns True or False)
```

X and Y may be any truth value, or any expression that returns a truth value (e.g., an equality test, range comparison, and so on).Boolean operators are typed out as words in Python (instead of C’s &&, ||, and !).

Boolean `and` and `or` operators return a `true` or `false` object in Python, not the values True or False.

```
>>> 2 < 3, 3 < 2 		# Less than: return True or False (1 or 0)
(True, False)

# Magnitude comparisons such as these return True or False as their truth results,are really just custom versions of the integers 1 and 0
```

the `and` and `or` operators always return an object—either the object on the left side of the operator or the object on the right.

**For `or` tests, Python evaluates the operand objects from left to right and returns the first one that is true**. Moreover, Python stops at the first true operand it finds. This is usually called **short-circuit evaluation**

```
>>> 2 or 3, 3 or 2 		# Return left operand if true
(2, 3)					# Else, return right operand (true or false)
>>> [] or 3 
3
>>> [] or {} 
{}
```

> In the first line of the preceding example, both operands (2 and 3) are true (i.e., are nonzero), so Python always stops and returns the one on the left—it determines the result because true `or` anything is always true.

> In the other two tests, **the left operand is false** (an empty object), so **Python simply evaluates and returns the object on the right**—**which may happen to have either a true or a false value when tested**.

**Python `and` operations also stop as soon as the result is known**; however, in this case Python evaluates the operands from left to right and stops if the left operand is a `false` object because it determines the result—false `and` anything is always false:

```
>>> 2 and 3, 3 and 2 		# Return left operand if false
(3, 2)						# Else, return right operand (true or false)
>>> [] and {} 
[]
>>> 3 and [] 
[]
```

> Here, both operands are true in the first line, so Python evaluates both sides and returns the object on the right. 
>
> In the second test, the left operand is false (`[]`), so Python stops and returns it as the test result. 
>
> In the last test, the left side is true (`3`), so Python evaluates and returns the object on the right—which happens to be a false `[]`.



## The if/else Ternary Expression

> ```
> if X:
> 	A = Y 
> else:
> 	A = Z
> ```

Python 2.5 introduced a new expression format that allows us to say the same thing in one expression:

```
A = Y if X else Z
```

examples:

```
>>> A = 't' if 'spam' else 'f'		# For strings, nonempty means true
>>> A 
't'
>>> A = 't' if '' else 'f'
>>> A 
'f'
```

the same effect can often be achieved by a careful combination of the `and` and `or` operators

```
A = ((X and Y) or Z)
```

you have to be able to assume that Y will be Boolean true. If that is the case, the effect is the same: the `and` runs first and returns Y if X is true; if X if false the `and` skips Y, and the `or` simply returns `Z`.

using the following expression in Python is similar because the `bool` function will translate X into the equivalent of integer `1` or `0` , which can then be used as offsets to pick true and false values from a list:

```
A = [Z, Y][bool(X)]
```

example:

```
>>> ['f', 't'][bool('')] 
'f'
>>> ['f', 't'][bool('spam')] 
't'
```



## Why You Will Care: Booleans

Python Boolean operators is to select from a set of objects with an or. A statement such as this:

```
X = A or B or C or None
```

> assigns X to the first nonempty (that is, true) object among A, B, and C, or to None if all of them are empty.



if `f1` returns a true (or nonempty) value, Python will never run `f2`.

```
if f1() or f2(): ...
```

To guarantee that both functions will be run, call them before the `or`:

```
tmp1, tmp2 = f1(), f2() 
if tmp1 or tmp2: ...
```



# while Loops

Python’s while statement is the most general iteration construct in the language. In simple terms, it repeatedly executes a block of (normally indented) statements as long as a test at the top keeps evaluating to a true value. It is called a “loop” because control keeps looping back to the start of the statement until the test becomes false. When the test becomes false, control passes to the statement that follows the while block. The net effect is that the loop’s body is executed repeatedly while the test at the top is true. If the test is false to begin with, the body never runs and the while statement is skipped.



### General Format

In its most complex form, the while statement consists of a header line with a test expression, a body of one or more normally indented statements, and an optional else part that is executed if control exits the loop without a break statement being encountered. Python keeps evaluating the test at the top and executing the statements nested in the loop body until the test returns a false value:

```
while test:			# Loop test
	statements 		# Loop body
else:				# Optional else 
	statements		# Run if didn't exit loop with break
```

#### Examples:

```
>>> x = 'spam'
>>> while x:				# While x is not empty
... 	print(x, end=' ') 	# In 2.X use print x,
... 	x = x[1:] 			# Strip first character off x
...
spam pam am m
```

counts from the value of a up to, but not including, b:

```
>>> a=0; b=10
>>> while a < b:			# One way to code counter loops
... 	print(a, end=' ') 
... 	a += 1				# Or, a = a + 1
...
0 1 2 3 4 5 6 7 8 9
```

```
while True:
	...loop body...
	if exitTest(): break
```



# General Loop Format

Factoring in `break` and `continue` statements, the general format of the `while` loop looks like this:

```
while test1:
	statements 
	if test2 : break 		# Exit loop now, skip else if present 
	if test3: continue 		# Go to top of loop now, to test1
else:
	statements				# Run if we didn't hit a 'break'
```

`break` and `continue` statements can appear anywhere inside the `while` ( or `for` ) loop’s body, but they are usually coded further nested in an if test to take action in response to some condition.



# break 

**Jumps out of the closest enclosing loop (past the entire loop statement).** Because the code that follows it in the loop is not executed if the `break` is reached, you can also sometimes avoid nesting by including a `break`.

inputs data with `input` (known as `raw_input` in Python 2.X) and exits when the user enters “stop” for the name request:

```
>>> while True:
...		name = input('Enter name:')		# Use raw_input() in 2.X
... 	if name == 'stop': break 
... 	age = input('Enter age: ') 
... 	print('Hello', name, '=>', int(age) ** 2) 
...
Enter name:bob 
Enter age: 40 
Hello bob => 1600 
Enter name:sue 
Enter age: 30 Hello sue => 900 
Enter name:stop
```





# continue

**Jumps to the top of the closest enclosing loop (to the loop’s header line).** It also sometimes lets you avoid statement nesting.

skip odd numbers:

```
x = 10 
while x:
	x = x−1 					# Or, x -= 1
	if x % 2 != 0: continue 	# Odd? -- skip print
	print(x, end=' ')			# it prints 8 6 4 2 0
```



# pass 

**Does nothing at all, it’s an empty statement placeholder. It is often used to code an empty body for a compound statement.**

A `pass` is also sometime coded to mean “to be filled in later,” to stub out the bodies of functions temporarily:

```
def func1(): 
	pass			# Add real code here later
def func2(): 
	pass
```

We can’t leave the body empty without getting a syntax error, so we say `pass` instead.

#### Version skew note `...`  :

Python 3.X (but not 2.X) allows ellipses coded as `...` (literally, three consecutive dots) to appear any place an expression can. Because ellipses do nothing by themselves, this can serve as an alternative to the pass statement, especially for code to be filled in later—a sort of Python “TBD”(未确定内容):

```
def func1():
	...				# Alternative to pass

def func2():
	...

func1()				# Does nothing if called
```

Ellipses can also appear on the same line as a statement header and may be used to initialize variable names if no specific type is required:

```
def func1(): ... 			# Works on same line too
def func2(): ...

>>> X = ...					# Alternative to None
>>> X 
Ellipsis
```





# Loop else block

**Runs if and only if the loop is exited normally (i.e., without hitting a break)**

When combined with the loop else clause, the break statement can often eliminate the need for the search status flags used in other languages.

**For instance:**

> the following piece of code determines whether a positive integer y is prime by searching for factors greater than 1:

```
x = y // 2 							# For some y > 1 
while x > 1:
	if y % x == 0:					# Remainder 
		print(y, 'has factor', x) 
		break 						# Skip else 
	x -= 1 
else:								# Normal exit
	print(y, 'is prime')
```

Rather than setting a flag to be tested when the loop is exited, it inserts a break where a factor is found. This way, the loop else clause can assume that it will be executed only if no factor is found; if you don’t hit the break, the number is prime. 



**it is a coding structure that lets us catch the “other” way out of a loop**

**For instance:**

> that we are writing a loop to search a list for a value, and we need to know whether the value was found after we exit the loop.

```
found = False 
while x and not found:
	if match(x[0]):					# Value at front?
		print('Ni') 
		found = True 
	else:
		x = x[1:] 					# Slice off front and repeat
if not found:
	print('not found')
```

Here’s an else equivalent:

```
while x:				# Exit when x empty
	if match(x[0]):
		print('Ni') 
		break			# Exit, go around else
	x = x[1:] 
else:
	print('Not found')	# Only here if exhausted x
```

> Because the `break` inside the main part of the `while` exits the loop and goes around the `else`, this serves as a more structured way to catch the search-failure case.



**You can move the assignment into the loop body with a `break`**:

```
while True:
	x = next(obj) 
	if not x: break 
	...process x...
```

or move the assignment into the loop with tests:

```
x = True 
while x:
	x = next(obj) 
	if x:
		...process x...
```

or move the first assignment outside the loop:

```
x = next(obj) 
while x:
	...process x... 
	x = next(obj)
```



# for Loops

The for loop is a generic iterator in Python: it can step through the items in any ordered sequence or other iterable object. 

> The for statement works on strings, lists, tuples, and other built-in iterables, as well as new user-defined objects

The Python for loop begins with a header line that specifies an assignment target (or targets), along with the object you want to step through. The header is followed by a block of (normally indented) statements that you want to repeat:

```
for target in object:		# Assign object items to target 
	statements 				# Repeated loop body: use target 
else:						# Optional else part 
	statements				# If we didn't hit a 'break'
```

When Python runs a `for` loop, it assigns the items in the iterable object to the target one by one and executes the loop body for each. The loop body typically uses the assignment target to refer to the current item in the sequence as though it were a cursor stepping through the sequence.

```
for target in object:			# Assign object items to target
	statements 
	if test: break 				# Exit loop now, skip else 
	if test: continue 			# Go to top of loop now
else:
	statements					# If we didn't hit a 'break', run else
```

#### List Example:

```
>>> for x in ["spam", "eggs", "ham"]: 
... 	print(x, end=' ') 
...
spam eggs ham

>>> sum = 0
>>> for x in [1, 2, 3, 4]: 
... 	sum = sum + x 
...
>>> sum 
10
>>> prod = 1
>>> for item in [1, 2, 3, 4]: prod *= item 
...
>>> prod 
24
```

#### String & Tuple Example:

```
>>> S = "lumberjack"
>>> T = ("and", "I'm", "okay")

>>> for x in S: print(x, end=' ') 		# Iterate over a string
...
l u m b e r j a c k

>>> for x in T: print(x, end=' ') 		# Iterate over a tuple
...
and I'm okay
```

assign manually within the loop to unpack:

```
>>> T 
[(1, 2), (3, 4), (5, 6)]

>>> for both in T: 
... 	a, b = both 	# Manual assignment equivalent
... 	print(a, b) 
...
1 2 
3 4 
5 6
```



#### iterating through a sequence of tuples:

```
>>> T = [(1, 2), (3, 4), (5, 6)]
>>> for (a, b) in T: 			# Tuple assignment at work
...		print(a, b) 
...
1 2
3 4
5 6
```

#### Dictionary:

```
>>> D = {'a': 1, 'b': 2, 'c': 3}
>>> for key in D:
... 	print(key, '=>', D[key]) 		# Use dict keys iterator and index
...
a => 1 
c => 3 
b => 2

>>> list(D.items()) 			# dictionaries using the items method
[('a', 1), ('c', 3), ('b', 2)]

>>> for (key, value) in D.items(): 
... 	print(key, '=>', value) 		# Iterate over both keys and values
...
a => 1 
c => 3 
b => 2
```

#### Nested Structures :

```
>>> ((a, b), c) = ((1, 2), 3)		# Nested sequences work too
>>> a, b, c 
(1, 2, 3)

>>> for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c) 
...
1 2 3 
4 5 6
```

Any nested sequence structure may be unpacked this way, simply because sequence assignment is so generic:

```
>>> for ((a, b), c) in [([1, 2], 3), ['XY', 6]]: print(a, b, c) 
...
1 2 3 
X Y 6
```

### Python 3.X extended sequence assignment in for loops

**The only difference is that slicing returns a type-specific result, whereas starred names always are assigned lists**

In Python 3.X,:

```
>>> a, *b, c = (1, 2, 3, 4)		# Extended seq assignment
>>> a, b, c
(1, [2, 3], 4)

>>> for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]: 	# in 3.X
... 	print(a, b, c) 
...
1 [2, 3] 4 
5 [6, 7] 8
```

In Python 2.X starred names aren’t allowed, but you can achieve similar effects by slicing:

```
>>> for all in [(1, 2, 3, 4), (5, 6, 7, 8)]: 		# Manual slicing in 2.X
... 	a, b, c = all[0], all[1:3], all[3] 
... 	print(a, b, c) 
...
1 (2, 3) 4 
5 (6, 7) 8
```

### Nested for loops











