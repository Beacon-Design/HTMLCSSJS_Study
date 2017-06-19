# module operator



## help(operator)

```
Help on module operator:

NAME
    operator - Operator interface.

MODULE REFERENCE
    http://docs.python.org/3.4/library/operator
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module exports a set of functions implemented in C corresponding
    to the intrinsic operators of Python.  For example, operator.add(x, y)
    is equivalent to the expression x+y.  The function names are those
    used for special methods; variants without leading and trailing
    '__' are also provided for convenience.

CLASSES
    builtins.object
        attrgetter
        itemgetter
        methodcaller
    
    class attrgetter(builtins.object)
     |  attrgetter(attr, ...) --> attrgetter object
     |  
     |  Return a callable object that fetches the given attribute(s) from its operand.
     |  After f = attrgetter('name'), the call f(r) returns r.name.
     |  After g = attrgetter('name', 'date'), the call g(r) returns (r.name, r.date).
     |  After h = attrgetter('name.first', 'name.last'), the call h(r) returns
     |  (r.name.first, r.name.last).
     |  
     |  Methods defined here:
     |  
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
    
    class itemgetter(builtins.object)
     |  itemgetter(item, ...) --> itemgetter object
     |  
     |  Return a callable object that fetches the given item(s) from its operand.
     |  After f = itemgetter(2), the call f(r) returns r[2].
     |  After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
     |  
     |  Methods defined here:
     |  
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
    
    class methodcaller(builtins.object)
     |  methodcaller(name, ...) --> methodcaller object
     |  
     |  Return a callable object that calls the given method on its operand.
     |  After f = methodcaller('name'), the call f(r) returns r.name().
     |  After g = methodcaller('name', 'date', foo=1), the call g(r) returns
     |  r.name('date', foo=1).
     |  
     |  Methods defined here:
     |  
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.

FUNCTIONS
    __abs__ = abs(...)
        abs(a) -- Same as abs(a).
    
    __add__ = add(...)
        add(a, b) -- Same as a + b.
    
    __and__ = and_(...)
        and_(a, b) -- Same as a & b.
    
    __concat__ = concat(...)
        concat(a, b) -- Same as a + b, for a and b sequences.
    
    __contains__ = contains(...)
        contains(a, b) -- Same as b in a (note reversed operands).
    
    __delitem__ = delitem(...)
        delitem(a, b) -- Same as del a[b].
    
    __eq__ = eq(...)
        eq(a, b) -- Same as a==b.
    
    __floordiv__ = floordiv(...)
        floordiv(a, b) -- Same as a // b.
    
    __ge__ = ge(...)
        ge(a, b) -- Same as a>=b.
    
    __getitem__ = getitem(...)
        getitem(a, b) -- Same as a[b].
    
    __gt__ = gt(...)
        gt(a, b) -- Same as a>b.
    
    __iadd__ = iadd(...)
        a = iadd(a, b) -- Same as a += b.
    
    __iand__ = iand(...)
        a = iand(a, b) -- Same as a &= b.
    
    __iconcat__ = iconcat(...)
        a = iconcat(a, b) -- Same as a += b, for a and b sequences.
    
    __ifloordiv__ = ifloordiv(...)
        a = ifloordiv(a, b) -- Same as a //= b.
    
    __ilshift__ = ilshift(...)
        a = ilshift(a, b) -- Same as a <<= b.
    
    __imod__ = imod(...)
        a = imod(a, b) -- Same as a %= b.
    
    __imul__ = imul(...)
        a = imul(a, b) -- Same as a *= b.
    
    __index__ = index(...)
        index(a) -- Same as a.__index__()
    
    __inv__ = inv(...)
        inv(a) -- Same as ~a.
    
    __invert__ = invert(...)
        invert(a) -- Same as ~a.
    
    __ior__ = ior(...)
        a = ior(a, b) -- Same as a |= b.
    
    __ipow__ = ipow(...)
        a = ipow(a, b) -- Same as a **= b.
    
    __irshift__ = irshift(...)
        a = irshift(a, b) -- Same as a >>= b.
    
    __isub__ = isub(...)
        a = isub(a, b) -- Same as a -= b.
    
    __itruediv__ = itruediv(...)
        a = itruediv(a, b) -- Same as a /= b
    
    __ixor__ = ixor(...)
        a = ixor(a, b) -- Same as a ^= b.
    
    __le__ = le(...)
        le(a, b) -- Same as a<=b.
    __lshift__ = lshift(...)
        lshift(a, b) -- Same as a << b.
    
    __lt__ = lt(...)
        lt(a, b) -- Same as a<b.
    
    __mod__ = mod(...)
        mod(a, b) -- Same as a % b.
    
    __mul__ = mul(...)
        mul(a, b) -- Same as a * b.
    
    __ne__ = ne(...)
        ne(a, b) -- Same as a!=b.
    
    __neg__ = neg(...)
        neg(a) -- Same as -a.
    
    __not__ = not_(...)
        not_(a) -- Same as not a.
    
    __or__ = or_(...)
        or_(a, b) -- Same as a | b.
    
    __pos__ = pos(...)
        pos(a) -- Same as +a.
    
    __pow__ = pow(...)
        pow(a, b) -- Same as a ** b.
    
    __rshift__ = rshift(...)
        rshift(a, b) -- Same as a >> b.
    
    __setitem__ = setitem(...)
        setitem(a, b, c) -- Same as a[b] = c.
    
    __sub__ = sub(...)
        sub(a, b) -- Same as a - b.
    
    __truediv__ = truediv(...)
        truediv(a, b) -- Same as a / b.
    
    __xor__ = xor(...)
        xor(a, b) -- Same as a ^ b.
    
    abs(...)
        abs(a) -- Same as abs(a).
    
    add(...)
        add(a, b) -- Same as a + b.
    
    and_(...)
        and_(a, b) -- Same as a & b.
    
    concat(...)
        concat(a, b) -- Same as a + b, for a and b sequences.
    
    contains(...)
        contains(a, b) -- Same as b in a (note reversed operands).
    
    countOf(...)
        countOf(a, b) -- Return the number of times b occurs in a.
    
    delitem(...)
        delitem(a, b) -- Same as del a[b].
    
    eq(...)
        eq(a, b) -- Same as a==b.
    
    floordiv(...)
        floordiv(a, b) -- Same as a // b.
    
    ge(...)
        ge(a, b) -- Same as a>=b.
    
    getitem(...)
        getitem(a, b) -- Same as a[b].
    
    gt(...)
        gt(a, b) -- Same as a>b.
    iadd(...)
        a = iadd(a, b) -- Same as a += b.
    
    iand(...)
        a = iand(a, b) -- Same as a &= b.
    
    iconcat(...)
        a = iconcat(a, b) -- Same as a += b, for a and b sequences.
    
    ifloordiv(...)
        a = ifloordiv(a, b) -- Same as a //= b.
    
    ilshift(...)
        a = ilshift(a, b) -- Same as a <<= b.
    
    imod(...)
        a = imod(a, b) -- Same as a %= b.
    
    imul(...)
        a = imul(a, b) -- Same as a *= b.
    
    index(...)
        index(a) -- Same as a.__index__()
    
    indexOf(...)
        indexOf(a, b) -- Return the first index of b in a.
    
    inv(...)
        inv(a) -- Same as ~a.
    
    invert(...)
        invert(a) -- Same as ~a.
    
    ior(...)
        a = ior(a, b) -- Same as a |= b.
    
    ipow(...)
        a = ipow(a, b) -- Same as a **= b.
    
    irshift(...)
        a = irshift(a, b) -- Same as a >>= b.
    
    is_(...)
        is_(a, b) -- Same as a is b.
    
    is_not(...)
        is_not(a, b) -- Same as a is not b.
    
    isub(...)
        a = isub(a, b) -- Same as a -= b.
    
    itruediv(...)
        a = itruediv(a, b) -- Same as a /= b
    
    ixor(...)
        a = ixor(a, b) -- Same as a ^= b.
    
    le(...)
        le(a, b) -- Same as a<=b.
    
    length_hint(...)
        length_hint(obj, default=0) -> int
        Return an estimate of the number of items in obj.
        This is useful for presizing containers when building from an
        iterable.
        
        If the object supports len(), the result will be
        exact. Otherwise, it may over- or under-estimate by an
        arbitrary amount. The result will be an integer >= 0.
    
    lshift(...)
        lshift(a, b) -- Same as a << b.
    
    lt(...)
        lt(a, b) -- Same as a<b.
    
    mod(...)
        mod(a, b) -- Same as a % b.
    
    mul(...)
        mul(a, b) -- Same as a * b.
    ne(...)
        ne(a, b) -- Same as a!=b.
    
    neg(...)
        neg(a) -- Same as -a.
    
    not_(...)
        not_(a) -- Same as not a.
    
    or_(...)
        or_(a, b) -- Same as a | b.
    
    pos(...)
        pos(a) -- Same as +a.
    
    pow(...)
        pow(a, b) -- Same as a ** b.
    
    rshift(...)
        rshift(a, b) -- Same as a >> b.
    
    setitem(...)
        setitem(a, b, c) -- Same as a[b] = c.
    
    sub(...)
        sub(a, b) -- Same as a - b.
    
    truediv(...)
        truediv(a, b) -- Same as a / b.
    
    truth(...)
        truth(a) -- Return True if a is true, False otherwise.
    
    xor(...)
        xor(a, b) -- Same as a ^ b.

DATA
    __all__ = ['abs', 'add', 'and_', 'attrgetter', 'concat', 'contains', '...

FILE
    /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/operator.py
```



## dir(operator)

```
>>> import operator
>>> dir(operator)
['__abs__', '__add__', '__all__', '__and__', '__builtins__', '__cached__', '__concat__', '__contains__', '__delitem__', '__doc__', '__eq__', '__file__', '__floordiv__', '__ge__', '__getitem__', '__gt__', '__iadd__', '__iand__', '__iconcat__', '__ifloordiv__', '__ilshift__', '__imod__', '__imul__', '__index__', '__inv__', '__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', '__itruediv__', '__ixor__', '__le__', '__loader__', '__lshift__', '__lt__', '__mod__', '__mul__', '__name__', '__ne__', '__neg__', '__not__', '__or__', '__package__', '__pos__', '__pow__', '__rshift__', '__setitem__', '__spec__', '__sub__', '__truediv__', '__xor__', '_abs', 'abs', 'add', 'and_', 'attrgetter', 'concat', 'contains', 'countOf', 'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt', 'iadd', 'iand', 'iconcat', 'ifloordiv', 'ilshift', 'imod', 'imul', 'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift', 'is_', 'is_not', 'isub', 'itemgetter', 'itruediv', 'ixor', 'le', 'length_hint', 'lshift', 'lt', 'methodcaller', 'mod', 'mul', 'ne', 'neg', 'not_', 'or_', 'pos', 'pow', 'rshift', 'setitem', 'sub', 'truediv', 'truth', 'xor']
```





### add()

> ```
> Help on built-in function add in module _operator:
>
> add(...)
>     add(a, b) -- Same as a + b.
> ```

example:

```
>>> import operator, functools
>>> functools.reduce(operator.add, [2, 4, 6]) 		# Function-based +
12
>>> functools.reduce((lambda x, y: x + y), [2, 4, 6]) 
12
```