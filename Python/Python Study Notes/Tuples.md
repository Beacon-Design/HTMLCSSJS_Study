

# Tuples

- **Ordered collections of arbitrary objects** 

  Like strings and lists, tuples are positionally ordered collections of objects (i.e., they maintain a left-to-right order among their contents); like lists, they can embed any kind of object.


- **Accessed by offset** 

  Like strings and lists, items in a tuple are accessed by offset (not by key); they support all the offset-based access operations, such as indexing and slicing.


- **Of the category “immutable sequence”** 

  Like strings and lists, tuples are sequences; they support many of the same operations. However, like strings, tuples are immutable; they don’t support any of the in-place change operations applied to lists.


- **Fixed-length, heterogeneous, and arbitrarily nestable** 

  Because tuples are immutable, you cannot change the size of a tuple without making a copy. On the other hand, tuples can hold any type of object, including other compound objects (e.g., lists, dictionaries, other tuples), and so support arbitrary nesting.


- **Arrays of object references** 

  Like lists, tuples are best thought of as object reference arrays; tuples store access points to other objects (references), and indexing a tuple is relatively quick.

A tuple is written as a series of objects (technically, expressions that generate objects), separated by commas and normally enclosed in parentheses. An empty tuple is just a parentheses pair with nothing inside.

### Common tuple literals and operations

```
Common tuple literals and operations

Operation						Interpretation

() 								An empty tuple
T = (0,) 						A one-item tuple (not an expression)
T = (0, 'Ni', 1.2, 3) 			A four-item tuple
T = 0, 'Ni', 1.2, 3				Another four-item tuple (same as prior line)
T = ('Bob', ('dev', 'mgr')) 	Nested tuples
T = tuple('spam') 				Tuple of items in an iterable
T[i] 							Index, index of index, slice, length
T[i][j] 
T[i:j] 
len(T) 
T1 + T2 						Concatenate, repeat
T * 3 
for x in T: print(x) 			Iteration, membership
'spam' in T 
[x ** 2 for x in T]
T.index('Ni')					Methods in 2.6, 2.7, and 3.X: search, count
T.count('Ni') 
namedtuple('Emp', ['name', 'jobs'])		Named tuple extension type
```

### sequence operations

```
>>> (1, 2) + (3, 4) 			# Concatenation
(1, 2, 3, 4)

>>> (1, 2) * 4 					# Repetition
(1, 2, 1, 2, 1, 2, 1, 2)

>>> T = (1, 2, 3, 4)			# Indexing, slicing
>>> T[0], T[1:3] 
(1, (2, 3))
```

### Tuple syntax peculiarities: Commas and parentheses

If you really want a single-item tuple, simply add a trailing comma after the single item, before the closing parenthesis:

```
>>> x = (40)				# An integer!
>>> x 
40

>>> y = (40,)				# A tuple containing an integer
>>> y 
(40,)
```

Python also allows you to omit the opening and closing parentheses for a tuple in contexts where it isn’t syntactically ambiguous to do so.

**The most common places where the parentheses are required for tuple literals are those where:**

- Parentheses matter—within a function call, or nested in a larger expression.


- Commas matter—embedded in the literal of a larger data structure like a list or dictionary, or listed in a Python 2.X print statement.

### Conversions, methods, and immutability

tuple operations are identical to string and list operations. The only differences worth noting are that **the `+` , `*` , and slicing operations return new tuples when applied to tuples**, and that tuples don’t provide the same methods you saw for strings, lists, and dictionaries.

If you want to sort a tuple, for example, you’ll usually have to either first convert it to a list to gain access to a sorting method call and make it a mutable object, or use the newer sorted built-in that accepts any sequence object 

```
>>> T = ('cc', 'aa', 'dd', 'bb')
>>> tmp = list(T)					# Make a list from a tuple's items
>>> tmp.sort()						# Sort the list
>>> tmp 
['aa', 'bb', 'cc', 'dd']
>>> T = tuple(tmp)					# Make a tuple from the list's items
>>> T 
('aa', 'bb', 'cc', 'dd')
>>> sorted(T) 						# Or use the sorted built-in, and save two steps
['aa', 'bb', 'cc', 'dd']
```

List comprehensions can also be used to convert tuples:

```
>>> T = (1, 2, 3, 4, 5)
>>> L = [x + 20 for x in T]
>>> L 
[21, 22, 23, 24, 25]
```

List comprehensions are really sequence operations—they always build new lists, but they may be used to iterate over any sequence objects, including tuples, strings, and other lists. As we’ll see later in the book, they even work on some things that are not physically stored sequences—any iterable objects will do, including files, which are automatically read line by line. Given this, they may be better called iteration tools.

**index and count**

```
>>> T = (1, 2, 3, 2, 4, 2)		# Tuple methods in 2.6, 3.0, and later
>>> T.index(2) 					# Offset of first appearance of 2
1
>>> T.index(2, 2) 				# Offset of appearance after offset 2
3
>>> T.count(2) 					# How many 2s are there?
3
```

the rule about tuple immutability applies only to the top level of the tuple itself, not to its contents. A list inside a tuple, for instance, can be changed as usual:

```
>>> T = (1, [2, 3], 4)
>>> T[1] = 'spam' 				# This fails: can't change tuple itself 
TypeError: object doesn't support item assignment

>>> T[1][0] = 'spam'			# This works: can change mutables inside
>>> T 
(1, ['spam', 3], 4)
```



### Records Revisited: Named Tuples

```
>>> bob = ('Bob', 40.5, ['dev', 'mgr'])		# Tuple record
>>> bob 
('Bob', 40.5, ['dev', 'mgr'])

>>> bob[0], bob[2] 							# Access by position
('Bob', ['dev', 'mgr'])
```

the same record recoded as a dictionary with named fields:

```
>>> bob = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])	# Dictionary record
>>> bob 
{'jobs': ['dev', 'mgr'], 'name': 'Bob', 'age': 40.5}

>>> bob['name'], bob['jobs'] 								# Access by key
('Bob', ['dev', 'mgr'])

>>> tuple(bob.values()) 									# Values to tuple
(['dev', 'mgr'], 'Bob', 40.5)
>>> list(bob.items()) 										# Items to tuple list
[('jobs', ['dev', 'mgr']), ('name', 'Bob'), ('age', 40.5)]
```

named tuples are a tuple/class/dictionary hybrid. They also represent a classic tradeoff.(In short, named tuples build new classes that extend the tuple type, inserting a property accessor method for each named field that maps the name to its position)

```
>>> from collections import namedtuple					# Import extension type
>>> Rec = namedtuple('Rec', ['name', 'age', 'jobs'])	# Make a generated class
>>> bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])		# A named-tuple record
>>> bob 
Rec(name='Bob', age=40.5, jobs=['dev', 'mgr'])

>>> bob[0], bob[2] 										# Access by position
('Bob', ['dev', 'mgr'])
>>> bob.name, bob.jobs 									# Access by attribute
('Bob', ['dev', 'mgr'])

>>> O = bob._asdict()									# Dictionary-like form
>>> O['name'], O['jobs'] 								# Access by key too
('Bob', ['dev', 'mgr'])
>>> O 
OrderedDict([('name', 'Bob'), ('age', 40.5), ('jobs', ['dev', 'mgr'])])
```

the positional initial values here: named tuples accept these by name, position, or both:

```
>>> bob = Rec('Bob', 40.5, ['dev', 'mgr'])		# For both tuples and named tuples
>>> name, age, jobs = bob						# Tuple assignment
>>> name, jobs 
('Bob', ['dev', 'mgr'])

>>> for x in bob: print(x) 						# Iteration context
...prints Bob, 40.5, ['dev', 'mgr']...
```



```
>>> bob = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
>>> job, name, age = bob.values()
>>> name, job 									# Dict equivalent (but order may vary) 
('Bob', ['dev', 'mgr'])

>>> for x in bob: print(bob[x]) 				# Step though keys, index values
...prints values...
>>> for x in bob.values(): print(x) 			# Step through values view
...prints values...
```



















### ...

### ...

### ...