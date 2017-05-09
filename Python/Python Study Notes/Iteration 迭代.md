# Python Study Notes



# Iteration 迭代

如果给定一个list或tuple，我们可以通过 `for` 循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

> *Terminology*
>
> this book has a very strong preference for using the term **iterable** to refer to an object that supports the iter call, 
>
> and **iterator** to refer to an object returned by an iterable on iter that supports the next(I) call. Both these calls are defined ahead.
>
> the term **generator** —which refers to objects that automatically support the iteration protocol, and hence are iterable—even though all iterables generate results!

The concept of “iterable objects” is relatively recent in Python, but it has come to permeate the language’s design. It’s essentially a generalization of the notion of sequences—an object is considered iterable if it is either a physically stored sequence, or an object that produces one result at a time in the context of an iteration tool like a `for` loop. In a sense, **iterable objects include both physical sequences and virtual sequences computed on demand.**

all iteration tools that scan objects from left to right in Python, including `for` loops, the list comprehensions , `in` membership tests, the `map` built-in function, and more.



### The Iteration Protocol: File Iterators

understand the iteration protocol is to see how it works with a built-in type such as the file：

call the iteration protocol in Python. Any object with a `__next__` method to advance to a next result, which raises `StopIteration` at the end of the series of results, is considered an iterator in Python. because all iteration tools normally work internally by calling `__next__` on each iteration and catching the `StopIteration` exception to determine when to exit.

> a `next(X)` built-in function is also available in both Python 3.X and 2.X (2.6 and later)
>
> calls `X.__next__()` in 3.X and `X.next()` in 2.X.



### Manual Iteration: iter and next



### `for` loop

`for` loop can work on any sequence type in Python, including lists, tuples, and strings, like this:

```
>>> for x in [1, 2, 3, 4]: print(x ** 2, end=' ') 
...
1 4 9 16

>>> for x in (1, 2, 3, 4): print(x ** 3, end=' ') .
..
1 8 27 64

>>> for x in 'spam': print(x * 2, end=' ') 
...
ss pp aa mm
```

在Python中，迭代是通过 `for ... in` 来完成的.

> 而很多语言比如C或者Java，迭代list是通过下标完成的，比如Java代码：
>
> ```
> for (i=0; i<list.length; i++) {
>     n = list[i];
> }
> ```

同时引用了两个变量:

```
>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print(x, y)
...
1 1
2 4
3 9
```



#### best way to read a text file

the best way to read a text file line by line today is to not read it at all—instead, allow the `for` loop to automatically call `__next__` to advance to the next line on each iteration.

for three reasons: 

1. it’s the simplest to code, 
2. might be the quickest to run, 
3. and is the best in terms of memory usage.

```
>>> for line in open('script2.py'): 		# Use file iterators to read by lines
... print(line.upper(), end='') 			# Calls __next__, catches StopIteration
...
IMPORT SYS 
PRINT(SYS.PATH) 
X = 2 
PRINT(X ** 32)
```

The older, original way to achieve the same effect with a for loop is to call the file readlines method to load the file’s content into memory as a list of line strings:

```
>>> for line in open('script2.py').readlines(): 
... 	print(line.upper(), end='') 
...
IMPORT SYS 
PRINT(SYS.PATH) 
X = 2 
PRINT(X ** 32)
```

read a file line by line with a `while` loop:

> this may run slower than the iterator-based `for` loop version, because itera-tors run at C language speed inside Python, whereas the `while` loop version runs Python byte code through the Python virtual machine.
>
> Anytime we trade Python code for C code, speed tends to increase.









### dict 可以迭代

```
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
...     print(key)
...
a
c
b
```

因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

默认情况下，dict迭代的是key。如果要迭代value，可以用 `for value in d.values():`，如果要同时迭代key和value，可以用 `for k, v in d.items():`。

```
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for value in d.values():
...     print(value)
... 
3
1
2
```

```
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for k, v in d.items():
...     print(k, v)
... 
c 3
a 1
b 2
```



### 字符串也是可迭代对象

```
>>> for ch in 'ABC':
...     print(ch)
...
A
B
C
```



### 如何判断一个对象是可迭代对象?

通过collections模块的Iterable类型判断：

```
>>> from collections import Iterable
>>> isinstance('abc', Iterable) 	# str是否可迭代
True
>>> isinstance([1,2,3], Iterable)   # list是否可迭代
True
>>> isinstance(123, Iterable) 		# 整数是否可迭代
False
```



### enumerate

Python内置的 `enumerate` 函数可以把一个list变成索引-元素对，这样就可以在`for`循环中同时迭代索引和元素本身：

```
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C
```