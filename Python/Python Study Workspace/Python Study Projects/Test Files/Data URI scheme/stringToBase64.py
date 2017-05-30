#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# this file present string to base64; base64 to string.

import base64

# string s
s = "http://www.baidu.com"          # http://www.baidu.com
print('s (string):\n' + s, '\n')


# string to bytes
sb = s.encode('ascii')              # b'http://www.baidu.com'
print('sb (string to bytes):\n', sb, '\n')

# bytes to byte base64
s64 = base64.b64encode(sb)  # b'aHR0cDovL3d3dy5iYWlkdS5jb20='
print('s64 (bytes to base64):\n', s64, '\n')

# byte base64 to bytes
tb = base64.b64decode(s64)  # b'http://www.baidu.com'
print('tb (base64 to bytes):\n', tb, '\n')

# bytes to string
ts = tb.decode('ascii')             # http://www.baidu.com
print('ts (bytes to string):\n' + ts, '\n\n')



# byte base64 to byte string
byteString = s64.decode('ascii')    # aHR0cDovL3d3dy5iYWlkdS5jb20=
print('byteString (bytes to byte string):\n' + byteString, '\n\n')


# string to Data URI Scheme data:,
sURId = 'data:,' + s                # data:,http://www.baidu.com 
print('string to Data URI Scheme data:, \n' + sURId, '\n')

# string to Data URI Scheme data:text/plain,
sURItextP = 'data:text/plain,' + s
print('string to Data URI Scheme data:text/plain, \n' + sURItextP, '\n')

# string to Data URI Scheme data:text/html,
sURItextH = 'data:text/html,' + s
print('string to Data URI Scheme data:text/html, \n' + sURItextH, '\n')

# string to  Data URI Scheme  data:text/html;base64,
sURItextH64 = 'data:text/html;base64,' + byteString      # data:text/html;base64,aHR0cDovL3d3dy5iYWlkdS5jb20=
print('string to Data URI Scheme data:text/html;base64, \n' + sURItextH64, '\n')


# image/png;base64 string to  Data URI Scheme  data:image/png;base64, 
imgB64 = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAkUlEQVQ4jWOUO87Q8J+RoZ6BDMD4n6GRUfYEw39yNMMAEyWaqW9AoUw9wyPz/3BswWfPwMDAwLBKcx9crFCmHrcB6KBPaQFpLkAHMuwKGDaiAxZCNhRKNzA8+fmAdBcga5JhVyDHgPsM/U8bCDkQfxj0P2nE63yCBjAwMDAU3UvAKz8ckjLjf4ZGcjUz/mdoBADXpy5umvCg6AAAAABJRU5ErkJggg==' 
sURIpng = 'data:image/png;base64,' + imgB64
print('string to Data URI Scheme data:image/png;base64, \n' + sURIpng, '\n')



