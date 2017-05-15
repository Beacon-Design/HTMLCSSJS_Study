# Python Study Notes



# List Comprehensions 列表生成式

列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

Together with `for` loops, list comprehensions are one of the most prominent contexts in which the iteration protocol is applied.

要生成list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` 可以用 `list(range(1, 11))` ：

```
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```



生成 `[1*1, 2*2, 3*3, ..., 10*10]`, 列表生成式则:

```
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

> 相等的循环表达方式：
>
> ```
> >>> L = []
> >>> for x in range(1, 11):
> ...    L.append(x * x)
> ...
> >>> L
> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
> ```



在 `for` 循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

```
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
```
可以使用两层循环:

```
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```


example:

```
>>> L = [1, 2, 3, 4, 5]
>>> for i in range(len(L)): 
... 	L[i] += 10 
...
>>> L 
[11, 12, 13, 14, 15]
```

The list comprehension isn’t exactly the same as the for loop statement version because it makes a new list object (which might matter if there are multiple references to the original list)

```
>>> L = [x + 10 for x in L]
>>> L 
[21, 22, 23, 24, 25]
```



### List Comprehension Basics

Syntactically, its syntax is derived from a construct in set theory notation that applies an operation to each item in a set, but you don’t have to know set theory to use this tool

```
L = [x + 10 for x in L]
```

Technically speaking, list comprehensions are never really required because we can always build up a list of expression results manually with for loops that append results as we go:

```
>>> res = []
>>> for x in L:
... 	res.append(x + 10) 
...
>>> res 
[31, 32, 33, 34, 35]
```

> this is exactly what the list comprehension does internally.

**list comprehensions might run much faster than manual `for` loop statements** (often roughly twice as fast) because their iterations are performed at C language speed inside the interpreter, rather than with manual Python code. Especially for larger data sets, there is often a major performance advantage to using this expression.



### Using List Comprehensions on Files

Anytime we start thinking about performing an operation on each item in a sequence, we’re in the realm of list comprehensions.

the file object has a `readlines` method that loads the file into a list of line strings all at once:

```
>>> f = open('script2.py')
>>> lines = f.readlines()
>>> lines 
['import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n']
```

each line in the list through the string `rstrip` method to remove whitespace on the right side (a `line[:−1]` slice would work, too, but only if we can be sure all lines are properly `\n` terminated, and this may not always be the case for the last line in a file):

```
>>> lines = [line.rstrip() for line in lines]
>>> lines 
['import sys', 'print(sys.path)', 'x = 2', 'print(x ** 32)']
```



### Extended List Comprehension Syntax

#### Filter clauses: if

the `for` loop nested in a comprehension expression can have an associated `if` clause to filter out of the result items for which the test is not true.

```
>>> lines = [line.rstrip() for line in open('script2.py') if line[0] == 'p']
>>> lines 
['print(sys.path)', 'print(x ** 32)']
```

we can always translate a list comprehension to a `for` statement by appending as we go and further indenting each successive part:

```
>>> res = []
>>> for line in open('script2.py'): 
... 	if line[0] == 'p':
... 		res.append(line.rstrip()) 
...
>>> res 
['print(sys.path)', 'print(x ** 32)']
```



#### Nested loops: for

List comprehensions may contain nested loops, coded as a series of `for` clauses. In fact, their full syntax allows for any number of `for` clauses, each of which can have an optional associated `if` clause.

collects all the ordered combinations of the characters in two strings:

```
>>> [x + y for x in 'abc' for y in 'lmn'] 
['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
```

The following is an equivalent, but likely slower, alternative way to achieve the same effect:

```
>>> res = []
>>> for x in 'abc':
... 	for y in 'lmn':
... 		res.append(x + y) 
...
>>> res 
['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
```





