#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import base64

fb64 = open('filebase64.txt', 'wb')
rimg = open('star.png', 'rb')
content = rimg.readlines()
print(content)
print(type(content))

for i in content:
    print(i)