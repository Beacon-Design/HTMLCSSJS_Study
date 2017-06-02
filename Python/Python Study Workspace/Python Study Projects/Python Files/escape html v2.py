#!/usr/bin/env python3
#coding:utf-8

# python2 version

import cgi
def escape_html(s):
    return cgi.escape(s, quote = True)

print(escape_html(''' <b>html</b> ' " '''))
