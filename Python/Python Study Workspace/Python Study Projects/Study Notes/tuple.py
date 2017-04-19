print("------tuple/string,immutable---------------------------------")
print(r'''
------sequence(in,not in expression)(index)(slice)-------

print(1,2,3) and print( (1,2,3) ) mean two different things 
- the former prints three numbers whereas the latter prints 
a tuple (which contains three numbers)


''')

zoo = ('python', 'elephant', 'penguin')
print(len(zoo))

new_zoo = 'monkey', 'camel', zoo
print(len(new_zoo))
print(new_zoo)
print(new_zoo[2])
print(new_zoo[2][2])
print(len(new_zoo)-1+len(new_zoo[2]))
print()

print('''
An empty tuple is constructed by an empty pair of parentheses 
such as myempty = (). However, a tuple with a single item is 
not so simple. You have to specify it using a comma following 
the first (and only) item so that Python can differentiate 
between a tuple and a pair of parentheses surrounding the 
object in an expression i.e. you have to specify 
singleton = (2 , ) if you mean you want a tuple containing the item 2.

''')

#empty tuple
myempty = ()
#a tuple containing the item 2
singleton = (2 , )