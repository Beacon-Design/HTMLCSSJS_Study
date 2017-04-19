# coding=utf-8

print('''======Parallel Iteration===============================================
------zip-----------------------------------------------------------------------
A useful tool for parallel iteration is the built-in function zip, 
which 'zips' together the sequences, returning a list of tuples

''')
name = ["anne","beth","tom","jay"]
age = [12,23,32,50]

for i in range(len(name)):
    print(name[i],age[i])

print(zip(name,age))
for name,age in zip(name,age):
    print(name,age)

print('''-----------------------------------------------------------------------
The zip function works with as many sequences as you want. It's important to 
note what zip does when the sequences are of different lengths: it stops when 
the shortest sequence is used up:
''')

zip(range(0,5),range(10,14))
for n1,n2 in zip(range(0,5),range(10,14)):
    print(n1,n2)

print('''======Numbered Iteration===============================================
------enumerate-----------------------------------------------------------------
This function lets you iterate over index-value pairs, where the indices 
are supplied automatically

''')
strings = "abcxdefxghix"

print(enumerate(strings))

for index, string in enumerate(strings):
    if "x" in string:
        print(index,strings[index]) 


print('''======Reversed and Sorted Iteration===============================================
''')
print(sorted([4, 3, 6, 8, 3]))
print(sorted("Hello, World!"))
print(list(reversed("Hello, World!")))
print("".join(reversed("Hello, World!")))















