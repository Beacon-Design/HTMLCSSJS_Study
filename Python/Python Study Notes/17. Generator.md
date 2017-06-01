

# generator

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。**在Python中，这种一边循环一边计算的机制，称为生成器：generator。**

要创建一个generator。第一种方法，把一个列表生成式的`[]`改成`()`：

```
>>> L = [x * x for x in range(10)]				
>>> L											# L是一个list
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>		# g是一个generator
```

> 如果要一个一个打印出来，可以通过`next()`函数获得generator的下一个返回值：

> ```
> >>> next(g)					# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值
> 0
> >>> next(g)
> 1
> >>> next(g)
> 4
> >>> next(g)
> 9
> >>> next(g)
> 16
> >>> next(g)
> 25
> >>> next(g)
> 36
> >>> next(g)
> 49
> >>> next(g)
> 64
> >>> next(g)
> 81
> >>> next(g)
> Traceback (most recent call last):				# 没有更多的元素时，抛出StopIteration的错误。
>   File "<stdin>", line 1, in <module>
> StopIteration
> ```

正确的方法是使用 `for` 循环，因为generator也是可迭代对象：

```
>>> g = (x * x for x in range(10))
>>> for n in g:
...     print(n)
... 
0
1
4
9
16
25
36
49
64
81
```

