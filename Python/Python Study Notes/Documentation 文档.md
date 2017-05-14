# Documentation 文档



## Python Documentation Sources

```
Python documentation sources

Form							Role

# comments						In-file documentation
The dir function 				Lists of attributes available in objects
Docstrings: __doc__ 			In-file documentation attached to objects
PyDoc: the help function 		Interactive help for objects
PyDoc: HTML reports 			Module documentation in a browser
Sphinx third-party tool 		Richer documentation for larger projects
The standard manual set 		Official language and library descriptions
Web resources 					Online tutorials, examples, and so on
Published books					Commercially polished reference texts
```



#### `#` Comments

Python simply ignores all the text following a # (as long as it’s not inside a string literal)

docstrings are best for larger functional documentation (e.g., “my file does this”)

and # comments are best limited to smaller code documentation (e.g., “this strange expression does that”) and are best limited in scope to a statement or small group of statements within a script or function.

#### dir函数



### Docstrings: `__doc__`

Python supports documentation that is automatically attached to objects and retained at runtime for inspection. Syntactically, such comments are coded as strings at the tops of module files and function and class statements, before any other executable code (# comments, including Unix-stye #! lines are OK before them). Python automatically stuffs the text of these strings, known informally as docstrings, into the `__doc__` attributes of the corresponding objects.

#### User-defined docstrings

For example, consider the following file, *docstrings.py*. Its docstrings appear at the beginning of the file and at the start of a function and a class within it. Here, I’ve used triple-quoted block strings for multiline comments in the file and the function, but any sort of string will work; single- or double-quoted one-liners like those in the class are fine, but don’t allow multiple-line text.

```
""" 
Module documentation 
Words Go Here 
"""

spam = 40

def square(x):
	""" 
	function documentation 
	can we have your liver then?
	""" 
	return x ** 2 				# square

class Employee:
	"class documentation" 
	pass

print(square(4)) 
print(square.__doc__)
```

The whole point of this documentation protocol is that your comments are *retained* for inspection in `__doc__` attributes after the file is imported. Thus, to display the doc-strings associated with the module and its objects, we simply import the file and print their `__doc__` attributes, where Python has saved the text:

```
>>> import docstrings 
16

	function documentation 
	can we have your liver then?

>>> print(docstrings.__doc__)

Module documentation 
Words Go Here

>>> print(docstrings.square.__doc__)

	function documentation 
	can we have your liver then?

>>> print(docstrings.Employee.__doc__) 
	class documentation
```

you will generally want to use `print` to print docstrings; otherwise, you’ll get a single string with embedded \n newline characters.

You can also attach docstrings to methods of classes

To fetch the docstring of a method function inside a class within a module, you would simply extend the path to go through the class: `module.class.method.__doc__`

#### Built-in docstrings

built-in modules and objects in Python use similar techniques to attach documentation above and beyond the attribute lists returned by `dir`.

For example, to see an actual human-readable description of a built-in module, import it and print its `__doc__` string:

```
>>> import sys
>>> print(sys.__doc__)
This module provides access to some objects used or maintained by the interpreter and to functions that interact strongly with the interpreter.
...
```

Functions, classes, and methods within built-in modules have attached descriptions in their `__doc__` attributes as well:

```
>>> print(sys.getrefcount.__doc__) 
getrefcount(object) -> integer

Return the reference count of object. The count returned is generally one higher than you might expect, because it includes the (temporary) reference as an argument to getrefcount().
```



### PyDoc: The help Function

the `help` function it invokes PyDoc to generate a simple textual report for any Python object.

```
>>> import docstrings
>>> help(docstrings.square) 
Help on function square in module docstrings:
square(x)
	function documentation 
	can we have your liver then?
```

### PyDoc: HTML Reports

- Prior to 3.3, Python ships with a simple GUI desktop client for submitting search requests. This client launches a web browser to view documentation produced by an automatically started local server.


- As of 3.3, the former GUI client is replaced by an all-browser interface scheme, which combines both search and display in a web page that communicates with an automatically started local server.
- Python 3.2 straddles this fence, supporting both the original GUI client scheme, as well as the newer all-browser mode mandated as of 3.3.

### Common Coding Gotchas

**Don’t code C in Python.** 

A reminder for C/C++ programmers: you don’t need to type parentheses around tests in if and while headers (e.g., if (X==1):). You can, if you like (any expression can be enclosed in parentheses), but they are fully superfluous in this context. Also, do not terminate all your statements with semicolons; it’s technically legal to do this in Python as well, but it’s totally useless unless you’re placing more than one statement on a single line (the end of a line normally terminates a statement). And remember, don’t embed assignment statements in while loop tests, and don’t use {} around blocks (indent your nested code blocks consistently instead).

**Use simple for loops instead of while or range.**

 Another reminder: a simple `for` loop (e.g., `for x in seq:`) is almost always simpler to code and often quicker to run than a `while` or `range` based counter loop. Because Python handles indexing internally for a simple `for`, it can sometimes be faster than the equivalent `while`, though this can vary per code and Python. For code simplicity alone, though, avoid the temptation to count things in Python!

**Beware of mutables in assignments.** 

you need to be careful about using mutables in a multiple-target assignment (`a = b = []`), as well as in an augmented assignment (`a += [1, 2]`). In both cases, in-place 

**Don’t expect results from functions that change objects in place.** 

We encountered this one earlier, too: in-place change operations like the list.append and list.sort methods introduced in Chapter 8 do not return values (other than None), so you should call them without assigning the result. It’s not uncommon for beginners to say something like mylist = mylist.append(X) to try to get the result of an append, but what this actually does is assign mylist to None, not to the modified list (in fact, you’ll lose your reference to the list altogether). A more devious example of this pops up in Python 2.X code when trying to step through dictionary items in a sorted fashion. It’s fairly common to see code like for k in D.keys().sort():. This almost works—the keys method builds a keys list, and the sort method orders it—but because the sort method returns None, the loop fails because it is ultimately a loop over None (a nonsequence). This fails even sooner in Python 3.X, because dictionary keys are views, not lists! To code this correctly, either use the newer sorted built-in function, which returns the sorted list, or split the method calls out to statements: Ks = list(D.keys()), then Ks.sort(), and finally, for k in Ks:. This, by the way, is one case where you may. still want to call the keys method explicitly for looping, instead of relying on the dictionary iterators—iterators do not sort.

**Always use parentheses to call a function.** 

You must add parentheses after a function name to call it, whether it takes arguments or not (e.g., use function(), not function). In the next part of this book, we’ll learn that functions are simply objects that have a special operation—a call that you trigger with the parentheses. They can be referenced like any other object without triggering a call. In classes, this problem seems to occur most often with files; it’s common to see beginners type file.close to close a file, rather than file.close(). Because it’s legal to reference a function without calling it, the first version with no parentheses succeeds silently, but it does not close the file!

**Don’t use extensions or paths in imports and reloads.** 

Omit directory paths and file extensions in import statements—say import mod, not import mod.py. We discussed module basics in Chapter 3 and will continue studying modules in Part V. Because modules may have other extensions besides .py (.pyc, for instance), hardcoding a particular extension is not only illegal syntax, it doesn’t make sense. Python picks an extension automatically, and any platform-specific directory path syntax comes from module search path settings, not the import statement.

**And other pitfalls in other parts.** 

Be sure to also see the built-in type warnings at the end of the prior part, as they may qualify as coding issues too. There are additional “gotchas” that crop up commonly in Python coding—losing a built-in function by reassigning its name, hiding a library module by using its name for one of your own, changing mutable argument defaults, and so on—but we don’t have enough background to cover them yet. To learn more about both what you should and shouldn’t do in Python, you’ll have to read on; later parts extend the set of “gotchas” and fixes we’ve added to here.