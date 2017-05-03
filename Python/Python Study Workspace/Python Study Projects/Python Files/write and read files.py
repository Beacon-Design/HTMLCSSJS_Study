#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Terminal run the file:
# python write\ and\ read\ files.py

# write file
fw = open("file.txt", "w")		
fw.write("Python write a file.\n")
fw.write("Write Done.")
fw.close()

print("Write Done!")	# Terminal print "Done"
print("\n")

# read file
fr = open("file.txt", "r")
text = fr.read()
print("Read file:")
print(text)
print("\n")	
fr.close()