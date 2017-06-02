

# module html

This module defines utilities to manipulate HTML.



## help(html)

```
Help on package html:

NAME
    html - General functions for HTML manipulation.

MODULE REFERENCE
    http://docs.python.org/3.4/library/html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

PACKAGE CONTENTS
    entities
    parser

FUNCTIONS
    escape(s, quote=True)
        Replace special characters "&", "<" and ">" to HTML-safe sequences.
        If the optional flag quote is true (the default), the quotation mark
        characters, both double quote (") and single quote (') characters are also
        translated.
    
    unescape(s)
        Convert all named and numeric character references (e.g. &gt;, &#62;,
        &x3e;) in the string s to the corresponding unicode characters.
        This function uses the rules defined by the HTML 5 standard
        for both valid and invalid character references, and the list of
        HTML 5 named character references defined in html.entities.html5.

DATA
    __all__ = ['escape', 'unescape']

FILE
    /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/html/__init__.py
```





## dir(html)

```
>>> import html
>>> dir(html)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_charref', '_html5', '_invalid_charrefs', '_invalid_codepoints', '_re', '_replace_charref', 'entities', 'escape', 'unescape']
```



### html.escape()

```
html.escape(s, quote=True)
```

Convert the characters `&`, `<` and `>` in string *s* to HTML-safe sequences. Use this if you need to display text that might contain such characters in HTML. If the optional flag *quote* is true, the characters (`"`) and (`'`) are also translated; this helps for inclusion in an HTML attribute value delimited by quotes, as in `<a href="...">`.

> ```
> Help on function escape in module html:
>
> escape(s, quote=True)
>     Replace special characters "&", "<" and ">" to HTML-safe sequences.
>     If the optional flag quote is true (the default), the quotation mark
>     characters, both double quote (") and single quote (') characters are also
>     translated.
> ```

example:

```
>>> import html
>>> s = ''' A < A > A & " A ' '''
>>> html.escape(s, quote=True)
' A &lt; A &gt; A &amp; &quot; A &#x27; '

>>> html.escape("'", quote=True)
'&#x27;'
>>> html.escape("'", quote=False)
"'"

>>> html.escape('"', quote=True)
'&quot;'
>>> html.escape('"', quote=False)
'"'
```





### html.unescape()

```
html.unescape(s)
```

Convert all named and numeric character references (e.g. `&gt;`, `&#62;`, `&x3e;`) in the string *s* to the corresponding unicode characters. This function uses the rules defined by the HTML 5 standard for both valid and invalid character references, and the [`list of HTML 5 named character references`](https://docs.python.org/3/library/html.entities.html#html.entities.html5).

> ```
> Help on function unescape in module html:
>
> unescape(s)
>     Convert all named and numeric character references (e.g. &gt;, &#62;,
>     &x3e;) in the string s to the corresponding unicode characters.
>     This function uses the rules defined by the HTML 5 standard
>     for both valid and invalid character references, and the list of
>     HTML 5 named character references defined in html.entities.html5.
> ```

example:

```
>>> import html
>>> s1 = "&gt;"
>>> s2 = "&#62;"
>>> s3 = "&x3e;"
>>> html.unescape(s1)
'>'
>>> html.unescape(s2)
'>'
>>> html.unescape(s3)
'&x3e;'
```







#### ...

#### ...

#### ...

