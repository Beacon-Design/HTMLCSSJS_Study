# Python Study Notes



# Built-in Functions (内建函数)

Reference:

https://docs.python.org/3.6/library/functions.html



|                                          |                                          | Built-in Functions                       |                                          |                                          |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| [`abs()`](https://docs.python.org/3.6/library/functions.html#abs) | [`dict()`](https://docs.python.org/3.6/library/functions.html#func-dict) | [`help()`](https://docs.python.org/3.6/library/functions.html#help) | [`min()`](https://docs.python.org/3.6/library/functions.html#min) | [`setattr()`](https://docs.python.org/3.6/library/functions.html#setattr) |
| [`all()`](https://docs.python.org/3.6/library/functions.html#all) | [`dir()`](https://docs.python.org/3.6/library/functions.html#dir) | [`hex()`](https://docs.python.org/3.6/library/functions.html#hex) | [`next()`](https://docs.python.org/3.6/library/functions.html#next) | [`slice()`](https://docs.python.org/3.6/library/functions.html#slice) |
| [`any()`](https://docs.python.org/3.6/library/functions.html#any) | [`divmod()`](https://docs.python.org/3.6/library/functions.html#divmod) | [`id()`](https://docs.python.org/3.6/library/functions.html#id) | [`object()`](https://docs.python.org/3.6/library/functions.html#object) | [`sorted()`](https://docs.python.org/3.6/library/functions.html#sorted) |
| [`ascii()`](https://docs.python.org/3.6/library/functions.html#ascii) | [`enumerate()`](https://docs.python.org/3.6/library/functions.html#enumerate) | [`input()`](https://docs.python.org/3.6/library/functions.html#input) | [`oct()`](https://docs.python.org/3.6/library/functions.html#oct) | [`staticmethod()`](https://docs.python.org/3.6/library/functions.html#staticmethod) |
| [`bin()`](https://docs.python.org/3.6/library/functions.html#bin) | [`eval()`](https://docs.python.org/3.6/library/functions.html#eval) | [`int()`](https://docs.python.org/3.6/library/functions.html#int) | [`open()`](https://docs.python.org/3.6/library/functions.html#open) | [`str()`](https://docs.python.org/3.6/library/functions.html#func-str) |
| [`bool()`](https://docs.python.org/3.6/library/functions.html#bool) | [`exec()`](https://docs.python.org/3.6/library/functions.html#exec) | [`isinstance()`](https://docs.python.org/3.6/library/functions.html#isinstance) | [`ord()`](https://docs.python.org/3.6/library/functions.html#ord) | [`sum()`](https://docs.python.org/3.6/library/functions.html#sum) |
| [`bytearray()`](https://docs.python.org/3.6/library/functions.html#bytearray) | [`filter()`](https://docs.python.org/3.6/library/functions.html#filter) | [`issubclass()`](https://docs.python.org/3.6/library/functions.html#issubclass) | [`pow()`](https://docs.python.org/3.6/library/functions.html#pow) | [`super()`](https://docs.python.org/3.6/library/functions.html#super) |
| [`bytes()`](https://docs.python.org/3.6/library/functions.html#bytes) | [`float()`](https://docs.python.org/3.6/library/functions.html#float) | [`iter()`](https://docs.python.org/3.6/library/functions.html#iter) | [`print()`](https://docs.python.org/3.6/library/functions.html#print) | [`tuple()`](https://docs.python.org/3.6/library/functions.html#func-tuple) |
| [`callable()`](https://docs.python.org/3.6/library/functions.html#callable) | [`format()`](https://docs.python.org/3.6/library/functions.html#format) | [`len()`](https://docs.python.org/3.6/library/functions.html#len) | [`property()`](https://docs.python.org/3.6/library/functions.html#property) | [`type()`](https://docs.python.org/3.6/library/functions.html#type) |
| [`chr()`](https://docs.python.org/3.6/library/functions.html#chr) | [`frozenset()`](https://docs.python.org/3.6/library/functions.html#func-frozenset) | [`list()`](https://docs.python.org/3.6/library/functions.html#func-list) | [`range()`](https://docs.python.org/3.6/library/functions.html#func-range) | [`vars()`](https://docs.python.org/3.6/library/functions.html#vars) |
| [`classmethod()`](https://docs.python.org/3.6/library/functions.html#classmethod) | [`getattr()`](https://docs.python.org/3.6/library/functions.html#getattr) | [`locals()`](https://docs.python.org/3.6/library/functions.html#locals) | [`repr()`](https://docs.python.org/3.6/library/functions.html#repr) | [`zip()`](https://docs.python.org/3.6/library/functions.html#zip) |
| [`compile()`](https://docs.python.org/3.6/library/functions.html#compile) | [`globals()`](https://docs.python.org/3.6/library/functions.html#globals) | [`map()`](https://docs.python.org/3.6/library/functions.html#map) | [`reversed()`](https://docs.python.org/3.6/library/functions.html#reversed) | [`__import__()`](https://docs.python.org/3.6/library/functions.html#__import__) |
| [`complex()`](https://docs.python.org/3.6/library/functions.html#complex) | [`hasattr()`](https://docs.python.org/3.6/library/functions.html#hasattr) | [`max()`](https://docs.python.org/3.6/library/functions.html#max) | [`round()`](https://docs.python.org/3.6/library/functions.html#round) |                                          |
| [`delattr()`](https://docs.python.org/3.6/library/functions.html#delattr) | [`hash()`](https://docs.python.org/3.6/library/functions.html#hash) | [`memoryview()`](https://docs.python.org/3.6/library/functions.html#func-memoryview) | [`set()`](https://docs.python.org/3.6/library/functions.html#func-set) |                                          |



## eval()

eval() 函数用来执行一个字符串表达式，并返回表达式的值。

> ```
> eval(...)
>     eval(source[, globals[, locals]]) -> value
>     
>     Evaluate the source in the context of globals and locals.
>     The source may be a string representing a Python expression
>     or a code object as returned by compile().
>     The globals must be a dictionary and locals can be any mapping,
>     defaulting to the current globals and locals.
>     If only globals is given, locals defaults to it.
> ```

#### 函数语法

```
eval(expression[, globals[, locals]])
```

#### 参数

- expression -- 表达式。
- globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
- locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

#### 返回值

返回表达式计算结果

#### 实例

```
>>>x = 7
>>> eval( '3 * x' )
21
>>> eval('pow(2,2)')
4
>>> eval('2 + 2')
4
>>> eval("n + 4")
85
```





## filter()

**filter()** 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

#### 函数语法:

```
filter(function, iterable)
```

#### 参数说明：

- function -- 判断函数。
- iterable -- 可迭代对象

#### 返回值:

返回列表。

#### 实例:

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def is_odd(n):
    return n % 2 == 1
 
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)
```

```
[1, 3, 5, 7, 9]
```







## isinstance() 

isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。

> isinstance() 与 type() 区别：
>
> - type() 不会认为子类是一种父类类型，不考虑继承关系。
> - isinstance() 会认为子类是一种父类类型，考虑继承关系。
>
> 如果要判断两个类型是否相同推荐使用 isinstance()。

> ```
> isinstance(...)
>     isinstance(object, class-or-type-or-tuple) -> bool
>     
>     Return whether an object is an instance of a class or of a subclass thereof.
>     With a type as second argument, return whether that is the object's type.
>     The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for
>     isinstance(x, A) or isinstance(x, B) or ... (etc.).
>
> ```

#### 函数语法:

```
isinstance(object, classinfo)
```

#### 参数说明：

- object -- 实例对象。
- classinfo -- 可以是直接或间接类名、基本类型或者有它们组成的元组。

#### 返回值:

如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。。

#### 实例:

```
>>>a = 2
>>> isinstance (a,int)
True
>>> isinstance (a,str)
False
>>> isinstance (a,(str,int,list))    # 是元组中的一个返回 True
True
```

#### type() 与 isinstance() 区别:

```
class A:
    pass
 
class B(A):
    pass
 
isinstance(A(), A)    # returns True
type(A()) == A        # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False
```





## open()

python open() 函数用于打开一个文件，创建一个 `file` 对象，相关的方法才可以调用它进行读写。

更多文件操作可参考：[Python 文件I/O](http://www.runoob.com/python/python-files-io.html)。

> ```
> open(...)
>     open(file, mode='r', buffering=-1, encoding=None,
>          errors=None, newline=None, closefd=True, opener=None) -> file object
>     
>     Open file and return a stream.  Raise IOError upon failure.
>     
>     file is either a text or byte string giving the name (and the path
>     if the file isn't in the current working directory) of the file to
>     be opened or an integer file descriptor of the file to be
>     wrapped. (If a file descriptor is given, it is closed when the
>     returned I/O object is closed, unless closefd is set to False.)
>     
>     mode is an optional string that specifies the mode in which the file
>     is opened. It defaults to 'r' which means open for reading in text
>     mode.  Other common values are 'w' for writing (truncating the file if
>     it already exists), 'x' for creating and writing to a new file, and
>     'a' for appending (which on some Unix systems, means that all writes
>     append to the end of the file regardless of the current seek position).
>     In text mode, if encoding is not specified the encoding used is platform
>     dependent: locale.getpreferredencoding(False) is called to get the
>     current locale encoding. (For reading and writing raw bytes use binary
> ```

#### 函数语法:

```
open(name[, mode[, buffering]])
```

#### 参数说明：

- name : 一个包含了你要访问的文件名称的字符串值。
- mode : mode 决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
- buffering : 如果 buffering 的值被设为 0，就不会有寄存。如果 buffering 的值取 1，访问文件时会寄存行。如果将 buffering 的值设为大于 1 的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

#### 不同模式打开文件的完全列表：

| 模式   | 描述                                       |
| ---- | ---------------------------------------- |
| r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。         |
| rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。   |
| r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。                |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。          |
| w    | 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 |
| wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 |
| w+   | 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 |
| a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

#### file 对象方法

**file.read([size])** size未指定则返回整个文件,如果文件大小>2倍内存则有问题.f.read()读到文件尾时返回""(空字串)

**file.readline()** 返回一行

**file.readline([size]) **返回包含size行的列表,size 未指定则返回全部行

**for line in file: print line **#通过迭代器访问

**file.write("hello\n")** #如果要写入字符串以外的数据,先将他转换为字符串.

**file.tell()** 返回一个整数,表示当前文件指针的位置(就是到文件头的比特数).

**file.seek(偏移量,[起始位置])** 用来移动文件指针.

- 偏移量:单位:比特,可正可负
- 起始位置:0-文件头,默认值;1-当前位置;2-文件尾

**file.close()** 关闭文件



## type()

type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。

> isinstance() 与 type() 区别：
>
> - type() 不会认为子类是一种父类类型，不考虑继承关系。
> - isinstance() 会认为子类是一种父类类型，考虑继承关系。
>
> 如果要判断两个类型是否相同推荐使用 isinstance()。

> ```
>
> ```

#### 函数语法:

```
class type(name, bases, dict)
```

#### 参数说明：

- name -- 类的名称。
- bases -- 基类的元组。
- dict -- 字典，类内定义的命名空间变量。

#### 返回值:

一个参数返回对象类型, 三个参数，返回新的类型对象。

#### 实例:

```
# 一个参数实例
>>> type(1)
<class 'int'>
>>> type('apple')
<class 'str'>
>>> type([2])
<class 'list'>
>>> type({0:'zero'})
<class 'dict'>
>>> x = 1
>>> type(x) == int		# 判断类型是否相等
True

# 三个参数
>>> class D(object):
...     a = 1
... 
>>> D = type('D', (object,), dict(a=1))		# 产生一个新的类型 D
>>> D
<class '__main__.D'>
```

#### type() 与 isinstance() 区别：

```
class A:
    pass
 
class B(A):
    pass
 
isinstance(A(), A)    # returns True
type(A()) == A        # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False
```