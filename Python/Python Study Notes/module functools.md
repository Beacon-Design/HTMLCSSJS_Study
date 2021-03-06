# module functools

Python 3.X

## help(functools)

```
Help on module functools:

NAME
    functools - functools.py - Tools for working with functions and callable objects

MODULE REFERENCE
    http://docs.python.org/3.4/library/functools
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        partial
        partialmethod
    
    class partial(builtins.object)
     |  partial(func, *args, **keywords) - new function with partial application
     |  of the given arguments and keywords.
     |  
     |  Methods defined here:
     |  
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |  
     |  args
     |      tuple of arguments to future partial calls
     |  
     |  func
     |      function object to use in future partial calls
     |  
     |  keywords
     |      dictionary of keyword arguments to future partial calls
    
    class partialmethod(builtins.object)
     |  Method descriptor with partial application of the given arguments
     |  and keywords.
     |  
     |  Supports wrapping existing descriptors and handles non-descriptor
     |  callables as instance methods.
     |  
     |  Methods defined here:
     |  
     |  __get__(self, obj, cls)
     |  
     |  __init__(self, func, *args, **keywords)
     |  
     |  __repr__(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __isabstractmethod__
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    cmp_to_key(...)
        Convert a cmp= function into a key= function.
    
    lru_cache(maxsize=128, typed=False)
        Least-recently-used cache decorator.
        
        If *maxsize* is set to None, the LRU features are disabled and the cache
        can grow without bound.
        
        If *typed* is True, arguments of different types will be cached separately.
        For example, f(3.0) and f(3) will be treated as distinct calls with
        distinct results.
        
        Arguments to the cached function must be hashable.
        
        View the cache statistics named tuple (hits, misses, maxsize, currsize)
        with f.cache_info().  Clear the cache and statistics with f.cache_clear().
        Access the underlying function with f.__wrapped__.
        
        See:  http://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used
    
    reduce(...)
        reduce(function, sequence[, initial]) -> value
        
        Apply a function of two arguments cumulatively to the items of a sequence,
        from left to right, so as to reduce the sequence to a single value.
        For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
        ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
        of the sequence in the calculation, and serves as a default when the
        sequence is empty.
    
    singledispatch(func)
        Single-dispatch generic function decorator.
        
        Transforms a function into a generic function, which can have different
        behaviours depending upon the type of its first argument. The decorated
        function acts as the default implementation, and additional
        implementations can be registered using the register() attribute of the
        generic function.
    
    total_ordering(cls)
        Class decorator that fills in missing ordering methods
    
    update_wrapper(wrapper, wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',))
        Update a wrapper function to look like the wrapped function
        
        wrapper is the function to be updated
        wrapped is the original function
        assigned is a tuple naming the attributes assigned directly
        from the wrapped function to the wrapper function (defaults to
        functools.WRAPPER_ASSIGNMENTS)
        updated is a tuple naming the attributes of the wrapper that
        are updated with the corresponding attribute from the wrapped
        function (defaults to functools.WRAPPER_UPDATES)
    
    wraps(wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',))
        Decorator factory to apply update_wrapper() to a wrapper function
        
        Returns a decorator that invokes update_wrapper() with the decorated
        function as the wrapper argument and the arguments to wraps() as the
        remaining arguments. Default arguments are as for update_wrapper().
        This is a convenience function to simplify applying partial() to
        update_wrapper().

DATA
    WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__do...
    WRAPPER_UPDATES = ('__dict__',)
    __all__ = ['update_wrapper', 'wraps', 'WRAPPER_ASSIGNMENTS', 'WRAPPER_...

FILE
    /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/functools.py
```



## dir(functools)

```
>>> import functools
>>> dir(functools)
['MappingProxyType', 'RLock', 'WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', 'WeakKeyDictionary', '_CacheInfo', '_HashedSeq', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_c3_merge', '_c3_mro', '_compose_mro', '_find_impl', '_ge_from_gt', '_ge_from_le', '_ge_from_lt', '_gt_from_ge', '_gt_from_le', '_gt_from_lt', '_le_from_ge', '_le_from_gt', '_le_from_lt', '_lt_from_ge', '_lt_from_gt', '_lt_from_le', '_make_key', 'cmp_to_key', 'get_cache_token', 'lru_cache', 'namedtuple', 'partial', 'partialmethod', 'reduce', 'singledispatch', 'total_ordering', 'update_wrapper', 'wraps']
```





### reduce()

> ```
> Help on built-in function reduce in module _functools:
>
> reduce(...)
>     reduce(function, sequence[, initial]) -> value
>     
>     Apply a function of two arguments cumulatively to the items of a sequence,
>     from left to right, so as to reduce the sequence to a single value.
>     For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
>     ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
>     of the sequence in the calculation, and serves as a default when the
>     sequence is empty.
> ```

example:

```
python 3.X

>>> from functools import reduce
>>> reduce((lambda x, y: x + y), [1, 2, 3, 4]) 
10
>>> reduce((lambda x, y: x * y), [1, 2, 3, 4]) 
24
```

Coding your own version of `reduce` :

```
>>> def myreduce(function, sequence):
		tally = sequence[0] 
		for next in sequence[1:]:
			tally = function(tally, next) 
		return tally

>>> myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5]) 
15
>>> myreduce((lambda x, y: x * y), [1, 2, 3, 4, 5]) 
120
```





