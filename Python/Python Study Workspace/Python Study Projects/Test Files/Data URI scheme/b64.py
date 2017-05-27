#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# this file present string to base64; base64 to string.

import base64


s = "http://www.baidu.com"
print('s (string): ', s)


# string to bytes
sb = s.encode('ascii')
print('sb (string to bytes): ', sb)

# bytes to base64
s64 = base64.urlsafe_b64encode(sb)
print('s64 (bytes to base64): ', s64)

# base64 to bytes
tb = base64.urlsafe_b64decode(s64)
print('tb (base64 to bytes): ', tb)

# bytes to string
ts = tb.decode('ascii')
print('ts (bytes to string): ', ts)