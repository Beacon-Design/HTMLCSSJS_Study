

# Statements



Python is a procedural, statement-based language; by combining statements, you specify a procedure that Python performs to satisfy a program’s goals.

Python program structure:

1. Programs are composed of modules.
2. Modules contain statements.
3. Statements contain expressions.
4. Expressions create and process objects.

### Python statements

```
# Python statements

================================================================================
STATEMENT					 ROLE					EXAMPLE
================================================================================
Assignment 					 Creating references	a, b = 'good', 'bad'
--------------------------------------------------------------------------------
Calls and other expressions  Running functions		log.write("spam, ham")
--------------------------------------------------------------------------------
print calls 				 Printing objects		print('The Killer', joke)
--------------------------------------------------------------------------------
if/elif/else 				 Selecting actions		if "python" in text:
													    print(text)
--------------------------------------------------------------------------------
for/else 					 Iteration				for x in mylist: 
														print(x)
--------------------------------------------------------------------------------
while/else					 General loops			while X > Y:
														print('hello')
--------------------------------------------------------------------------------
pass 						 Empty placeholder		while True:
														pass
--------------------------------------------------------------------------------
break 						 Loop exit				while True:
														if exittest(): break
--------------------------------------------------------------------------------
continue 					 Loop continue			while True:
														if skiptest(): continue
--------------------------------------------------------------------------------
def 						 Functions and methods	def f(a, b, c=1, *d):
														print(a+b+c+d[0])
--------------------------------------------------------------------------------
return 						 Functions results		def f(a, b, c=1, *d):
														return a+b+c+d[0]
--------------------------------------------------------------------------------
yield 						 Generator functions	def gen(n):
														for i in n: yield i*2
--------------------------------------------------------------------------------
global						 Namespaces				x = 'old' 
													def function():
														global x, y; x = 'new'
--------------------------------------------------------------------------------
nonlocal					 Namespaces (3.X)		def outer():
														x = 'old'
														def function():
															nonlocal x; x = 'new'
--------------------------------------------------------------------------------
import 						 Module access			import sys
--------------------------------------------------------------------------------
from 						 Attribute access		from sys import stdin
--------------------------------------------------------------------------------
class						 Building objects		class Subclass(Superclass):
														staticData = [] 
														def method(self): pass
--------------------------------------------------------------------------------
try/except/ finally			 Catching exceptions	try:
														action() 
													except:
														print('action error')
--------------------------------------------------------------------------------
raise 						 Triggering exceptions	raise EndSearch(location)
--------------------------------------------------------------------------------
assert 						 Debugging checks		assert X > Y, 'X too small'
--------------------------------------------------------------------------------
with/as						 Context managers 		with open('data') as myfile:
							 (3.X, 2.6+)				process(myfile)
--------------------------------------------------------------------------------
del							 Deleting references	del data[k] 
													del data[i:j] 
													del obj.attr 
													del variable
```

Python 3.X’s statements, Here are a few fine points about its content:

- Assignment statements come in a variety of syntax flavors, sequence, augmented, and more.


- `print` is technically neither a reserved word nor a statement in 3.X, but a built-in function call; because it will nearly always be run as an expression statement, though (and often on a line by itself), it’s generally thought of as a statement type.


- `yield` is also an expression instead of a statement as of 2.5; like print, it’s typically used as an expression statement and so is included in this table, but scripts occasionally assign or otherwise use its result. As an expression, `yield` is also a reserved word, unlike print.

Python 2.X, here are a few notes for your Python:

- In 2.X, `nonlocal` is not available, there are alternative ways to achieve this statement’s writeable state-retention effect.
- In 2.X, `print` is a statement instead of a built-in function call.
- In 2.X, the 3.X `exec` code execution built-in function is a statement, with specific syntax; since it supports enclosing parentheses, though, you can generally use its. 3.X call form in 2.X code.


- In 2.5, the `try` / `except` and `try` / `finally` statements were merged: the two were formerly separate statements, but we can now say both `except` and `finally` in the same `try` statement.


- In 2.5, `with` / `as` is an optional extension, and it is not available unless you explicitly turn it on by running the statement from `__future__ import with_statement` .

the following if statement, coded in a C-like language:

```
if (x > y) { 
	x = 1; 
	y = 2; 
}

# This might be a statement in C, C++, Java, JavaScript, or similar.
```

the equivalent statement in the Python language:

```
if x > y: 
	x = 1 
	y = 2
```



### the colon `:` character 

**All Python compound statements**—statements that have other statements nested inside them—**follow the same general pattern of a header line terminated in a colon**, **followed by a nested block of code usually indented underneath the header line**, like this:

```
Header line:
	Nested statement block
```



### Parentheses `()` are optional

> The parentheses here are required by the syntax of many C-like languages
>
> ```
> if (x < y)
> ```

In Python, we simply omit the parentheses, and the statement works the same way:

```
if x < y
```

Technically speaking, because **every expression can be enclosed in parentheses**, including them will not hurt in this Python code, and they are not treated as an error if present. **But don’t do that**.



### End-of-line is end of statement

> You don’t need to terminate statements with semicolons in Python the way you do in C-like languages:
>
> ```
> x = 1;
> ```

In Python, the general rule is that **the end of a line automatically terminates the statement that appears on that line**. In other words, you can leave off the semicolons, and it works the same way:

```
x = 1
```

write one statement per line for the vast majority of Python code, and no semicolon is required.

**you can continue to use semicolons at the end of each statement**—the language lets you get away with them if they are present, **because the semicolon is also a separator when statements are combined.But don’t do that**



### End of indentation is end of block

> You don’t need to include begin/end, then/endif, or braces around the nested block, as you do in C-like languages:
>
> ```
> if (x > y) { 
> 	x = 1; 
> 	y = 2; 
> }
> ```

in Python, we consistently indent all the statements in a given single nested block the same distance to the right, and **Python uses the statements’ physical indentation to determine where the block starts and stops**:

```
if x > y: 
	x = 1 
	y = 2
```

By indentation, I mean the blank whitespace all the way to the left of the two nested statements here. Python doesn’t care how you indent (you may use either spaces or tabs), or how much you indent (you may use any number of spaces or tabs). In fact, the indentation of one nested block can be totally different from that of another. The syntax rule is only that for **a given single nested block, all of its statements must be indented the same distance to the right. If this is not the case, you will get a syntax error**, and your code will not run until you repair its indentation to be consistent.

### Indentation Syntax

- **aligning your code according to its logical structure is a major part of making it readable, and thus reusable and maintainable, by yourself and others.**

- Python is a WYSIWYG language—what you see is what you get—because the way code looks is the way it runs, regardless of who coded it.

  > ```
  > if x:
  > 	if y:
  > 		statement1
  > else:
  > 	statement2
  > ```
  >
  > In this example, the if that the else lines up with vertically is the one it is associated with logically (the outer if x). In a sense, 


- As a rule of thumb, **you probably shouldn’t mix tabs and spaces in the same block in Python**, unless you do so consistently; use tabs or spaces in a given block, but not both (in fact, Python 3.X now issues an error for inconsistent use of tabs and spaces). Then again, you probably shouldn’t mix tabs or spaces in indentation in any structured language—such code can cause major readability issues if the next programmer has his or her editor set to display tabs differently than yours.




### Statement rule special cases

#### statement separators `;`

Although statements normally appear one per line, it is possible to squeeze more than one statement onto a single line in Python by separating them with semicolons:

```
a = 1; b = 2; print(a + b)			# Three statements on one line
```

This is the only place in Python where semicolons are required: **as statement separators**.**This only works**, though, **if the statements thus combined are not themselves compound statements**. In other words, you can chain together only simple statements, like assignments, prints, and function calls.

> Compound statements like if tests and while loops must still appear on lines of their own



#### make a single statement span across multiple lines.

To make this work, you simply have to enclose part of your statement in a bracketed pair—parentheses ( `()` ), square brackets ( `[]` ), or curly braces ( `{}` ). **Any code enclosed in these constructs can cross multiple lines: your statement doesn’t end until Python reaches the line containing the closing part of the pair**. For instance, to continue a list literal:

```
mylist = [1111, 
		  2222, 
		  3333]
```

The curly braces surrounding dictionaries (as well as set literals and dictionary and set comprehensions in 3.X and 2.7) allow them to span lines this way too, and parentheses handle tuples, function calls, and expressions. **The indentation of the continuation lines does not matter**, though common sense dictates that the lines should be aligned somehow for readability.

**Parentheses are the catchall device**—because any expression can be wrapped in them, simply inserting a left parenthesis allows you to drop down to the next line and continue your statement:

```
X = (A + B + 
	 C + D)
```

```
if (A == 1 and
	B == 2 and 
	C == 3):
		print('spam' * 3)
```

> An older rule also allows for continuation lines when the prior line ends in a backslash: don't do this
>
> ```
> X = A + B + \ 
> 	C + D			# An error-prone older alternative
> ```

#### Block rule special case

As one special case here, the body of a compound statement can instead appear on the same line as the header in Python, after the colon:

```
if x > y: print(x)
```

> - this will work only if the body of the compound statement itself does not contain any compound statements. only simple statements.
> - Extra parts of compound statements (such as the else part of an if, which we’ll meet in the next section) must also be on separate lines of their own.
> - Compound statement bodies can also consist of multiple simple statements separated by semicolons, but this tends to be frowned upon.



# Assignments, Expressions, and Prints



## Assignment Statements

In its basic form, you write the target of an assignment on the left of an equals sign, and the object to be assigned on the right. The target on the left may be a name or object component, and the object on the right can be an arbitrary expression that computes an object.

- **Assignments create object references.**

  > Python assignments store references to objects in names or data structure components. They always create references to objects instead of copying the objects. Because of that, Python variables are more like pointers than data storage areas.


- **Names are created when first assigned.** 

  > Python creates a variable name the first time you assign it a value (i.e., an object reference), so there’s no need to predeclare names ahead of time. Some (but not all) data structure slots are created when assigned, too (e.g., dictionary entries, some object attributes). Once assigned, a name is replaced with the value it references whenever it appears in an expression.


- **Names must be assigned before being referenced.** 

  > It’s an error to use a name to which you haven’t yet assigned a value. Python raises an exception if you try, rather than returning some sort of ambiguous default value. This turns out to be crucial in Python because names are not predeclared—if Python provided default values for unassigned names used in your program instead of treating them as errors, it would be much more difficult for you to spot name typos in your code.


- **Some operations perform assignments implicitly.** 

  > In this section we’re concerned with the `=` statement, but assignment occurs in many contexts in Python. For instance, we’ll see later that module imports, function and class definitions, for loop variables, and function arguments are all implicit assignments. Because assignment works the same everywhere it pops up, all these contexts simply bind names to object references at runtime.

### Assignment statement forms

```
Assignment statement forms

================================================================================
Operation						Interpretation
================================================================================
spam = 'Spam' 					Basic form
--------------------------------------------------------------------------------
spam, ham = 'yum', 'YUM' 		Tuple assignment (positional)
--------------------------------------------------------------------------------
[spam, ham] = ['yum', 'YUM'] 	List assignment (positional)
--------------------------------------------------------------------------------
a, b, c, d = 'spam' 			Sequence assignment, generalized
--------------------------------------------------------------------------------
a, *b = 'spam' 					Extended sequence unpacking (Python 3.X)
--------------------------------------------------------------------------------
spam = ham = 'lunch' 			Multiple-target assignment
--------------------------------------------------------------------------------
spams += 42				Augmented assignment (equivalent to spams = spams + 42)
```

### Tuple- and list-unpacking assignments

The second and third forms in the table are related. When you code a tuple or list on the left side of the `=` , Python pairs objects on the right side with targets on the left by position and assigns them from left to right. For example, in the second line of Table , the name `spam` is assigned the string `'yum'` , and the name `ham` is bound to the string  `'YUM'`. In this case Python internally may make a tuple of the items on the right, which is why this is called tuple-unpacking assignment.

```
>>> spam, ham = 'yum', 'YUM'			# Tuple assignment (positional)
>>> spam, ham
('yum', 'YUM')

>>> [spam, ham] = ['yum', 'YUM']		# List assignment (positional)
>>> [spam, ham]
['yum', 'YUM']
```

### Sequence assignments

In later versions of Python, tuple and list assignments were generalized into instances of what we now call **sequence assignment** — **any sequence of names can be assigned to any sequence of values, and Python assigns the items one at a time by position**. We can even mix and match the types of the sequences involved. The fourth line in Table, for example, pairs a tuple of names with a string of characters: `a` is assigned `'s'` , `b` is assigned `'p'` , and so on.

```
>>> a, b, c, d = 'spam'
>>> a
's'
>>> b
'p'
>>> c
'a'
>>> d
'm'
```

**sequence-unpacking assignments**：

```
>>> nudge = 1					# Basic assignment
>>> wink = 2
>>> A, B = nudge, wink			# Tuple assignment
>>> A, B 						# Like A = nudge; B = wink
(1, 2)
>>> [C, D] = [nudge, wink]		# List assignment
>>> C, D 
(1, 2)
```

> two tuples in the third line in this interaction—we’ve just omitted their enclosing parentheses.

Python pairs the values in the tuple on the right side of the assignment operator with the variables in the tuple on the left side and assigns the values one at a time.

Because Python creates a temporary tuple that saves the original values of the variables on the right while the statement runs, unpacking assignments are also a way to swap two variables’ values without creating a temporary variable of your own—the tuple on the right remembers the prior values of the variables automatically

**the original tuple and list assignment forms in Python have been generalized to accept any type of sequence (really, iterable) on the right as long as it is of the same length as the sequence on the left.**

Python assigns items in the sequence on the right to variables in the sequence on the left by position, from left to right:

```
>>> [a, b, c] = (1, 2, 3)		# Assign tuple of values to list of names
>>> a, c 
(1, 3)
>>> (a, b, c) = "ABC"			# Assign string of characters to tuple
>>> a, c 
('A', 'C')
```

Technically speaking, **sequence assignment actually supports any iterable object on the right**, not just any sequence.



### Advanced sequence assignment patterns

around the `=` symbol, **sequence assignments must generally have the same number of items on the right as we have variables on the left, or we’ll get an error**.

```
>>> string = 'SPAM'
>>> a, b, c, d = string			# Same number on both sides
>>> a, d 
('S', 'M')

>>> a, b, c = string 			# Error if not
...error text omitted...
ValueError: too many values to unpack (expected 3)
```

There are a variety of ways to employ slicing to make this last case work:

```
>>> string = 'SPAM'
>>> a, b, c = string[0], string[1], string[2:]		# Index and slice
>>> a, b, c 
('S', 'P', 'AM')

>>> a, b, c = list(string[:2]) + [string[2:]]		# Slice and concatenate
>>> a, b, c 
('S', 'P', 'AM')

>>> a, b = string[:2]								# Same, but simpler
>>> c = string[2:]
>>> a, b, c 
('S', 'P', 'AM')

>>> (a, b), c = string[:2], string[2:]				# Nested sequences
>>> a, b, c 
('S', 'P', 'AM')
```

assign nested sequences:

```
>>> ((a, b), c) = ('SP', 'AM')					# Paired by shape and position
>>> a, b, c 
('S', 'P', 'AM')
# the sequence-nesting shape of the object on the left must match that of the object on the right.


for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: ...		# Simple tuple assignment
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: ...	# Nested tuple assignment

 
```

we’ll also see that this nested tuple (really, sequence) unpacking assignment form works for function argument lists in Python 2.X (though not in 3.X), because function arguments are passed by assignment as well:

```
def f(((a, b), c)): ... 		# For arguments too in Python 2.X, but not 3.X
f(((1, 2), 3))
```

assigning an integer series to a set of variables:

```
>>> red, green, blue = range(3)
>>> red, blue 
(0, 2)
```

Another place you may see a tuple assignment at work is for splitting a sequence into its front and the rest in loops like this:

```
>>> L = [1, 2, 3, 4]
>>> while L:
... 	front, L = L[0], L[1:] 		# See next section for 3.X * alternative
... 	print(front, L) 
...
1 [2, 3, 4] 
2 [3, 4] 
3 [4] 
4 []
```

> The tuple assignment in the loop here could be coded as the following two lines instead, but it’s often more convenient to string them together:
>
> ```
> ...		front = L[0]
> ...		L = L[1:]
> ```

Notice that this code is using the list as a sort of stack data structure, which can often **also be achieved with the `append` and `pop` methods of list objects**; here, **`front = L.pop(0)` would have much the same effect as the tuple assignment statement**, but it would be an in-place change.









### Extended sequence unpacking

In Python 3.X (only), a new form of sequence assignment allows us to be more flexible in how we select portions of a sequence to assign. The fifth line in Table, for example, matches a with the first character in the string on the right and b with the rest: `a` is assigned `'s'`, and `b` is assigned `'pam'` . This provides a simpler alternative to assigning the results of manual slicing operations.

```
>>> a, *b = 'spam' 
>>> a
's'
>>> b
['p', 'a', 'm']
```

**In Python 3.X, though, we can use a single starred name in the target to match more generally:**

```
>>> seq = [1, 2, 3, 4]
>>> a, *b = seq
>>> a
1
>>> b
[2, 3, 4]
```

**When a starred name is used, the number of items in the target on the left need not match the length of the subject sequence**:

```
>>> seq = [1, 2, 3, 4]
>>> *a, b = seq
>>> a
[1, 2, 3]
>>> b
4

>>> a, b, *c = seq
>>> a
1
>>> b
2
>>> c
[3, 4]
```

This is similar in spirit to slicing, but not exactly the same—**a sequence unpacking assignment always returns a list for multiple matched items**, whereas **slicing returns a sequence of the same type as the object sliced**:

```
>>> a, *b = 'spam'			# * assignment always returns a list
>>> a, b
('s', ['p', 'a', 'm'])
>>> a, *b, c = 'spam'
>>> a, b, c
('s', ['p', 'a'], 'm')

>>> S = 'spam'
>>> S[0], S[1:] 			# Slices are type-specific, 
('s', 'pam')
>>> S[0], S[1:3], S[3] 
('s', 'pa', 'm')
```

**the starred name may match just a single item, but is always assigned a list**. example:

```
>>> L = [1, 2, 3, 4]
>>> while L:
...     front, *L = L			# Get first, rest without slicing
...     print(front, L)
... 
1 [2, 3, 4]
2 [3, 4]
3 [4]
4 []
```

**if there is nothing left to match the starred name, it is assigned an empty list, regardless of where it appears**:

```
>>> seq = [1, 2, 3, 4]

>>> a, b, c, d, *e = seq
>>> print(a, b, c, d, e) 
1 2 3 4 []

>>> a, b, *e, c, d = seq
>>> print(a, b, c, d, e) 
1 2 3 4 []
```

**errors can still be triggered if there is more than one starred name, if there are too few values and no star (as before), and if the starred name is not itself coded inside a sequence:**

```
>>> a, *b, c, *d = seq 
SyntaxError: two starred expressions in assignment

>>> a, b = seq 
ValueError: too many values to unpack (expected 2)

>>> *a = seq 
SyntaxError: starred assignment target must be in a list or tuple

>>> *a, = seq
>>> a 
[1, 2, 3, 4]
```

In Python 3.X, extended assignments may show up after the word for, where a simple variable name is more commonly used:

```
>>> for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:		# (a, *b, c) = (1, 2, 3, 4)...
...     print(a, b, c)
... 
1 [2, 3] 4
5 [6, 7] 8
```



### Multiple-target assignments 

The sixth line in Table shows the multiple-target form of assignment. In this form, Python assigns a reference to the same object (the object farthest to the right) to all the targets on the left. In the table, the names `spam` and `ham` are both assigned references to the same string object, `'lunch'`. The effect is the same as if we had coded `ham = 'lunch'` followed by `spam = ham`, as `ham` evaluates to the original string object (i.e., not a separate copy of that object).

```
>>> spam = ham = 'lunch'
>>> spam
'lunch'
>>> ham
'lunch'

spam = ham = 'lunch'
equivalent to:
ham = 'lunch'
spam = ham
```

### Multiple-target assignment and shared references

Keep in mind that **there is just one object here, shared by all three variables (they all wind up pointing to the same object in memory). This behavior is fine for immutable types**

```
>>> a = b = 0
>>> b = b + 1
>>> a, b 
(0, 1)

# As long as the object assigned is immutable, it’s irrelevant if more than one name references it.
```

we have to **be more cautious when initializing variables to an empty mutable object such as a list or dictionary**:

```
>>> a = b = []
>>> b.append(42)
>>> a, b 
([42], [42])

# because a and b reference the same object, appending to it in place through b will impact what we see through a as well.
```

initialize mutable objects in separate statements:

```
>>> a = []
>>> b = []				# a and b do not share the same object
>>> b.append(42)
>>> a, b 
([], [42])

>>> a, b = [], []		# a and b do not share the same object
```



### Augmented assignments 

The last line in Table is an example of augmented assignment—a shorthand that combines an expression and an assignment in a concise way. Saying `spam += 42`, for example, has the same effect as `spam = spam + 42` , but the augmented form requires less typing and is generally quicker to run. In addition, if the subject is mutable and supports the operation, an augmented assignment may run even quicker by choosing an in-place update operation instead of an object copy. There is one augmented assignment statement for every binary expression operator in Python.

```
spam += 42

equivalent to:
spam = spam + 42
```
Known as **augmented assignments**, and borrowed from the C language. They **imply the combination of a binary expression and an assignment**.

```
the following two formats are roughly equivalent:

X = X + Y 			# Traditional form
X += Y				# Newer augmented form
```

Augmented assignment statements:

```
X += Y 			X *= Y 			X %= Y
X &= Y 			X ^= Y 			X <<= Y
X −= Y 			X /= Y 			X **= Y
X |= Y 			X >>= Y 		X //= Y
```

**Augmented assignments have three advantages**:

1. **There’s less for you to type**. Need I say more?

2. **The left side has to be evaluated only once**. In X += Y, X may be a complicated object expression. In the augmented form, its code must be run only once. However, in the long form, X = X + Y, X appears twice and must be run twice. Because of this, augmented assignments usually run faster.

3. **The optimal technique is automatically chosen**. That is, for objects that support in-place changes, the augmented forms automatically perform in-place change operations instead of slower copies.

   ```
   >>> L = [1, 2]
   >>> L = L + [3]			# Concatenate: slower
   >>> L 
   [1, 2, 3]
   >>> L.append(4)			# Faster, but in place
   >>> L 
   [1, 2, 3, 4]
   ```
   - For augmented assignments, in-place operations may be applied for mutable objects as an optimization.



- **Concatenation operations must create a new object**, copy in the list on the left, and then copy in the list on the right.



- **in-place method calls simply add items at the end of a memory block**.


**Augmented assignment and shared references**:

```
>>> L = [1, 2]
>>> M = L						# L and M reference the same object
>>> L = L + [3, 4]				# Concatenation makes a new object
>>> L, M 						# Changes L but not M
([1, 2, 3, 4], [1, 2])

>>> L = [1, 2]
>>> M = L
>>> L += [3, 4]					# But += really means extend
>>> L, M 						# M sees the in-place change too!
([1, 2, 3, 4], [1, 2, 3, 4])
```

- **This only matters for mutables like lists and dictionaries**


- **!!! Concatenation makes a new object** : `L = L + [3, 4]`


- **!!! `+=`  in-place change really means extend **: `L += [3, 4]`	

make copies of your mutable objects if you need to break the shared reference structure.



## Expression Statements

**you can use an expression as a statement, on a line by itself**. But because the result of the expression won’t be saved, it usually makes sense to do so only if the expression does something useful as a side effect.

 Expressions are commonly used as statements in two situations:

- **For calls to functions and methods** 

  > **Some functions and methods do their work without returning a value.** Such functions are sometimes called procedures in other languages. Because they don’t return values that you might be interested in retaining, you can call these functions with expression statements.


- **For printing values at the interactive prompt** 

  > **Python echoes back the results of expressions typed at the interactive command line**. Technically, these are expression statements, too; they serve as a shorthand for typing print statements.

Common Python expression statements (expressions that evaluate to objects):

```
# Common Python expression statements (expressions that evaluate to objects)

Operation					Interpretation

spam(eggs, ham) 			Function calls
spam.ham(eggs) 				Method calls
spam 						Printing variables in the interactive interpreter
print(a, b, c, sep='') 		Printing operations in Python 3.X
yield x ** 2				Yielding expression statements
```



### Expression Statements and In-Place Changes

Expression statements are often used to run list methods that change a list in place:

```
>>> L = [1, 2]
>>> L.append(3)		# Append is an in-place change
>>> L 
[1, 2, 3]
```

**!!! Calling an in-place change operation** such as `append` , `sort` , or `reverse` on a list always changes the list in place, but **these methods do not return the list they have changed; instead, they return the None object.**

> ```
> >>> L = L.append(4)		# But append returns None, not L
> >>> print(L) 			# So we lose our list!
> None
> ```



## Print Operations

### ...

### ...

### ...





# Python Syntax Revisited

- **Statements execute one after another, until you say otherwise.** 

  > Python normally runs statements in a file or nested block in order from first to last as a sequence, but statements like `if` (as well as loops and exceptions) cause the interpreter to jump around in your code. Because Python’s path through a program is called the control flow, statements such as `if` that affect it are often called control-flow statements.


- **Block and statement boundaries are detected automatically.**

  >  As we’ve seen, there are no braces or “begin/end” delimiters around blocks of code in Python; instead, Python uses the indentation of statements under a header to group the statements in a nested block. Similarly, Python statements are not normally terminated with semicolons; rather, the end of a line usually marks the end of the statement coded on that line. As a special case, statements can span lines and be combined on a line with special syntax.


- **Compound statements = header + “`:`” + indented statements.** 

  > All Python compound statements—those with nested statements—follow the same pattern: a header line terminated with a colon, followed by one or more nested statements, usually indented under the header. The indented statements are called a block (or sometimes, a suite). In the `if` statement, the `elif` and `else` clauses are part of the `if`, but they are also header lines with nested blocks of their own. As a special case, blocks can show up on the same line as the header if they are simple noncompound code.


- **Blank lines, spaces, and comments are usually ignored.** 

  > Blank lines are both optional and ignored in files (but not at the interactive prompt, when they terminate compound statements). Spaces inside statements and expressions are almost always ignored (except in string literals, and when used for indentation). Comments are always ignored: they start with a # character (not inside a string literal) and extend to the end of the current line.


- **Docstrings are ignored but are saved and displayed by tools.**

  >  Python supports an additional comment form called documentation strings (docstrings for short), which, unlike # comments, are retained at runtime for inspection. Docstrings are simply strings that show up at the top of program files and some statements. Python ignores their contents, but they are automatically attached to objects at runtime and may be displayed with documentation tools like PyDoc. Docstrings are part of Python’s larger documentation strategy



### Block Delimiters: Indentation Rules

Python detects block boundaries automatically, by line indentation—that is, the empty space to the left of your code. All statements indented the same distance to the right belong to the same block of code.

Indentation is simpler in practice than its details might initially imply, and it makes your code reflect its logical structure.



### Avoid mixing tabs and spaces: New error checking in 3.X

In fact, Python 3.X issues an error, for these very reasons, when a script mixes tabs and spaces for indentation inconsistently within a block (that is, in a way that makes it dependent on a tab’s equivalent in spaces). Python 2.X allows such scripts to run, but it has a `-t` command-line flag that will warn you about inconsistent tab usage and a `-tt` flag that will issue errors for such code (you can use these switches in a command line like `python –t main.py` in a system shell window). Python 3.X’s error case is equivalent to 2.X’s `-tt` switch.



### Statement Delimiters: Lines and Continuations

A statement in Python normally ends at the end of the line on which it appears. When a statement is too long to fit on a single line, though, a few special rules may be used to make it span multiple lines:

- **Statements may span multiple lines if you’re continuing an open syntactic pair.** 

  > Python lets you continue typing a statement on the next line if you’re coding something enclosed in a `()` , `{}` , or `[]` pair. For instance, expressions in parentheses and dictionary and list literals can span any number of lines; your statement doesn’t end until the Python interpreter reaches the line on which you type the closing part of the pair ( a `)` , `}` , or `]` ). Continuation lines—lines 2 and beyond of the statement —can start at any indentation level you like, but you should try to make them align vertically for readability if possible. This open pairs rule also covers set and dictionary comprehensions in Python 3.X and 2.7.


- **Statements may span multiple lines if they end in a backslash.**

  >  This is a somewhat outdated feature that’s not generally recommended, but if a statement needs to span multiple lines, you can also add a backslash (a `\` not embedded in a string literal or comment) at the end of the prior line to indicate you’re continuing on the next line. Because you can also continue by adding parentheses around most con-structs, backslashes are rarely used today. This approach is also error-prone: accidentally forgetting a `\` usually generates a syntax error and might even cause the next line to be silently mistaken (i.e., without warning) for a new statement, with unexpected results.


- **Special rules for string literals.**

  > triple-quoted string blocks are designed to span multiple lines normally.  adjacent string literals are implicitly concatenated; when it’s used in conjunction with the open pairs rule mentioned earlier, wrapping this construct in parentheses allows it to span multiple lines.


- **you can terminate a statement with a semi-colon**

  > this convention is sometimes used to squeeze more than one simple (non-compound) statement onto a single line. Also, 


- comments and blank lines can appear anywhere in a file; comments (which begin with a # character) terminate at the end of the line on which they appear.



### A Few Special Cases

Here’s what a continuation line looks like using the open syntactic pairs rule just described. Delimited constructs, such as lists in square brackets, can **span across any number of lines**:

```
L = ["Good", 
	 "Bad", 
	 "Ugly"]		# Open pairs may span lines
```

> This also **works for anything in parentheses (expressions, function arguments, function headers, tuples, and generator expressions)**, as well as **anything in curly braces (dictionaries and, in 3.X and 2.7, set literals and set and dictionary comprehensions)**

**wrap a part of your statement in parentheses**:

```
if (a == b and c == d and 
	d == e and e == f): 
	print('new')				# But parentheses usually do too, and are obvious
```

> If you like using backslashes to continue lines, you can, but it’s not common practice in Python:
>
> ```
> if a == b and c == d and 	\
>    d == e and f == g: 
>    print('olde')				# Backslashes allow continuations...
> ```
> backslashes are too easy to not notice and too easy to omit altogether

Python lets you move a compound statement’s body up to the header line, provided the body contains just simple (noncompound) statements.

```
if 1: print('hello')		# Simple statement on header line
```







