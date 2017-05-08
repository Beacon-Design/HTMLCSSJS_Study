#!usr/bin/evn python3
# coding:utf-8

# 1. load a file’s contents into a string all at once
def loadAllAtOnce():
    file = open('file.txt', 'r')    # Read contents into a string
    print(file.read())
loadAllAtOnce()


# 2. load a file in smaller pieces while
def smallW():
    file = open('file.txt')
    while True:
        char = file.read(1)     # Read by character
        if not char:            # Empty string means end-of-file
            break
        print(char)
print('load a file in smaller pieces: While\n')
smallW()


# 3. load a file in smaller pieces for
def smallF():
    for char in open('file.txt').read():
        print(char)
print('load a file in smaller pieces: for\n')
smallF()


# 4. To read by lines while
def lineWhile():
    file = open('file.txt')
    while True:
        line = file.readline()      # Read line by line
        if not line:
            break
        print(line.rstrip())        # Line already has a \n
print('To read by lines or blocks while01\n')
lineWhile()


# 5. To read binary data in blocks while
def blockWhile():
    file = open('file.txt', 'rb')
    while True:
        chunk = file.read(10)
        if not chunk:
            break
        print(chunk)
print('To read by lines or blocks while02\n')
blockWhile()


# 6. read text files line by line
def lineFor01():
    for line in open('file.txt').readlines():
        print(line.rstrip())
print('read text files line by line: lineFor01\n')
lineFor01()


# 7. read text files line by line
def lineFor02():
    for line in open('file.txt'):
        print(line.rstrip())
print('read text files line by line: linrFor02\n')
lineFor02()

