print("The E notation indicates powers of 10. In this case")
print(2E4)
print(2*10**4)
print('''
NOTE:There is no separate long type. The int type can 
be an integer of any size.
''')

print(5/2,",",5/2.0,",",5/-2,",",5/-2.0)
print(5//2,",",5//2.0,",",5//-2,",",5//-2.0)
print(9/3,",",9.0/3,",",9//3,",",9//3.0)

print('''
------Hex, Octal, Binary: Literals and Conversions------------------------------
''')
print(oct(64),hex(64),bin(64))
print(int("64"),int("100",8),int("40",16),int("1000000",2))
print(int("0x40",16),int("0b1000000",2),"\n")

print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'),"\n")
# The eval function, which you'll meet later in this book, treats strings as though they
# were Python code. Therefore, it has a similar effect, but usually runs more slowly-it
# actually compiles and runs the string as a piece of a program, and it assumes the string
# being run comes from a trusted source-a clever user might be able to submit a string
# that deletes files on your machine, so be careful with this call

print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))
print('%o, %x, %x, %X' % (64, 64, 255, 255))