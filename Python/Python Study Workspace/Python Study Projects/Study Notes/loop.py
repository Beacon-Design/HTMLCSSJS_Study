print("#01--------------------")
a="this is a string"
for i,k in enumerate(a):
    if k == "s":
        print("index {} is an s".format(i))
print("#02--------------------")

for i,k in enumerate(a):
    print(i,k)

print("#03--------------------")
for i in a:
    if i == "s":
        continue
    print(i,end="")


print()
print("#04--------------------")
for i in a:
    if i == "s":
        break
    print(i,end="")