#!/usr/bin/env python3
#coding:utf-8


# To emulate the traversal of the recursive call version more closely, we can change it to perform depth-first traversal simply by adding the content of nested lists to the front of the list, forming a last-in-first-out stack:

def sumtree(L):                         # Depth-first, explicit stack
    tot = 0
    items = list(L)                     # Start with copy of top level
    while items:
        front = items.pop(0)            # Fetch/delete front item
        if not isinstance(front, list):
            tot += front                # Add numbers directly
        else:
            items[:0] = front           # <== Prepend all in nested list
    return tot

print(sumtree([1, 2, 3, 4]))