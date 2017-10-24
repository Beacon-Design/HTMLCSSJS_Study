
# -*- coding: utf-8 -*-
def power2(x, n):
    if not isinstance(x, (int, float)):
        raise TypeError('x must be a number')
    if not isinstance(n, (int, float)):
        raise TypeError('n must be a number')

    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


root = float(input('root of the number: '))
p = float(input('power of the number: '))
a = power2(root, p)
print("root is " + str(root))
print("p is " + str(p))
print(a)