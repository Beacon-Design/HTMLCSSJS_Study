#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, y=i: y ** x)
    return acts


acts = makeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))

# The following is an equivalent of the prior example
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts


acts = makeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))
