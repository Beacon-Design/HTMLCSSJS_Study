# module collections

[`collections`](https://docs.python.org/3.4/library/collections.html#module-collections) — Container datatypes

This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, [`dict`](https://docs.python.org/3.4/library/stdtypes.html#dict), [`list`](https://docs.python.org/3.4/library/stdtypes.html#list), [`set`](https://docs.python.org/3.4/library/stdtypes.html#set), and [`tuple`](https://docs.python.org/3.4/library/stdtypes.html#tuple).

| [`namedtuple()`](https://docs.python.org/3.4/library/collections.html#collections.namedtuple) | factory function for creating tuple subclasses with named fields |
| ---------------------------------------- | ---------------------------------------- |
| [`deque`](https://docs.python.org/3.4/library/collections.html#collections.deque) | list-like container with fast appends and pops on either end |
| [`ChainMap`](https://docs.python.org/3.4/library/collections.html#collections.ChainMap) | dict-like class for creating a single view of multiple mappings |
| [`Counter`](https://docs.python.org/3.4/library/collections.html#collections.Counter) | dict subclass for counting hashable objects |
| [`OrderedDict`](https://docs.python.org/3.4/library/collections.html#collections.OrderedDict) | dict subclass that remembers the order entries were added |
| [`defaultdict`](https://docs.python.org/3.4/library/collections.html#collections.defaultdict) | dict subclass that calls a factory function to supply missing values |
| [`UserDict`](https://docs.python.org/3.4/library/collections.html#collections.UserDict) | wrapper around dictionary objects for easier dict subclassing |
| [`UserList`](https://docs.python.org/3.4/library/collections.html#collections.UserList) | wrapper around list objects for easier list subclassing |
| [`UserString`](https://docs.python.org/3.4/library/collections.html#collections.UserString) | wrapper around string objects for easier string subclassing |



### namedtuple()

Factory Function for Tuples with Named Fields

Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.

```
Help on function namedtuple in module collections:

namedtuple(typename, field_names, verbose=False, rename=False)
    Returns a new subclass of tuple with named fields.
    
    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessable by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)
```

> ```
> collections.namedtuple(typename, field_names, verbose=False, rename=False)
> Returns a new tuple subclass named typename. The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable. Instances of the subclass also have a helpful docstring (with typename and field_names) and a helpful __repr__() method which lists the tuple contents in a name=value format.
>
> The field_names are a single string with each fieldname separated by whitespace and/or commas, for example 'x y' or 'x, y'. Alternatively, field_names can be a sequence of strings such as ['x', 'y'].
>
> Any valid Python identifier may be used for a fieldname except for names starting with an underscore. Valid identifiers consist of letters, digits, and underscores but do not start with a digit or underscore and cannot be a keyword such as class, for, return, global, pass, or raise.
>
> If rename is true, invalid fieldnames are automatically replaced with positional names. For example, ['abc', 'def', 'ghi', 'abc'] is converted to ['abc', '_1', 'ghi', '_3'], eliminating the keyword def and the duplicate fieldname abc.
>
> If verbose is true, the class definition is printed after it is built. This option is outdated; instead, it is simpler to print the _source attribute.
>
> Named tuple instances do not have per-instance dictionaries, so they are lightweight and require no more memory than regular tuples.
> ```

