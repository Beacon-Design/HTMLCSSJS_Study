print('''------ unordered collections of simple objects-------
------ immutable -----------------------------------------------
sets can only contain immutable (a.k.a. "hashable") object types. 
Hence, lists and dictionaries cannot be embedded in sets.
Sets themselves are mutable.
!!! items are stored only once in a set !!!

''')
print(set([1,2,3,4,]),"# Built-in call(all)")
print({1,2,3,4,},"# set literals(2.7,3.x) \n")

s1 = {1,2,3,4}
s2 = {3,5,6}
print(s1 & {1,3},"# Intersection")
print(s1 | {10,11},"# Union")
print(s1 - {1,2,3},"# Difference")
print(s1 > {1,3},"# Superset")
print(s1 - {1,3,2,4},"# Empty set")
print(s1 ^ s2,),"# who is in one but not both"
print(type({}),"\n")

s = set()
s.add(1.23)
s.add((2,3,1))
print(s)
print({1,2,3}.union([5,4]))
print({1,2,3}.union({5,4}))
print({1,2,3}.union(set([5,4])))
print({1,2,3}.intersection((1,3,5)))
print({1,2,3}.issubset(range(1,4)),"\n")
print('''
# Tuples in a set, for instance, might be used to represent dates, records, IP addresses,
and so on (more on tuples later in this part of the book). Sets may also contain modules,
type objects, and more. Sets themselves are mutable too, and so cannot be nested in
other sets directly; if you need to store a set inside another set, the frozenset built-in
call works just like set but creates an immutable set that cannot change and thus can
be embedded in other sets


''')





print("----------------------------------------------------------")
bri = set(["brazil","russia","india"])
print(bool("india" in bri))
print(bool("usa" in bri),"\n")

bric = bri.copy()
bric.add("china")
print(bric.issuperset(bri),"\n")

bri.remove("russia")
print(bri & bric,"\n")

print(list(set([1,2,1,3,1])))
print(set("spam")-set("ham"))
print(set("spm") == set("mps"))

print("------set comprehensions--------------------------------")
x = {n**2 for n in [1,2,3,4]}
print(x,"\n")

print("------ filter duplicates ---------------------------------------------------")
L = [1, 2, 1, 3, 2, 4, 5]
print(L)
print(set(L)) 
L1 = list(set(L))
print(L1,"\n")

print("------isolate differences in lists, strings, and other iterable objects---------")
print(set([3,5,7,1])-set([1,2,4,5,6]))
print(bool(set("box") == set("xbo")))



