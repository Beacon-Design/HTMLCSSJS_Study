print(r'''------mutable--------(not sequence)----------------------------------
----------------mapping type---(Mappings are not positionally ordered)----------------------------------
------ key-value pairs in a dictionary are not ordered -----------

Note that you can use only immutable objects (like strings) for 
the keys of a dictionary but you can use either immutable or 
mutable objects for the values of the dictionary. 

dict = {'ob1':'computer', 'ob2':'mouse', 'ob3':'printer'}
dict ={key:value} key,numbers/string

Values can be any type of variable (including lists or even 
dictionaries (those dictionaries or lists of course can contain 
dictionaries or lists themselves)


''')
print("------dict()------------------------------------------------------")
d={}
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4
print(d)
# d = {"a":1,"b":2,"c":3,"d":4}
bob1 = dict(name="Bob",job="Dev",age=40)
print(bob1)
bob2 = dict(zip(["name","job","age"],["Bob","Dev",40]))
print(bob2)
# {'age': 40, 'name': 'Bob', 'job': 'Dev'}
print()

for x in d.keys():
    print(x,end="")

print()
for k in d:
    print(k,d[k],end=" / ")
print()

for n in sorted(d.keys()):
    print(n,d[n],end=" / ")
print()

p=dict( six=6,seven=7,eight=8,nine=9)
print(p)

p["ten"]=10
print(p)
print()

d["five"]=5
print(d)

del d["c"]
print(d)
print()

for w,m in d.items():
    print("{} is {}".format(w,m))
    
print('''------index---(nesting revissited)---------------------------------------\n''')

rec = {"name":{"first":"Bob","last":"Smith"},
       "job":["Dev","Mgr"],
       "age":40}
print(rec["name"],"\n",
      rec["name"]["last"],"\n",
      rec["job"],"\n",
      rec["job"][0],"\n",)

rec["job"].append("Design")
print(rec)

