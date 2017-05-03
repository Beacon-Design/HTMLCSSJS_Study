#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# b = dir(type)

a = str(help(type))

fw = open('type.txt', 'w')
for i in a:
    fw.write(i+'\n')
print ('done')






