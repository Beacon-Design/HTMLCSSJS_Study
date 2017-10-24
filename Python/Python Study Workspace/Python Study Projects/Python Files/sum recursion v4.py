#!/usr/bin/env python3
#coding:utf-8

# it adds nested lists’ contents to the end of the list, forming a first-in-first-out queue.

def sumtree(L):                         # Breadth-first, explicit queue
    tot = 0
    items = list(L)                     # Start with copy of top level
    while items:
        front = items.pop(0)            # Fetch/delete front item
        if not isinstance(front, list):
            tot += front                # Add numbers directly
        else:
            items.extend(front)         # <== Append all in nested list
    return tot

print(sumtree([1, 2, 3, 4]))