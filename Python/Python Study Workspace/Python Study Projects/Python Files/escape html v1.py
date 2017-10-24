#!/usr/bin/env python3
#coding:utf-8

def escape_html(s):
    for (i, o) in (("&", "&amp;"),
                   (">", "&gt;"),
                   ("<", "lt;"),
                   ('"', "&quot;")):
        s = s.replace(i, o)
        # print(i, o)
    return s
print(escape_html("<b>html</b>"))
