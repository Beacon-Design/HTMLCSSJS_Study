#!/usr/bin/env python3
#coding:utf-8

# python3 version

import html
def escape_html(s):
    return html.escape(s, quote = True)

print(escape_html(''' <b>html</b> ' " '''))
