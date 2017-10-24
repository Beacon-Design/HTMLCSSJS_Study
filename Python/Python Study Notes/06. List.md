# Python Study Notes



# List

1. Lists are ordered collection object type.

2. lists can contain any sort of object: numbers, strings, and even other lists.

3. Lists are mutable objects. 

   > (may be changed in place by assignment to offsets and slices, list method calls, deletion statements, and more)

**Ordered collections of arbitrary objects**

> From a functional view, lists are just places to collect other objects so you can treat them as groups. Lists also maintain a left-to-right positional ordering among the items they contain (i.e., they are sequences).

**Accessed by offset**

> Just as with strings, you can fetch a component object out of a list by indexing the list on the object’s offset. Because items in lists are ordered by their positions, you can also do tasks such as slicing and concatenation.

**Variable-length, heterogeneous, and arbitrarily nestable**

> Unlike strings, lists can grow and shrink in place (their lengths can vary), and they can contain any sort of object, not just one-character strings (they’re heterogene-ous). Because lists can contain other complex objects, they also support arbitrary nesting; you can create lists of lists of lists, and so on.

**Of the category “mutable sequence”**

> In terms of our type category qualifiers, lists are mutable (i.e., can be changed in place) and can respond to all the sequence operations used with strings, such as indexing, slicing, and concatenation. In fact, sequence operations work the same on lists as they do on strings; the only difference is that sequence operations such as concatenation and slicing return new lists instead of new strings when applied to lists. Because lists are mutable, however, they also support other operations that strings don’t, such as deletion and index assignment operations, which change the lists in place.

**Arrays of object references**

> Technically, Python lists contain zero or more references to other objects. Lists might remind you of arrays of pointers (addresses) if you have a background in some other languages. Fetching an item from a Python list is about as fast as indexing a C array; in fact, lists really are arrays inside the standard Python inter-preter, not linked structures.  though, Python always follows a reference to an object whenever the reference is used, so your program deals only with objects. Whenever you assign an object to a data structure component or variable name, Python always **stores a reference to that same object**, not a copy of it (unless you request a copy explicitly).



## Common list literals and operations

```
Common list literals and operations

Operation							Interpretation

L = [] 								An empty list
L = [123, 'abc', 1.23, {}] 			Four items: indexes 0..3
L = ['Bob', 40.0, ['dev', 'mgr']] 	Nested sublists
L = list('spam') 		    		List of an iterable’s items, 
L = list(range(-4, 4)) 			    list of successive integers
L[i] 								Index
L[i][j] 							index of index
L[i:j] 								slice
len(L) 								length
L1 + L2								Concatenate
L * 3 								repeat
for x in L: print(x) 				Iteration
3 in L								membership
L.append(4)							Methods: growing
L.extend([5,6,7])
L.insert(i, X)
L.index(X)							Methods: searching
L.count(X)
L.sort()							Methods: sorting, reversing,
L.reverse()
L.copy()							copying (3.3+), clearing (3.3+)
L.clear()
L.pop(i)							Methods, statements: shrinking
L.remove(X) 
del L[i] 
del L[i:j] 
L[i:j] = [] 
L[i] = 3 
L[i:j] = [4,5,6] 					Index assignment, slice assignment
L = [x**2 for x in range(5)] 
list(map(ord, 'spam'))
```







## Basic List Operations

lists respond to the `+` and `*` operators. the result is a new list.

```
>>> len([1, 2, 3]) 				# Length 
3
>>> [1, 2, 3] + [4, 5, 6] 		# Concatenation 
[1, 2, 3, 4, 5, 6]
>>> ['Ni!'] * 4 				# Repetition
['Ni!', 'Ni!', 'Ni!', 'Ni!']
```

the `+`  operator the same sort of sequence on both sides—otherwise, you get a type error

```
>>> str([1, 2]) + "34" 		# Same as "[1, 2]" + "34"
'[1, 2]34'
>>> [1, 2] + list("34") 	# Same as [1, 2] + ["3", "4"]
[1, 2, '3', '4']
```



## List Iteration 

iteration tools:

```
>>> 3 in [1, 2, 3] 			# Membership
True
>>> for x in [1, 2, 3]: 
... print(x, end=' ') 
...
1 2 3
```



## list comprehensions

list comprehensions are a way to build a new list by applying an expression to each item in a sequence (really, in any iterable), and are close relatives to for loops:

```
>>> res = [c * 4 for c in 'SPAM']		# List comprehensions
>>> res 
['SSSS', 'PPPP', 'AAAA', 'MMMM']
```

list comprehensions are simpler to code and likely faster to run today:

```
>>> res = []
>>> for c in 'SPAM':			# List comprehension equivalent
... res.append(c * 4) 
...
>>> res 
['SSSS', 'PPPP', 'AAAA', 'MMMM']
```

the map built-in function does similar work, but applies a function to items in a sequence and collects all the results in a new list:

```
>>> list(map(abs, [−1, −2, 0, 1, 2])) 	# Map a function across a sequence
[1, 2, 0, 1, 2]
```



## Indexing, Slicing, and Matrixes

the result of indexing a list is whatever type of object lives at the offset you specify, while slicing a list always returns a new list:

```
>>> L = ['spam', 'Spam', 'SPAM!']
>>> L[2] 							# Offsets start at zero
'SPAM!'
>>> L[−2] 							# Negative: count from the right
'Spam'
>>> L[1:] 							# Slicing fetches sections
['Spam', 'SPAM!']
```

matrixes (multidimensional arrays)

```
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> matrix[1] 
[4, 5, 6]
>>> matrix[1][1] 
5
>>> matrix[2][0] 
7
>>> matrix = [[1, 2, 3], 
... 		  [4, 5, 6], 
... 		  [7, 8, 9]]
>>> matrix[1][1] 
5
```



## Changing Lists in Place

if you change an object in place, you might impact more than one reference to it at the same time.

### Index and slice assignments

Both index and slice assignments are in-place changes—they modify the subject list directly, rather than generating a new list object for the result.

```
>>> L = ['spam', 'Spam', 'SPAM!']
>>> L[1] = 'eggs'					# Index assignment
>>> L 
['spam', 'eggs', 'SPAM!']
>>> L[0:2] = ['eat', 'more']		# Slice assignment: delete+insert
>>> L 								# Replaces items 0,1
['eat', 'more', 'SPAM!']
```

> slice assignment replaces an entire section, or “column,” all at once—even if the column or its replacement is empty. 



## List method calls



```
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```



### L.append()

append, which simply tacks a single item (object reference) onto the end of the list.

The effect of L.append(X) is similar to L+[X], but while the former changes L in place, the latter makes a new list.

```
>>> L = ['eat', 'more', 'SPAM!']
>>> L.append('please')				# Append method call: add item at end
>>> L
['eat', 'more', 'SPAM!', 'please']
>>> L.sort()						# Sort list items ('S' < 'e')
>>> L 
['SPAM!', 'eat', 'more', 'please']
```



### L.sort()

by default sorts in ascending order

```
>>> L = ['abc', 'ABD', 'aBe']
>>> L.sort()								# Sort with mixed case
>>> L
['ABD', 'aBe', 'abc']
>>> L = ['abc', 'ABD', 'aBe']
>>> L.sort(key=str.lower)					# Normalize to lowercase
>>> L 
['abc', 'ABD', 'aBe']
>>> L.sort(key=str.lower, reverse=True) 	# Change sort order
>>> L 
['aBe', 'ABD', 'abc']
```

**One warning here**: beware that append and sort change the associated list object in place, but don’t return the list as a result (technically, they both return a value called None)

#### sorted()

Pythons as a built-in function, which sorts any collection (not just lists) and returns a new list for the result (instead of in-place changes):

```
>>> L = ['abc', 'ABD', 'aBe']
>>> sorted(L, key=str.lower, reverse=True) 		# Sorting built-in
['aBe', 'ABD', 'abc']
>>> sorted([x.lower() for x in L], reverse=True) 	
['abe', 'abd', 'abc']
```

#### L.reverse(), L.extend(), L.pop(), reversed(L)

```
>>> L = [1, 2]
>>> L.extend([3, 4, 5])		# Add many items at end (like in-place +)
>>> L 
[1, 2, 3, 4, 5]
>>> L.pop() 				# Delete and return last item (by default: −1)
5
>>> L 
[1, 2, 3, 4]
>>> L.reverse()				# In-place reversal method
>>> L 
[4, 3, 2, 1]
>>> list(reversed(L)) 		# Reversal built-in with a result (iterator)
[1, 2, 3, 4]
```

the list pop method is often used in conjunction with append to implement a quick last-in-first-out (LIFO) stack structure. The end of the list serves as the top of the stack:

```
>>> L = []
>>> L.append(1)			# Push onto stack
>>> L.append(2)
>>> L 
[1, 2]
>>> L.pop() 			# Pop off stack
2
>>> L
[1]
```

```
>>> L = ['spam', 'eggs', 'ham']
>>> L.index('eggs')					# Index of an object (search/find)
1
>>> L.insert(1, 'toast')			# Insert at position
>>> L 
['spam', 'toast', 'eggs', 'ham']
>>> L.remove('eggs')				# Delete by value
>>> L 
['spam', 'toast', 'ham']
>>> L.pop(1) 						# Delete by position
'toast'
>>> L 
['spam', 'ham']
>>> L.count('spam') 				# Number of occurrences
1
```

### del

```
>>> L = ['spam', 'eggs', 'ham', 'toast']
>>> del L[0] 							# Delete one item
>>> L 
['eggs', 'ham', 'toast']
>>> del L[1:] 							# Delete an entire section
>>> L 									# Same as L[1:] = [] 
['eggs']
```

because slice assignment is a deletion plus an insertion, you can also delete a section of a list by assigning an empty list to a slice ( `L[i:j]=[]` )

just stores a reference to the empty list object in the specified slot, rather than deleting an item:

```
>>> L = ['Already', 'got', 'one']
>>> L[1:] = []
>>> L 
['Already']
>>> L[0] = []
>>> L 
[[]]
```



#### ...

#### ...

#### ...