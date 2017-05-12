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







