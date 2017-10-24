#!/usr/bin/env python3
#coding:utf-8

import os

filePath = "/Users/yulei/Documents/YL/Hub/HTMLCSSJS_imac/Test Field/py/renameFiles"


originalPath = os.getcwd()       # original working path
print("Default working path is " + originalPath)

os.chdir(filePath)      # change working dir
changePath = os.getcwd()
print("Change working dir is " + changePath)



file_list = os.listdir(filePath)
print(file_list)
realFile_list = file_list[1:]
print(realFile_list)

transTable = str.maketrans("ab", "XY", "123")
# change "a" to "X", "b" to "Y", del "1","2","3"

for file_name in realFile_list:
    os.rename(file_name,file_name.translate(transTable))

print("Current working dir is " + os.getcwd() )








