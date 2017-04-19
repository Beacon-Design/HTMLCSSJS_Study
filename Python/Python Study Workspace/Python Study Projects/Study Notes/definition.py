#coding=utf-8

print('''------Python Keywords----------------------------------------------------
and, as, assert, break, class, continue, def, del, elif, else, except, finally, 
for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, 
return, try, while, with, yield

''')


print('''----------------------------------------------------------------------
a '#' (octothorpe) character 
An "octothorpe" is also called a "pound", "hash", "mesh", or any number of names.
''')

print('''------Python Internals-------------------------------------------------
Most probably you will have read somewhere, that the Python language is an 
interpreted programming or script language. The truth is: Python is both an 
interpreted and a compiled language. But calling Python a compiled language 
would be misleading. People would assume that the compiler translates the 
Python code into machine language. Python code is translated into intermediate 
code, which has to be executed by a virtual machine, known as the PVM, the 
Python virtual machine. This is a similar approach to the one taken by Java. 
There is even a way of translating Python programs into Java byte code for 
the Java Virtual Machine (JVM). This can be achieved with Jython.

Source Code -> Byte Code -> Virtual Machine PVM
Every time a Python script is executed, byte code is created. But only, if a 
Python program is imported as a module, the byte code will be stored in the 
corresponding .pyc file. 


------ Compiler ----------------------------------------------------------------
Definition: A compiler is a computer program that transforms (translates) source 
code of a programming language (the source language) into another computer 
language (the target language). In most cases compilers are used to transform 
source code into executable program, i.e. they translate code from high-level 
programming languages into low (or lower) level languages, mostly assembly or 
machine code.


------ Interpreter -------------------------------------------------------------
Definition: An interpreter is a computer program that executes instructions 
written in a programming language. It can either

execute the source code directly or
translates the source code in a first step into a more efficient representation 
and executes this code

''')

print('''\
------The Colon------

You may have noticed that we always place a colon at the end of if, else, 
while, and def statements. The colon marks the end of the statement, and 
tells us that the next line should be the beginning of a new block.

''')


print('''------number/tuple/string, immutable------------------

An “immutable” object is an object that cannot be changed after it is created.
Numbers, strings, and tuples in Python fall into this category. While you cannot
Test Your Knowledge: Answers | 131
change an immutable object in place, you can always make a new one by running
an expression. Bytearrays in recent Pythons offer mutability for text, but they are
not normal strings, and only apply directly to text if it’s a simple 8-bit kind
''')
print("list/dictionary/set, mutable")
print(r'''
print(1,2,3) and print( (1,2,3) ) mean two different things 
- the former prints three numbers whereas the latter prints 
a tuple (which contains three numbers)


''')

print('------------------------------------------------------------')
print('#01');n=2;print(n)
print("------------------------------------------------------------")

print('''------reference---------------------------------------------

Python variables are always pointers to objects, 
not labels of changeable memory areas

there is no way to ever link a variable to another variable in Python. 
Rather, both variables point to the same object via their references.


When you create an object and assign it to a variable, the variable 
only refers to the object and does not represent the object itself.
the variable name points to that part of your computer's memory where
the object is stored.
''')
L1 = [2,3,4]
L2 = L1
print("L1:",L1," , ","L2:",L2)
L1 = 24
print("L1:",L1," , ","L2:",L2,"\n")

N1 = [2,3,4]
N2 = N1
N1[0] = 24
print("L1:",L1," , ","L2:",L2,"\n")
# we haven’t changed L1 itself here; we’ve changed a component of the object that
# L1 references. This sort of change overwrites part of the list object’s value in place
# This behavior only occurs for mutable objects that support in-place changes





print('''------Shared References and Equality--------------------------------------
if both names point to the exact same object
''')
X = [1,2,3]
Y = X
print(bool(X == Y))
print(bool(X is Y),"\n")
# X,Y reference the same object,same values,same objects.

X = [1,2,3]
Y = [1,2,3]
print(bool(X == Y))
print(bool(X is Y),"\n")
# X,Y reference the different object,same values,different objects.







print('''
make a copy of a list or such kinds of sequences or complex objects 
(not simple objects such as integers), then you have to use the 
slicing operation to make a copy. If you just assign the variable 
name to another name, both of them will 'refer' to the same object

\n''')

print('''
Taking the slice [:] creates a new copy of the list. However it only 
copies the outer list. Any sublist inside is still a references to 
the sublist in the original list. Therefore, when the list contains 
lists, the inner lists have to be copied as well. You could do that 
manually but Python already contains a module to do it. You use the 
deepcopy function of the copy module

\n''')

import copy

a = [[1,2,3],[4,5,6]]
b = a[:]
c = copy.deepcopy(a)
b[0][1] = 10
c[0][1] = 12
print(a)
print(b)
print(c)

print('''
***only have to worry about references when using dictionaries and lists. 
Numbers and strings create references when assigned but every operation 
on numbers and strings that modifies them creates a new copy so you can 
never modify them unexpectedly. You do have to think about references 
when you are modifying a list or a dictionary***


''')

print('''------(memory space)_(Python’s garbage collection)----------------------------------------------------
Just as importantly, in a lower-level language we would have to be careful 
to clean up all of the object  space when we no longer need it. In Python, 
when we lose the last reference to the object y assigning its variable to 
something else, for example all of the memory space occupied by that 
object structure is automatically cleaned up for us.
Python will clean up unused space for you as your program runs.

''')

print('''
------Method-------------------------------------------------------------
Methods are functions associated with values of that data type. For 
example, string methods are functions that can be called on any string

''')

print('''------sequence-------------------------------------------------
A "sequence" is a positionally ordered collection of objects. Strings, lists, and tuples
are all sequences in Python. They share common sequence operations, such as
indexing, concatenation, and slicing, but also have type-specific method calls. A
related term, "iterable," means either a physical sequence, or a virtual one that
produces its items on request.

''')

print('''------mapping------------------------------------------------------
The term "mapping" denotes an object that maps keys to associated values.
Python's dictionary is the only mapping type in the core type set. Mappings do not
maintain any left-to-right positional ordering; they support access to data stored
by key, plus type-specific method calls

''')

print('''------polymorphism--------------------------------------------------------
"Polymorphism" means that the meaning of an operation (like a +) depends on the
objects being operated on. This turns out to be a key idea (perhaps the key idea)
behind using Python well-not constraining code to specific types makes that code
automatically applicable to many types


''')

print('''-----------------------------------------------------------------------
------object-oriented programming-----------------------------------------------

In object-oriented programming, the term object loosely means a collection of data (attributes)
with a set of methods for accessing and manipulating those data.ome of the most important
benefits of objects include the following:

------

Polymorphism: You can use the same operations on objects of different classes, and
they will work as if "by magic."

Encapsulation: You hide unimportant details of how objects work from the outside
world.

Inheritance: You can create specialized classes of objects from general ones.

------

Some Thoughts on Object-Oriented Design

• Gather what belongs together. If a function manipulates a global variable, the two of
them might be better off in a class, as an attribute and a method.
• Don’t let objects become too intimate. Methods should mainly be concerned with the
attributes of their own instance. Let other instances manage their own state.
• Go easy on the inheritance, especially multiple inheritance. Inheritance is useful at
times, but can make things unnecessarily complex in some cases. And multiple inheritance
can be very difficult to get right and even harder to debug.
• Keep it simple. Keep your methods small. As a rule of thumb, it should be possible to
read (and understand) most of your methods in, say, 30 seconds. For the rest, try to keep
them shorter than one page or screen.

When determining which classes you need and which methods they should have, you may
try something like this:
1. Write down a description of your problem (what should the program do?). Underline all
the nouns, verbs, and adjectives.
2. Go through the nouns, looking for potential classes.
3. Go through the verbs, looking for potential methods.
4. Go through the adjectives, looking for potential attributes.
5. Allocate methods and attributes to your classes.
Now you have a first sketch of an object-oriented model. You may also want to think about
what responsibilities and relationships (such as inheritance or cooperation) the classes and
objects will have. To refine your model, you can do the following:
1. Write down (or dream up) a set of use cases—scenarios of how your program may be
used. Try to cover all the functionality.
2. Think through every use case step by step, making sure that everything you need is
covered by your model. If something is missing, add it. If something isn’t quite right,
change it. Continue until you are satisfied.



''')

