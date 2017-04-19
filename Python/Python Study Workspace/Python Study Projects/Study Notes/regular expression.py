# coding=utf-8
print(r"""------正则表达式运算符的优先级顺序---------------------------------
\                                         转义笄1�7
(), (?:), (?=), []                        括号和中括号
*, +, ?, {n}, {n,}, {n,m}                 限定笄1�7
^, $, \任何元字符�1�7�任何字笄1�7                  定位点和序列
|                                         替换
""")



import re
a =re.compile(r'''a
                sd''',re.X)
print("------re.match---------------------------------------------------")

c = re.match(a,"asd lik")
d = a.match("asd lik")

print(c)
print(d)
print(d.group(),d.start(),d.end(),d.span(),"\n")

print("------re.findall-------------------------------------------------")
m = re.findall(a,"asd lik")
n = a.findall("asd lik")
print(m)
print(n)

print("------(?:...)----------------------------------------------------")
p = re.compile(r".?\.(?:jpg|png|gif)")
k = "asdq.gif"
print(re.findall(p,k))

print("------ .sub()----------------------------------------------------")
a = re.compile(r"book")
b = '''hi book name'''
c = re.sub(a,"your",b)
print(c)