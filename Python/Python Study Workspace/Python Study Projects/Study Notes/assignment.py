print('''------sequence unpacking-------------------------------------------''')
x,y,z = 1,2,3
print(x,y,z)
x, y = y, x
print(x,y)
values = 1,2,3
print(values)
x,y,z = values
print(x,"\n\n")

dict1 = {"name":'Robin',"girl":'May'}
key,value = dict1.popitem()
print(key,value)

print('''------chained assignmennt------------------------------------------
x = y = function()
which is the same as
y = function()
x = y
    Note that the preceding statements may not be the same as
x = somefunction()
y = somefunction() 







''')







