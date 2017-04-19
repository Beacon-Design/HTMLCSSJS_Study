print('''
------mutable------
------sequence(in,not in expression)(index)(slice)-------

A list is a data structure that holds an ordered collection of 
items i.e. you can store a sequence of items in a list

''')
print("--- 01 ---.append/ .sort/ .remove--------------------------------------------")
print()
shoplist = ['apple', 'mango', 'carrot', 'banana']

print(len(shoplist))
print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')
print()

print('\nI also have to buy rice.')
shoplist.append('rice')  
print('My shopping list is now', shoplist)
print()

shoplist.sort() # alphabetical
print('Sorted shopping list is', shoplist)
print()

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
print()

shoplist[1:1]=["EGG"]
print(shoplist)
shoplist.remove("carrot")
print(shoplist)
#  L.remove(value) -> None -- remove first occurrence of value.
#    Raises ValueError if the value is not present.
print(shoplist[-1])
print()

print("--- 02 --- range()/ .pop-------------------------------------------\n")

print([0]*5)

a = list(range(10,20))
print(a)
a1 = [[x**2,x**3] for x in range(4)]
print(a1)

b = a.pop(2)
print(b)
print(a,"\n")
# L.pop([index]) -> item -- remove and return item at index (default last).
#   Raises IndexError if list is empty or index is out of range.
print('''------### list comprehensions ###--------------------------------\n''')
print([x*x for x in range(5)])
print([x*x for x in range(5) if x%3 == 0])
print([(x, y) for x in range(3) for y in range(3)])
result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result,"\n\n")


girls = ["alice","bernice","clarice"]
boys = ["chris","arnold","bob"]
print([b+"+"+g for b in boys for g in girls if b[0] == g[0]])
print("a better solution")
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print([b + "+" + g for b in boys for g in letterGirls[b[0]]],"\n\n")


m = [[1,3,9],[4,0,6],[7,3,5]]
row1 = [row[1] for row in m]
print(row1)
# for row in m:
#     print(row[1])
row2 = [row[1]+1 for row in m]
print(row2)
row3 = [row[0] for row in m if row[0] % 2 == 0]
print(row3,"\n")

g = (sum(row) for row in m )
print(next(g),next(g),next(g))
# next(iterator[, default])
# Return the next item from the iterator. If default is given and the iterator
# is exhausted, it is returned instead of raising StopIteration.
print(list(map(sum,m)))
# map(func, *iterables) --> map object 
# Make an iterator that computes the function using arguments from
# each of the iterables.  Stops when the shortest iterable is exhausted.
print({i:sum(m[i]) for i in range(3)},"\n")

diag = [m[i][i] for i in [0,1,2]]
print(diag)
doubles = [c*2 for c in "box"]
print(doubles,"\n")


print('''------ lists, sets, dictionaries, and generators ---------------------------
------ can all be built with comprehensions ---------------------------- \n''')
# ord(c) -> integer
# Return the integer ordinal of a one-character string.    
print(
[ord(x) for x in "book"],
" __List of character ordinals\n",

{ord(x) for x in "book"},
" __Sets remove duplicates\n",

{x:ord(x) for x in "book"},
" __Doctionary\n",

(ord(x) for x in "book"),
" __Generator of values"
)

print('''
------ format -------------------------------------------------------------
''') 

print("------# 01------")   
# by position
template = '{0},{1} and {2}'
print(template.format('spam','ham','eggs'))

# by keyword
template = '{motto},{pork} and {food}'
print(template.format(motto='spam',pork='ham',food='eggs'))

#by both
template = '{motto},{0} and {food}'
print(template.format('ham',motto='spam',food='eggs'))

#by relative position
template = '{},{} and {}'
print(template.format('spam','ham','eggs'))

#via expression
template = '%s,%s and %s'
print(template %('spam','ham','eggs'))

template = '%(motto)s,%(pork)s and %(food)s'
print(template % dict(motto='spam',pork='ham',food='eggs'))

print("------# 02------")
import sys
print('My {1[kind]} runs {0.platform}'.format(sys,{'kind':'laptop'}))

print('My {map[kind]} runs {sys.platform}'.format(sys=sys,map={'kind':'laptop'}))

print("------# 03------")

somelist = list('SPAM')
print(somelist)

print("first={0[0]}, third={0[2]}".format(somelist))

print("first={0}, last={1}".format(somelist[0],somelist[-1]))

parts = somelist[0], somelist[-1], somelist[1:3]
print('first={0}, last={1}, middle={2}'.format(*parts))








