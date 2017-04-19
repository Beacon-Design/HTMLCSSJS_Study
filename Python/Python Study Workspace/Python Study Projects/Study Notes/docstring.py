
# Note that DocStrings also apply to modules and classes
# 
# The convention followed for a docstring is a multi-line string where the 
# first line starts with a capital letter and ends with a dot. Then the 
# second line is blank followed by any detailed explanation starting from 
# the third line. You are strongly advised to follow this convention for 
# all your docstrings for all your non-trivial functions.



def a():
    '''
This is __doc__ comment.

Three lines total.'''
# comment content
    print("file name = docstring,founction a")

print(a.__doc__)