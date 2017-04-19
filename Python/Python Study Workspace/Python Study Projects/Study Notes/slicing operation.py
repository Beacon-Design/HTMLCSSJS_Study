print('''
Remember that if you want to make a copy of a list or 
such kinds of sequences or complex objects (not simple 
objects such as integers), then you have to use the 
slicing operation to make a copy. If you just assign 
the variable name to another name, both of them will 
''refer'' to the same object and this could be trouble 
if you are not careful.

''')
print('Simple Assignment')
print()

shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist 
del shoplist[0] 
print('shoplist is', shoplist)
print('mylist is', mylist)
print()

print('Copy by making a full slice')
mylist = shoplist[:] 
del mylist[0] 
print('shoplist is', shoplist)
print('mylist is', mylist)
print("-------------------------------------------------------------")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[::-1])
print(letters[:-3:-1])
print(letters[3:1:-1])
print(letters[-3:])
print(letters[2:7:2])
letters[0]='A'
print(letters[:])
letters[0:3]=[]
print(letters+['h','i','j','k'])
