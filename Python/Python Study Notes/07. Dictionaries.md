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



## Help on class dict in module builtins

```
class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if D has a key k, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Returns a new dict with keys from iterable and values equal to value.
 |  
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
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

> - The first (dictionary comprehensions) can be coded only in 3.X and 2.7.
>
>
> - The second (dictionary views) can be coded only in 3.X, and with special method names in 2.7.
>
> the last three techniques—`sorted`, manual comparisons, and `in`—can be coded in 2.X today to ease 3.X migration in the future.



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





#### Dictionary comprehensions in 3.X and 2.7

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



#### Dictionary views in 3.X (and 2.7 via new methods)

1. Python 3.0中，字典的`keys`, `values`, `items` 都返回视图对象；而在Python 2.6中，他们返回实际的结果列表。  
2. 视图对象是可迭代的，对象每次产生一个结果项，而不是在内存中立即产生结果列表。
3. 字典试图还保持了字典成分的最初顺序，反应字典未来的修改，并支持集合操作。
4. 他们不是列表，不支持像索引和列表sort方法这样的操，打印时他们也不显示自己的项。

In 3.X the dictionary `keys`, `values`, and `items` methods all return view objects, whereas in 2.X they return actual result lists. View objects are iterables, which simply means objects that generate result items one at a time, instead of producing the result list all at once in memory. Besides being iterable, dictionary views also retain the original order of dictionary components, reflect future changes to the dictionary, and may support set operations. On the other hand, because they are not lists, they do not directly support operations like indexing or the list `sort` method, and do not display their items as a normal list when printed

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



#### Dictionary views and sets 字典视图与集合

1. 3.X’s view objects returned by the `keys` method are set-like and support common set operations such as intersection and union; 
2. `values` views are not set-like, 
3. but `items` results are if their `(key, value)` pairs are unique and hashable (immutable).

`keys` views look like when used in set operations：

```
>>> D = {'a':1, 'b':2, 'c':3}
>>> K = D.keys()
>>> V = D.values()
>>> K, V
(dict_keys(['c', 'b', 'a']), dict_values([3, 2, 1]))

>>> K | {'x':4}				# Keys (and some items) views are set-like
{'c', 'a', 'x', 'b'}

>>> V & {'x':4}
TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict'
>>> V & {'x': 4}.values() 
TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict_values'
```

In set operations, views may be mixed with other views, sets, and dictionaries; dictionaries are treated the same as their `keys` views in this context:

```
>>> D = {'a':1, 'b':2, 'c':3}
>>> M = {'a':1, 'b':2, 'c':3}
>>> D.keys() & M.keys()			# Intersect keys views
{'c', 'a', 'b'}
>>> D.keys() & {'b'}			# Intersect keys and set
{'b'}
>>> D.keys() & {'b':9}			# Intersect keys and dict
{'b'}
>>> D.keys() | {'b', 'c', 'd'}
{'a', 'c', 'd', 'b'}			# Union keys and set
```

Items views are set-like too if they are hashable—that is, if they contain only immutable objects:

```
>>> D = {'a':1}								# Items set-like if hashable
>>> list(D.items())
[('a', 1)]
>>> D.items() | D.keys()					# Items set-like if hashable
{'a', ('a', 1)}
>>> D.items() | D							# dict treated same as its keys
{'a', ('a', 1)}

>>> D.items() | {('c', 3), ('d', 4)}		# Set of key/value pairs
{('c', 3), ('d', 4), ('a', 1)}

>>> dict(D.items() | {('c', 3), ('d', 4)})	# dict accepts iterable sets too
{'c': 3, 'd': 4, 'a': 1}
```



#### Sorting dictionary keys in 3.X

because `keys` does not return a list in 3.X, the traditional coding pattern for scanning a dictionary by sorted keys in 2.X won’t work in 3.X:

```
>>> D = {'a': 1, 'b': 2, 'c': 3}
>>> D 
{'b': 2, 'c': 3, 'a': 1}

>>> Ks = D.keys() 					# Sorting a view object doesn't work!
>>> Ks.sort() 
AttributeError: 'dict_keys' object has no attribute 'sort'

>>> Ks = list(Ks)					# Force it to be a list and then sort
>>> Ks.sort()
>>> for k in Ks: print(k, D[k]) 	# 2.X: omit outer parens in prints
...
a 1 
b 2 
c 3

>>> D 
{'b': 2, 'c': 3, 'a': 1}
>>> Ks = D.keys()							# Or you can use sorted() on the keys
>>> for k in sorted(Ks): print(k, D[k]) 	# sorted() accepts any iterable
...											# sorted() returns its result
a 1
b 2 
c 3
```

using the dictionary’s keys iterator is probably preferable in 3.X, and works in 2.X as well:

```
>>> D
{'c': 3, 'b': 2, 'a': 1}					# Better yet, sort the dict directly
>>> for k in sorted(D): print(k, D[k])		# dict iterators return keys
... 
a 1
b 2
c 3
```



#### Dictionary magnitude comparisons no longer work in 3.X

while in Python 2.X dictionaries may be compared for relative magnitude directly with <, >, and so on, in Python 3.X this no longer works.

you can simulate it by comparing sorted keys lists manually:

```
sorted(D1.items()) < sorted(D2.items())		# Like 2.X D1 < D2
```

Dictionary equality tests (e.g., D1 == D2) still work in 3.X



#### use `in`

> the widely used dictionary `has_key` key presence test method is gone in 3.X.

use the `in` membership expression, or a `get` with a default test (of these, `in` is generally preferred):

```
>>> D 
{'b': 2, 'c': 3, 'a': 1}

>>> D.has_key('c') 										# 2.X only: True/False
AttributeError: 'dict' object has no attribute 'has_key'

>>> 'c' in D 								# Required in 3.X
True
>>> 'x' in D 								# Preferred in 2.X today
False
>>> if 'c' in D: print('present', D['c']) 	# Branch on result
...
present 3

>>> print(D.get('c')) 								# Fetch with default
3
>>> print(D.get('x')) 
None
>>> if D.get('c') != None: print('present', D['c']) # Another option
...
present 3
```





## Dictionary method calls



```
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```



### len(dict)

Python 字典(Dictionary) len() 函数计算字典元素个数，即键的总数。

```
len(dict)
```

- dict -- 要计算元素个数的字典。

返回字典的元素个数。

> **__len__**(self, /)
>
> ​    Return len(self).

**实例**:

```
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> len(dict)
3
```



### str(dict)

输出字典，以可打印的字符串表示。

> ```
> >>> help(dict.__str__)
> ```

> ```
> __str__ = class method-wrapper(object)
>  |  Methods defined here:
>  |  
>  |  __call__(self, /, *args, **kwargs)
>  |      Call self as a function.
>  |  
>  |  __eq__(self, value, /)
>  |      Return self==value.
>  |  
>  |  __ge__(self, value, /)
>  |      Return self>=value.
>  |  
>  |  __getattribute__(self, name, /)
>  |      Return getattr(self, name).
>  |  
>  |  __gt__(self, value, /)
>  |      Return self>value.
>  |  
>  |  __hash__(self, /)
>  |      Return hash(self).
>  |  
>  |  __le__(self, value, /)
>  |      Return self<=value.
>  |  
>  |  __lt__(self, value, /)
>  |      Return self<value.
>  |  
>  |  __ne__(self, value, /)
>  |      Return self!=value.
>  |  
>  |  __reduce__(...)
>  |  
>  |  __repr__(self, /)
>  |      Return repr(self).
>  |  
>  |  ----------------------------------------------------------------------
>  |  Data descriptors defined here:
>  |  
>  |  __objclass__
>  |  
>  |  __self__
>  |  
>  |  __text_signature__
> ```

```
str(dict)
```

- dict -- 字典。

返回字符串。

**实例**:

```
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> str(dict)
"{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"
```



### dict.clear()

Python 字典 clear() 函数用于删除字典内所有元素。

> ```
> clear(...) method of builtins.dict instance
>     D.clear() -> None.  Remove all items from D.
> ```

```
dict.clear()
```

该函数没有任何返回值。

**实例**:

```
>>> D = {'a':1, 'b':2, 'c':3}
>>> D
{'c': 3, 'b': 2, 'a': 1}
>>> D.clear()
>>> D
{}
```



### dict.copy()

Python 字典(Dictionary) copy() 函数返回一个字典的浅复制。

```
dict.copy()
```

返回一个字典的浅复制。

**实例**:

```

```



### dict.fromkeys()

Python 字典 fromkeys() 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。

> ```
> fromkeys(iterable, value=None, /) method of builtins.type instance
>     Returns a new dict with keys from iterable and values equal to value.
> ```

```
dict.fromkeys(seq[, value]))
```

- seq -- 字典键值列表。
- value -- 可选参数, 设置键序列（seq）的值。

该方法返回列表。

**实例**:

```
>>> seq = ('a', 'b','c')
>>> v = 10
>>> D = {}
>>> D.fromkeys(seq, v)
{'c': 10, 'b': 10, 'a': 10}
>>> D
{}
>>> d = D.fromkeys(seq, v)
>>> d
{'c': 10, 'b': 10, 'a': 10}
```






### dict.get()

Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。

> ```
> get(...) method of builtins.dict instance
>     D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
> ```

```
dict.get(key, default=None)
```

- key -- 字典中要查找的键。
- default -- 如果指定键的值不存在时，返回该默认值值。

返回指定键的值，如果值不在字典中返回默认值None。

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





### dict.items()

> ```
> items(...)
>     D.items() -> a set-like object providing a view on D's items
> ```

```
dict.items()
```

**实例**:

```
>>> D = {'a':1, 'b':2, 'c':3}
>>> D
{'c': 3, 'b': 2, 'a': 1}
>>> D.items()
dict_items([('c', 3), ('b', 2), ('a', 1)])
>>> d = D.items()
>>> d
dict_items([('c', 3), ('b', 2), ('a', 1)])
```





### dict.keys()



> ```
> keys(...) method of builtins.dict instance
>     D.keys() -> a set-like object providing a view on D's keys
> ```

**实例**:

```
>>> D = {'a':1, 'b':2, 'c':3}
>>> D.keys()
dict_keys(['c', 'b', 'a'])

>>> list(D.keys())
['c', 'b', 'a']
```



### dict.pop()

> ```
> pop(...)
>     D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
>     If key is not found, d is returned if given, otherwise KeyError is raised
> ```

**实例**:

```
>>> D = {'a':1, 'b':2, 'c':3}
>>> D.pop('a')
1
>>> D
{'c': 3, 'b': 2}
>>> D.pop(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 2
```



### dict.popitem()

> ```
> popitem(...)
>     D.popitem() -> (k, v), remove and return some (key, value) pair as a
>     2-tuple; but raise KeyError if D is empty.
> ```

**实例**:

```
>>> D
{'c': 3, 'b': 2}
>>> D.popitem()
('c', 3)
>>> D
{'b': 2}
>>> D.popitem()
('b', 2)
>>> D
{}
>>> D.popitem()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'popitem(): dictionary is empty'
```



### dict.setdefault()

Python 字典 setdefault() 函数和 get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值。

> ```
> setdefault(...)
>     D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
> ```

```
dict.setdefault(key, default=None)
```

- key -- 查找的键值。
- default -- 键不存在时，设置的默认键值。

如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。

**实例**:

```
>>> D = {'a':1, 'b':2, 'c':3}
>>> D.setdefault('d')
>>> D
{'d': None, 'c': 3, 'b': 2, 'a': 1}
>>> D.setdefault('c')
3
>>> D
{'d': None, 'c': 3, 'b': 2, 'a': 1}
>>> D.setdefault('f', 5)
5
>>> D
{'f': 5, 'd': None, 'b': 2, 'a': 1, 'c': 3}
```



### dict.update()

Python 字典(Dictionary) update() 函数把字典dict2的键/值对更新到dict里。

> ```
> update(...)
>     D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
>     If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
>     If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
>     In either case, this is followed by: for k in F:  D[k] = F[k]
> ```

```
dict.update(dict2)
```

- dict2 -- 添加到指定字典dict里的字典。

该方法没有任何返回值。

**实例**:

```
>>> D = {'a':1, 'b':2, 'c':3}
>>> d = {'x':10, 'y':11, 'z':12}
>>> D
{'c': 3, 'b': 2, 'a': 1}
>>> d
{'x': 10, 'y': 11, 'z': 12}

>>> D.update(d)
>>> D
{'x': 10, 'y': 11, 'b': 2, 'a': 1, 'z': 12, 'c': 3}

>>> d
{'x': 10, 'y': 11, 'z': 12}
```



### dict.values()

Python 字典(Dictionary) values() 函数以列表返回字典中的所有值。

> ```
> values(...)
>     D.values() -> an object providing a view on D's values
> ```

```
dict.values()
```

返回字典中的所有值。

**实例**:

```
>>> D = {'a':1, 'b':2, 'c':3}
>>> D.values()
dict_values([3, 2, 1])
```