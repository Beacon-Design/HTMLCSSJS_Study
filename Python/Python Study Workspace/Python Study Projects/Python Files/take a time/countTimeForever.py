#!/usr/bin/env python3
#coding:utf-8

import time
import webbrowser

total_break = 3
count = 0

print("Begin!")
while True :
    print(str(count) +"   " + time.ctime())
    time.sleep(1)
    count += 1

print("End!")

