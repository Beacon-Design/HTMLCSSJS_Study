#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num = input("number: ")
end = int(num)
total = 0
current = 1
while current <= end:
    total += current
    current += 1

print(total)