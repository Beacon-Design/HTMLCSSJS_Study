print("------packages------")
print('''
Packages are just folders of modules with a 
special __init__.py file that indicates to Python 
that this folder is special because it contains Python modules.


Let's say you want to create a package called 'world' 
with subpackages 'asia', 'africa', etc. and these 
subpackages in turn contain modules like 'india', 
'madagascar', etc.

This is how you would structure the folders:

- <some folder present in the sys.path>/
    - world/
        - __init__.py
        - asia/
            - __init__.py
            - india/
                - __init__.py
                - foo.py
        - africa/
            - __init__.py
            - madagascar/
                - __init__.py
                - bar.py


''')