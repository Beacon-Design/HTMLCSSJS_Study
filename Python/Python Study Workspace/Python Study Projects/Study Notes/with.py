# coding=utf-8
print('''------V1-----------------------------------------------------------------------''')

file = open("p.txt")
data = file.read()
file.close()

print('''------V2-----------------------------------------------------------''')

file = open("p.txt")
try:
    data = file.read()
finally:
    file.close()

print('''------with version----------------------------------------------------------''')

with open("p.txt") as file:
    data = file.read()    
    

print('''-----------------------------------------------------------------------
  为了我们自己的类也可以使用with， 只要给这个类增加两个函数__enter__, __exit__即可：  
''')
with open("p.txt") as f:
    print(f.readline())

class A:
    def __enter__(self):
        print("in enter")
    def __exit__(self,type,value,trace):
        print("in exit")
with A() as a:
    print("in with")





















print('''-----------------------------------------------------------------------

紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。
当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法
The __enter__() function is executed
The value returned by it - in this case "Foo" is assigned to sample
The body of the block is executed, thereby printing the value of sample ie. "Foo"
The __exit__() function is called.

1. __enter__()方法被执行
2. __enter__()方法返回的值 - 这个例子中是"Foo"，赋值给变量'sample'
3. 执行代码块，打印变量"sample"的值为 "Foo"
4. __exit__()方法被调用
''')
class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"
    def __exit__(self,type,value,trace):
        print("In __exit__()")
def get_sample():
    return Sample()
with get_sample() as sample:
    print("sample:",sample)
    
print('''---------------------------------------------------------------------

实际上，在with后面的代码块抛出任何异常时，__exit__()方法被执行。
异常抛出时，与之关联的type，value和stack trace传给__exit__()方法，因此抛出的ZeroDivisionError异常被打印出来了。
开发库时，清理资源，关闭文件等等操作，都可以放在__exit__方法当中。
''')

class Sample1:
    def __enter__(self):
        return self
    def __exit__(self,type,value,trace):
        print("type:",type)
        print("value:",value)
        print("trace:",trace)
    def do_something(self):
        bar = 1/0
        return bar + 10
with Sample1() as sample:
    sample.do_something()





