#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pngToDataURISchemeB64
import base64




# open and read binary img file data
rimg = open('n.png', 'rb')
rimgContent = rimg.readlines()
print(rimgContent, '\n')
print(type(rimgContent), '\n')


# convert list[bytes] to one byte
b = b''
for i in rimgContent:
    b = b + i 
    print(i, '\n')      # print img data in lines
print(b, '\n')          # print one byte (img data in one line) 



pngB64 = base64.b64encode(b)    # one byte to base64 byte
print(pngB64, '\n')

# notice the img formate png,jpg...
bURIpng = b'data:image/png;base64,' + pngB64    # base64 byte to Data URI Scheme byte
print(bURIpng, '\n')

sURIpng = bURIpng.decode('ascii')   # Data URI Scheme byte to string
print(sURIpng)
