# encoding=utf-8
print(u"------foo1只是一个普通的内嵌函数----------------------------------------------")
def foo(x):
    y = x
    def foo1():
        a = 1
        return a
    return foo1
print(u"------")










# http://www.brianholdefehr.com/decorators-and-functional-python
# http://www.oschina.net/translate/decorators-and-functional-python
# http://www.cnblogs.com/Alexander-Lee/archive/2010/09/04/python_decreator.html

def before(func):
    def wrapper(*args):
        print("before")
        return func(*args)
    return wrapper
@before
def foo():
    pass