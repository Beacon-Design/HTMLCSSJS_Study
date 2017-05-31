#!/usr/bin/env python3
#coding:utf-8

def intersect(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    print(res)
    return res

intersect([1, 2, 3], (1, 4))

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    print(res)
    return res

union("good", "book", "apple")