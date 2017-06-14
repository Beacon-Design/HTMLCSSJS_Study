# module webbrowser

**Source code:** [Lib/webbrowser.py](https://hg.python.org/cpython/file/3.4/Lib/webbrowser.py)

(https://hg.python.org/cpython/file/3.4/Lib/webbrowser.py)

## help(webbrowser)

```
Help on module webbrowser:

NAME
    webbrowser - Interfaces for launching and remotely controlling Web browsers.

MODULE REFERENCE
    http://docs.python.org/3.4/library/webbrowser
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.Exception(builtins.BaseException)
        Error
    
    class Error(builtins.Exception)
     |  Method resolution order:
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args

FUNCTIONS
    get(using=None)
        Return a browser launcher instance appropriate for the environment.
    
    open(url, new=0, autoraise=True)
    
    open_new(url)
    
    open_new_tab(url)
    
    register(name, klass, instance=None, update_tryorder=1)
        Register a browser connector and, optionally, connection.

DATA
    __all__ = ['Error', 'open', 'open_new', 'open_new_tab', 'get', 'regist...

FILE
    /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/webbrowser.py
```

## dir(webbrowser)

```
>>> dir(webbrowser)
['BackgroundBrowser', 'BaseBrowser', 'Chrome', 'Chromium', 'Elinks', 'Error', 'Galeon', 'GenericBrowser', 'Grail', 'Konqueror', 'MacOSX', 'MacOSXOSAScript', 'Mozilla', 'Netscape', 'Opera', 'UnixBrowser', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_browsers', '_synthesize', '_tryorder', 'get', 'main', 'open', 'open_new', 'open_new_tab', 'os', 'register', 'register_X_browsers', 'shlex', 'shutil', 'subprocess', 'sys']
```



## In terminal

The script **webbrowser** can be used as a command-line interface for the module. It accepts an URL as the argument. It accepts the following optional parameters: `-n` opens the URL in a new browser window, if possible; `-t` opens the URL in a new browser page (“tab”). The options are, naturally, mutually exclusive. Usage example:

```
python -m webbrowser -t "http://www.python.org"
```

in terminal:

```
$ python3 -m webbrowser -n "http://www.baidu.com"
```



### exception webbrowser.Error

> ```
> exception webbrowser.Error
>
> Exception raised when a browser control error occurs.
> ```



### webbrowser.open()

> ```
> webbrowser.open(url, new=0, autoraise=True)
>
> Display url using the default browser. If new is 0, the url is opened in the same browser window if possible. If new is 1, a new browser window is opened if possible. If new is 2, a new browser page (“tab”) is opened if possible. If autoraise is True, the window is raised if possible (note that under many window managers this will occur regardless of the setting of this variable).
>
> Note that on some platforms, trying to open a filename using this function, may work and start the operating system’s associated program. However, this is neither supported nor portable.
> ```

example:

```python
>>> import webbrowser
>>> webbrowser.open("http://www.baidu.com", 2, autoraise=True)
True
```



### webbrowser.open_new()

> ```
> webbrowser.open_new(url)
>
> Open url in a new window of the default browser, if possible, otherwise, open url in the only browser window.
> ```

example:

```python
>>> import webbrowser
>>> webbrowser.open_new("http://www.baidu.com")
True
```



### webbrowser.open_new_tab()

> ```
> webbrowser.open_new_tab(url)
> Open url in a new page (“tab”) of the default browser, if possible, otherwise equivalent to open_new().
> ```

example:

```python
>>> import webbrowser
>>> webbrowser.open_new_tab("http://www.baidu.com")
True
```

