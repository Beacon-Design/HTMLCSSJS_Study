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

> For any dictionary D, saying `for key in D` works the same as saying the complete `for key in D.keys()`.

















## Dictionary method calls



```
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```