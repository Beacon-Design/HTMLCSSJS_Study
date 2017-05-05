# Python Study Notes



# Dictionaries

1. dictionaries are unordered collections
2. in dictionaries, items are stored and fetched by key

**Accessed by key, not offset position**

> Dictionaries are sometimes called associative arrays or hashes (especially by users of other scripting languages). They associate a set of values with keys, so you can fetch an item out of a dictionary using the key under which you originally stored it. You use the same indexing operation to get components in a dictionary as you do in a list, but the index takes the form of a key, not a relative offset.

**Unordered collections of arbitrary objects** 

> Unlike in a list, items stored in a dictionary aren’t kept in any particular order; in fact, Python pseudo-randomizes their left-to-right order to provide quick lookup. Keys provide the symbolic (not physical) locations of items in a dictionary. 

**Variable-length, heterogeneous, and arbitrarily nestable** 

> Like lists, dictionaries can grow and shrink in place (without new copies being made), they can contain objects of any type, and they support nesting to any depth (they can contain lists, other dictionaries, and so on). Each key can have just one associated value, but that value can be a collection of multiple objects if needed, and a given value can be stored under any number of keys.

**Of the category “mutable mapping”** 

> You can change dictionaries in place by assigning to indexes (they are mutable), but they don’t support the sequence operations that work on strings and lists. Because dictionaries are unordered collections, operations that depend on a fixed positional order (e.g., concatenation, slicing) don’t make sense. Instead, dictionaries are the only built-in, core type representatives of the mapping category—objects that map keys to values. Other mappings in Python are created by imported modules.

**Tables of object references (hash tables)** 

> If lists are arrays of object references that support access by position, dictionaries are unordered tables of object references that support access by key. Internally, dictionaries are implemented as hash tables (data structures that support very fast retrieval), which start small and grow on demand. Moreover, Python employs optimized hashing algorithms to find keys, so retrieval is quick. Like lists, **dictionaries store object references** (not copies, unless you ask for them explicitly).

a dictionary is written as a series of key:value pairs, separated by commas, enclosed in curly braces. 4 An empty dictionary is an empty set of braces, and you can nest dictionaries by simply coding one as a value inside another dictionary, or within a list or tuple.

## Common dictionary literals and operations

see the library manual or run a `dir(dict)` or `help(dict)` call for a complete list—dict is the name of the type.

```
Common dictionary literals and operations

Operation									Interpretation

D = {} 										Empty dictionary 
D = {'name': 'Bob', 'age': 40} 				Two-item dictionary
E = {'cto': {'name': 'Bob', 'age': 40}} 	Nesting
D = dict(name='Bob', age=40) 		Alternative construction techniques:
D = dict([('name', 'Bob'), ('age', 40)]) 	keywords, key
D = dict(zip(keyslist, valueslist)) 		value pairs, zipped key
D = dict.fromkeys(['name', 'age']) 			value pairs, key lists
D['name'] 									Indexing by key
E['cto']['age'] 
'age' in D									Membership: key present test
D.keys()									Methods: all keys,
D.values()									all values,
D.items()									all key+value tuples,
D.copy()									copy (top-level),
D.clear()									clear (remove all items),
D.update(D2)								merge by keys,
D.get(key, default?)		fetch by key, if absent default (or None),
D.pop(key, default?)		remove by key, if absent default (or error)
D.setdefault(key, default?) fetch by key, if absent set default (or 								None),
D.popitem()					remove/return any (key, value) pair; etc.
len(D) 						Length: number of stored entries
D[key] = 42 				Adding/changing keys
del D[key] 					Deleting entries by key
list(D.keys()) 				Dictionary views (Python 3.X)
D1.keys() & D2.keys()
D.viewkeys(), D.viewvalues() 		Dictionary views (Python 2.7)
D = {x: x*2 for x in range(10)}		Dictionary comprehensions (Python 										3.X, 2.7)
```



## Basic Dictionary Operations

you create dictionaries with literals and store and access items by key with indexing:

```
>>> D = {'spam': 2, 'ham': 1, 'eggs': 3}		# Make a dictionary
>>> D['spam']									# Fetch a value by key
2
>>> D 											# Order is "scrambled"
{'eggs': 3, 'spam': 2, 'ham': 1}

>>> len(D) 					# Number of entries in dictionary
3
>>> 'ham' in D 				# Key membership test alternative
True
>>> list(D.keys()) 			# Create a new list of D's keys
['eggs', 'spam', 'ham']
```

> keys in 3.X returns an iterable object, instead of a physical list. The list call forces it to produce all its values at once so we can print them interactively, though this call isn’t required some other contexts.
>
> In 2.X, keys builds and returns an actual list, so the list call isn’t even needed to display a result

### Changing Dictionaries in Place

```
>>> D 
{'eggs': 3, 'spam': 2, 'ham': 1}
>>> D['ham'] = ['grill', 'bake', 'fry']    # Change entry (value=list)
>>> D 
{'eggs': 3, 'spam': 2, 'ham': ['grill', 'bake', 'fry']}
>>> del D['eggs']						   # Delete entry
>>> D 
{'spam': 2, 'ham': ['grill', 'bake', 'fry']}
>>> D['brunch'] = 'Bacon' 				   # Add new entry
>>> D 
{'brunch': 'Bacon', 'spam': 2, 'ham': ['grill', 'bake', 'fry']}
```



### More Dictionary Methods

```
>>> D = {'spam': 2, 'ham': 1, 'eggs': 3}
>>> list(D.values()) 
[3, 2, 1]
>>> list(D.items()) 
[('eggs', 3), ('spam', 2), ('ham', 1)]

>>> D.get('spam') 				# A key that is there
2
>>> print(D.get('toast')) 		# A key that is missing
None
>>> D.get('toast', 88) 
88
```

The update method:

```
>>> D 
{'eggs': 3, 'spam': 2, 'ham': 1}
>>> D2 = {'toast':4, 'muffin':5}# Lots of delicious scrambled order here
>>> D.update(D2)
>>> D 
{'eggs': 3, 'muffin': 5, 'toast': 4, 'spam': 2, 'ham': 1}
```

### pop (Dictionary VS List)

```
# pop a dictionary by key
>>> D 
{'eggs': 3, 'muffin': 5, 'toast': 4, 'spam': 2, 'ham': 1}
>>> D.pop('muffin') 
5
>>> D.pop('toast') 				# Delete and return from a key 
4
>>> D 
{'eggs': 3, 'spam': 2, 'ham': 1}


# pop a list by position
>>> L = ['aa', 'bb', 'cc', 'dd']
>>> L.pop() 					# Delete and return from the end
'dd'
>>> L 
['aa', 'bb', 'cc']
>>> L.pop(1) 					# Delete from a specific position
'bb'
>>> L 
['aa', 'cc']
```



### Example: Movie Database

```
>>> table = {'1975': 'Holy Grail', 				# Key: Value
... 		 '1979': 'Life of Brian', 
... 		 '1983': 'The Meaning of Life'}
>>>
>>> year = '1983'
>>> movie = table[year]						# dictionary[Key] => Value
>>> movie 
'The Meaning of Life'
>>> for year in table:
...     print(year + '\t' + table[year]) 
...
1979 	Life of Brian 
1975	Holy Grail 
1983 	The Meaning of Life
```

> For any dictionary D, saying `for key in D:` works the same as saying the complete `for key in D.keys():` .



### Mapping values to keys

**in dictionaries, there’s just one value per key, but there may be many keys per value.**

```
>>> table = {'Holy Grail': '1975', 				# Key=>Value (title=>year)
... 		 'Life of Brian': '1979', 
... 		 'The Meaning of Life': '1983'}
>>>
>>> table['Holy Grail'] 
'1975'

>>> list(table.items()) 						# Value=>Key (year=>title) 
[('The Meaning of Life', '1983'), ('Holy Grail', '1975'), ('Life of Brian', '1979')]
>>> [title for (title, year) in table.items() if year == '1975'] 
['Holy Grail']
```

Note that both of the last two commands return a list of titles:

```
>>> K = 'Holy Grail'
>>> table[K] 				# Key=>Value (normal usage)
'1975'

>>> V = '1975'
>>> [key for (key, value) in table.items() if value == V] 		# Value=>Key 
['Holy Grail']
>>> [key for key in table.keys() if table[key] == V] 			# Ditto
['Holy Grail']
```



### Dictionary Usage Notes

1. Sequence operations don’t work.

   > Dictionaries are mappings, not sequences; because there’s no notion of ordering among their items, things like concatenation (an ordered joining) and slicing (extracting a contiguous section) simply don’t ap-ply.

2. Assigning to new indexes adds entries.

   > Keys can be created when you write a dictionary literal (embedded in the code of the literal itself), or when you assign values to new keys of an existing dictionary object individually. The end result is the same.

3. Keys need not always be strings.

   > any other immutable objects work, their values are “hashable” and thus won’t change.
   >
   > Mutable objects such as lists, sets, and other dictionaries don’t work as keys, but are allowed as values.



### Using dictionaries to simulate flexible lists: Integer keys

When you use lists, it is illegal to assign to an offset that is off the end of the list:

```
>>> L = []
>>> L[99] = 'spam' 
Traceback (most recent call last):
	File "<stdin>", line 1, in ?
IndexError: list assignment index out of range
```

By using integer keys, dictionaries can emulate lists that seem to grow on offset assignment:

```
>>> D = {}
>>> D[99] = 'spam'
>>> D[99] 
'spam'
>>> D 
{99: 'spam'}
```

another example:

```
>>> table = {1975: 'Holy Grail', 
... 		 1979: 'Life of Brian', 			# Keys are integers, not strings
... 		 1983: 'The Meaning of Life'}
>>> table[1975] 
'Holy Grail'
>>> list(table.items()) 
[(1979, 'Life of Brian'), (1983, 'The Meaning of Life'), (1975, 'Holy Grail')]
```



### Using dictionaries for sparse data structures: Tuple keys

In a similar way, dictionary keys are also commonly leveraged to implement sparse data structures.

```
>>> Matrix = {}
>>> Matrix[(2, 3, 4)] = 88
>>> Matrix[(7, 8, 9)] = 99
>>>
>>> X = 2; Y = 3; Z = 4			# ; separates statements:
>>> Matrix[(X, Y, Z)]
>>> Matrix 
{(2, 3, 4): 88, (7, 8, 9): 99}
```

we can use a simple two-item dictionary. In this scheme, accessing an empty slot triggers a nonexistent key exception, as these slots are not physically stored:

```
>>> Matrix[(2,3,6)] 
Traceback (most recent call last):
	File "<stdin>", line 1, in ? 
KeyError: (2, 3, 6)
```



### Avoiding missing-key errors

There are at least three ways to fill in a default value instead of getting such an error message:

1. you can test for keys ahead of time in `if` statements, 
2. use a `try` statement to catch and recover from the exception explicitly,
3. or simply use the dictionary `get` method shown earlier to provide a default for keys that do not exist.

the `get` method is the most concise in terms of coding requirements, but the `if` and `try` statements are much more general in scope

```
>>> if (2, 3, 6) in Matrix:				# Check for key before fetch
... 	print(Matrix[(2, 3, 6)]) 		
... else:
... 	print(0) 
...
0
>>> try:								# Try to index
... 	print(Matrix[(2, 3, 6)]) 
... except KeyError:					# Catch and recover
... 	print(0) 
...
0
>>> Matrix.get((2, 3, 4), 0) 			# Exists: fetch and return
88
>>> Matrix.get((2, 3, 6), 0) 			# Doesn't exist: use default arg
0
```



### Nesting in dictionaries

nests a list and a dictionary to represent structured property values:

```
>>> rec = {'name': 'Bob', 
... 	'jobs': ['developer', 'manager'], 
... 	'web': 'www.bobs.org/˜Bob', 
... 	'home': {'state': 'Overworked', 'zip': 12345}}
>>> rec['name'] 
'Bob'
>>> rec['jobs'] 
['developer', 'manager']
>>> rec['jobs'][1] 
'manager'
>>> rec['home']['zip'] 
12345
```

top-level container in realistic programs:

```
db = [] 
db.append(rec) 			# A list "database"
db.append(other) 
db[0]['jobs']

db = {} 
db['bob'] = rec			# A dictionary "database"
db['sue'] = other 
db['bob']['jobs']
```



### Other Ways to Make Dictionaries

```
{'name': 'Bob', 'age': 40}			# Traditional literal expression

D = {} 									# Assign by keys dynamically
D['name'] = 'Bob' 
D['age'] = 40

dict(name='Bob', age=40)				# dict keyword argument form

dict([('name', 'Bob'), ('age', 40)])	# dict key/value tuples form
```

All four of these forms create the same two-key dictionary, but they are useful in differing circumstances:

- The first is handy if you can spell out the entire dictionary ahead of time.


- The second is of use if you need to create the dictionary one field at a time on the fly.



- The third involves less typing than the first, but it requires all keys to be strings.



- The last is useful if you need to build up keys and values as sequences at runtime.

to combine separate lists of keys and values obtained dynamically at runtime (parsed out of a data file’s columns, for instance):

```
dict(zip(keyslist, valueslist))  # Zipped key/value tuples form (ahead)
```

Provided all the key’s values are the same initially, you can also create a dictionary with this special form—simply pass in a list of keys and an initial value for all of the values (the default is None):

```
>>> dict.fromkeys(['a', 'b'], 0) 
{'a': 0, 'b': 0}
```



### Dictionary Changes in Python 3.X and 2.7

Specifically, dictionaries in Python 3.X:

- Support a new dictionary comprehension expression, a close cousin to list and set comprehensions


- Return set-like iterable views instead of lists for the methods D.keys, D.values, and

  D.items


- Require new coding styles for scanning by sorted keys, because of the prior point



- No longer support relative magnitude comparisons directly—compare manually instead



- No longer have the D.has_key method—the in membership test is used instead

dictionaries in Python 2.7 (but not earlier in 2.X):

- Support item 1 in the prior list—dictionary comprehensions—as a direct back-port from 3.X


- Support item 2 in the prior list—set-like iterable views—but do so with special method names D.viewkeys, D.viewvalues, D.viewitems); their nonview methods return lists as before



### Dictionary comprehensions in 3.X and 2.7

```
# Zip together keys and values
>>> list(zip(['a', 'b', 'c'], [1, 2, 3])) 
[('a', 1), ('b', 2), ('c', 3)]

# Make a dict from zip result
>>> D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
>>> D 
{'b': 2, 'c': 3, 'a': 1}
```

In Python 3.X and 2.7, though, you can achieve the same effect with a dictionary comprehension expression:

```
>>> D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
>>> D 
{'b': 2, 'c': 3, 'a': 1}
```

map a single stream of values to dictionaries as well, and keys can be computed with expressions just like values:

```
>>> D = {x: x ** 2 for x in [1, 2, 3, 4]}	# Or: range(1, 5)
>>> D 
{1: 1, 2: 4, 3: 9, 4: 16}

>>> D = {c: c * 4 for c in 'SPAM'} 			# Loop over any iterable
>>> D 
{'S': 'SSSS', 'P': 'PPPP', 'A': 'AAAA', 'M': 'MMMM'}

>>> D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
>>> D 
{'eggs': 'EGGS!', 'spam': 'SPAM!', 'ham': 'HAM!'}
```

Dictionary comprehensions are also useful for initializing dictionaries from keys lists:

```
>>> D = dict.fromkeys(['a', 'b', 'c'], 0)  # Initialize dict from keys
>>> D 
{'b': 0, 'c': 0, 'a': 0}

>>> D = {k:0 for k in ['a', 'b', 'c']}# Same, but with a comprehension
>>> D 
{'b': 0, 'c': 0, 'a': 0}

>>> D = dict.fromkeys('spam')		# Other iterables, default value
>>> D 
{'s': None, 'p': None, 'a': None, 'm': None}

>>> D = {k: None for k in 'spam'}
>>> D 
{'s': None, 'p': None, 'a': None, 'm': None}
```



### Dictionary views in 3.X (and 2.7 via new methods)

```
>>> D = dict(a=1, b=2, c=3)
>>> D 
{'b': 2, 'c': 3, 'a': 1}

>>> K = D.keys()		# Makes a view object in 3.X, not a list
>>> K 
dict_keys(['b', 'c', 'a'])
>>> list(K) 			# Force a real list in 3.X if needed
['b', 'c', 'a']

>>> V = D.values()		# Ditto for values and items views
>>> V 
dict_values([2, 3, 1])
>>> list(V) 
[2, 3, 1]

>>> D.items() 
dict_items([('b', 2), ('c', 3), ('a', 1)])
>>> list(D.items()) 
[('b', 2), ('c', 3), ('a', 1)]

>>> K[0] 			# List operations fail unless converted 
TypeError: 'dict_keys' object does not support indexing
>>> list(K)[0] 
'b'
```

because looping constructs in Python automatically force iterable objects to produce one result on each iteration:

```
>>> for k in D.keys(): print(k) # Iterators used automatically in loops
...
b
c
a
```

3.X dictionaries still have iterators themselves, which return successive keys—as in 2.X,

```
>>> for key in D: print(key) # Still no need to call keys() to iterate
...
b
c
a
```

dictionary views in 3.X, dynamically reflect future changes made to the dictionary after the view object has been created:

```
>>> D = {'a': 1, 'b': 2, 'c': 3}
>>> D 
{'b': 2, 'c': 3, 'a': 1}

>>> K = D.keys()
>>> V = D.values()
>>> list(K) 		# Views maintain same order as dictionary
['b', 'c', 'a']
>>> list(V) 
[2, 3, 1]

>>> del D['b']		# Change the dictionary in place
>>> D 
{'c': 3, 'a': 1}

>>> list(K) 		# Reflected in any current view objects
['c', 'a']
>>> list(V) 		# Not true in 2.X! - lists detached from dict
[3, 1]
```



### Dictionary views and sets





### ...

### ...

### ...

















## Dictionary method calls



```
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```






### dict.get()

Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。

```
dict.get(key, default=None)
```

- key -- 字典中要查找的键。
- default -- 如果指定键的值不存在时，返回该默认值值。

返回指定键的值，如果值不在字典中返回默认值None。

> **get**(...)
>
> ​    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

**实例**:

```
>>> dict = {'Name':'tom','Age':'6'}
>>> print(dict.get('Name'))
tom
>>> print(dict.get('school'))
None
>>> print(dict.get('Class','4'))
4
```









