#!/usr/bin/env python3
#coding:utf-8


def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])      # Call myself recursively

mysum([1, 2, 3, 4, 5])




