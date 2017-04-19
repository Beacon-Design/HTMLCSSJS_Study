print("------01------------------------------------------")
if __name__ == "__main__":
    print("this program is being run by itself")
else:
    print("I am being imported from another modele")   
print()

print("------02--------------------------------------------")
import docstring
docstring.a()
print(docstring.a.__doc__)

print("------03--------------------------------------------")
if docstring == "__main__":
    print("this program is being run by itself")
else:
    print("I am being imported from another modele")
print()

print("------04---------------------------------------------")
from docstring import a
a()


print('''----------------------------------------------------------------------
------import------
import somemoudle

from somemodule import somefunction

from somemoudle import somefunction, anotherfunction, yetanotherfunction 

from somemoudle import * 
# only when you are certain that you want to import
# everything from the given module


--------------------------------------------------------------------------------
------as------


you can add an as clause to the end and supply the name you
want to use, either for the entire module or for the given function:

''')

import math as foobar
print(foobar.sqrt(4))

from math import sqrt as foo
print(foo(9))

































