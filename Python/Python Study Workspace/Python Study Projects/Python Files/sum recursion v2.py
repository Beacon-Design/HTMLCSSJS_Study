#!/usr/bin/env python3
#coding:utf-8

def mysum(L):
    if not L: return 0
    return nonempty(L)

def nonempty(L):
    return L[0] + mysum(L[1:])


print(mysum([1.1, 2.2, 3.3, 4.4]))