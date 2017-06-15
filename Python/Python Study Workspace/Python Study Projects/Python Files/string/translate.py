# !/user/bin/env python3
# coding:utf-8

S = "12345abcde!!!"

table = str.maketrans({"1":"A", "!":""})
print(S.translate(table))
