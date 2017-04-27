# Python Study Notes



# Iteration 迭代

如果给定一个list或tuple，我们可以通过 `for` 循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

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





## dict 可以迭代

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



## 字符串也是可迭代对象

```
>>> for ch in 'ABC':
...     print(ch)
...
A
B
C
```



## 如何判断一个对象是可迭代对象?

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



## enumerate

Python内置的 `enumerate` 函数可以把一个list变成索引-元素对，这样就可以在`for`循环中同时迭代索引和元素本身：

```
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C
```