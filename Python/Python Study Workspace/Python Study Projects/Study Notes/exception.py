# coding=utf-8

print('''------exception--------------------------------------

Exception          The base class for all exceptions
AttributeError     Raised when attribute reference or assignment fails
IOError            Raised when trying to open a nonexistent file (among other things)
IndexError         Raised when using a nonexistent index on a sequence
KeyError           Raised when using a nonexistent key on a mapping
NameError          Raised when a name (variable) is not found
SyntaxError        Raised when the code is ill-formed
TypeError          Raised when a built-in operation or function is applied to 
                   an object of the wrong type
ValueError         Raised when a built-in operation or function is applied to 
                   an object with the correct type, but with an inappropriate value
ZeroDivisionError  Raised when the second argument of a division or modulo operation is zero


常见的异常：
AttributeError 调用不存在的方法引发的异常
EOFError 遇到文件末尾引发的异常
ImportError 导入模块出错引发的异常
IndexError 列表月越界引发的异常
IOError I/O操作引发的异常，如打开文件出错等
KeyError 使用字典中不存在的关键字引发的异常
NameError 使用不存在的变量名引发的异常
TabError 语句块缩进不正确引发的异常
ValueError 搜索列表中不存在值引发的异常
ZeroDivisionError 除数为零引发的异常
 
多重异常的处理
可以在try语句中嵌套另一个try语句
一旦发生异常，python匹配最近的except语句，
若是内部except能够处理该异常，则外围try语句不会捕获异常。
若是不能，或者忽略，外围try处理
 
引发异常
python中可以通过raise语句手工引发异常，并向异常传递数据
使用raise可以定义新的错误类型，以适应脚本的需要
 
格式：
raise 异常名
raise 类名(异常信息)

------try...except...-----------------------------------------
We can handle exceptions using the try..except statement. 
We basically put our usual statements within the try-block 
and put all our error handlers in the except-block.

You can also have an else clause associated with a try..except block. 
The else clause is executed if no exception occurs

''')

print('''
# example 01
''')
try:
    x = input("ENTER A NUMBER:")
    y = input("ENTER A NUMBER:")
    print(int(x)/int(y))
except ZeroDivisionError:
    print("y can not be zero")
except ValueError:
    print("y must be a number")
    
    
print('''
# example 02 
------Catching Two Exceptions with One Block------------------------------
If you want to catch more than one exception type with one block, you can 
specify them all in a tuple
''')
try:
    x = input("ENTER A NUMBER:")
    y = input("ENTER A NUMBER:")
    print(int(x)/int(y))
except (ZeroDivisionError, ValueError, NameError):
    print("your numbers were bogus ")
    

print('''
# example 03
------Catching the Object----------------------------------------
If you want access to the exception object itself in an except clause, you can use two arguments
instead of one. (Note that even when you are catching multiple exceptions, you are supplying
except with only one argument—a tuple.)
''')
try:
    x = input("ENTER A NUMBER:")
    y = input("ENTER A NUMBER:")
    print(int(x)/int(y))
except (ZeroDivisionError, ValueError) as e:
    print(e)
    

print('''
# example 04
------catch all exceptions in a piece of code----------------------------
Catching all exceptions like this is risky business because it will hide errors you haven’t thought
of as well as those you’re prepared for. It will also trap attempts by the user to terminate execution by Ctrl-C,
attempts by functions you call to terminate by sys.exit, and so on. In most cases, it would be better to use
(except Exception as e) and perhaps do some checking on the exception object as e.
''')
try:
    x = input("ENTER A NUMBER:")
    y = input("ENTER A NUMBER:")
    print(int(x)/int(y))
except Exception as e:
    print(e)


print('''
# example 05
''')
try:
    text = input('Enter something --> ')
except EOFError:
    print ('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print ('You cancelled the operation.')
else:
    print ('You entered {}'.format(text),"\n")
    
    
    
print("""
------raising exceptions--------------------------------
""")

class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    text = input("Enter -->")
    if len(text) < 3:
        raise ShortInputException(len(text),3)
except EOFError:
    print("EOFError")
except ShortInputException as ex:
    print("ShortInputException: The input was "\
          "{} long,excepted at least {}".format(ex.length,ex.atleast))
else:
    print("No exception was raised.")
    
print('''

In the except clause, we mention the class of error which will be stored 
as the variable name to hold the corresponding error/exception object
''')
 
print('''
------try...finally--------------------------------------------
Suppose you are reading a file in your program. How do you ensure 
that the file object is closed properly whether or not an exception 
was raised? This can be done using the finally block

''')    
import sys
import time

f = None
try:
    f = open("p.txt")
    # Our usual file-reading idiom
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print (line)
        sys.stdout.flush()
        print ("Press ctrl+c now")
        # To make sure it runs for a while
        time.sleep(2)
except IOError:
    print ("Could not find file p.txt")
except KeyboardInterrupt:
    print ("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print ("(Cleaning up: Closed the file)")  
    
print('''
------with statement---------------------------------------
The difference here is that we are using the open function with 
the with statement - we leave the closing of the file to be done 
automatically by with open

What happens behind the scenes is that there is a protocol used 
by the with statement. It fetches the object returned by the open
statement,let's call it "thefile" in the case.

It always calls the thefile.__enter__ function before starting the 
block of code under it and always calls thefile.__exit__ after 
finishing the block of code

So the code that we would have written in a finally block should be 
taken care of automatically by the __exit__ method. This is what helps 
us to avoid having to use explicit try..finally statements repeatedly

''')  

with open("p.txt") as f:
    for line in f:
        print(line)   
    
print('''-----------------------------------------------------------------
------Custom Exception Classes--------------------------------------------
how do you create exception classes? Just like any other class—but be sure 
to subclass Exception (either directly or indirectly, which means that 
subclassing any other built-in exception is okay)

class SomeCustomException(Exception): pass

''') 
    
 
print('''------Exceptions and Functions-----------------------------------
If an exception is raised inside a function,and isn't handled there, it 
propagates (bubbles up) to the place where the function was called. If it 
isn't handled there either, it continues propagating until it reaches the 
main program (the global scope), and if there is no exception handler there, 
the program halts with a stack trace.


>>> def faulty():
... raise Exception('Something is wrong')
>>> def ignore_exception():
... faulty()
...
>>> def handle_exception():
... try:
... faulty()
... except:
... print 'Exception handled'
...
>>> ignore_exception()
Traceback (most recent call last):
File '<stdin>', line 1, in ?
File '<stdin>', line 2, in ignore_exception
File '<stdin>', line 2, in faulty
Exception: Something is wrong
>>> handle_exception()
Exception handled


''') 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
    
    
    