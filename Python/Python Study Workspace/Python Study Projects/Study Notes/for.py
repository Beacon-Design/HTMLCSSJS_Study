print('''------The for loop----------------------------------------- 
The for..in statement is another looping statement which 
iterates over a sequence of objects i.e. go through each 
item in a sequence
 
Remember that the else part is optional. When included, 
it is always executed once after the for loop is over 
unless a break statement is encountered. 

''')
for x in range(1, 5):
    print(x)
else:
    print('The for loop is over')

print('___________________________________________________________')
print()

print("#01--------------------")
a="this is a string"
for i,k in enumerate(a):
    if k == "s":
        print("index {} is an s".format(i))
print("#02--------------------")

for i,k in enumerate(a):
    print(i,k)
print()

print('''======= else ==============================================================
You can use continue, break, and else clauses with both for loops and
while loops.
''')
import math
for n in range(99,90,-1):
    root = math.sqrt(n)
    print(n)
    if root == int(root):
        print(n,root)
        break
else:
    print("not find it")

