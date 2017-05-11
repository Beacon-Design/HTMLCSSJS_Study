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