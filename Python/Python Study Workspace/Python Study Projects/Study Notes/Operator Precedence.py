print('''
_______________________________________________________________

Associativity            Operators                  Description
left to right            lambda                     Lambda Expression
left to right            or                         Boolean
left to right            and                        Boolean
left to right            not                        Boolean 
right to left            in,not in,is,is not,       Comparisons
                         <,<=,>,>=,!=,==
left to right            |                          Bitwise
left to right            ^                          Bitwise
left to right            &                          Bitwise
---------------------------------------------------------------
left to right            <<,>>                      Bitwise
left to right            +,-                        Addition and subtraction
left to right            *,/,//,%                   Multiplication,division,remainder
N/A                      +x,-x,~x                   Unary arithmetic
left to right            **                         Exponentiation   
right to left            x[slice],x(arguments...),  Slice,function call,and 
                         x.attribute                attribute reference
left to right            (expression...),           Binding,tuple,list,
                         [expression...],           dictionary
                         {key:value}
________________________________________________________________
                         

''')

print('''
** (power)
Returns x to the power of y
3 ** 4 gives 81 (i.e. 3 * 3 * 3 * 3)

// (floor division)
Returns the floor of the quotient
13 // 3 gives 4.

% (modulo)
Returns the remainder of the division
13 % 3 gives 1. -25.5 % 2.25 gives 1.5.

<< (left shift)
Shifts the bits of the number to the left by the number of bits specified. 
(Each number is represented in memory by bits or binary digits i.e. 0 and 1)
2 << 2 gives 8. 2 is represented by 10 in bits.
Left shifting by 2 bits gives 1000 which represents the decimal 8.

>> (right shift)
Shifts the bits of the number to the right by the number of bits specified.
11 >> 1 gives 5.
11 is represented in bits by 1011 which when right shifted by 1 bit gives 
101`which is the decimal `5.

& (bit-wise AND)
Bit-wise AND of the numbers
5 & 3 gives 1.

| (bit-wise OR)
Bitwise OR of the numbers
5 | 3 gives 7

^ (bit-wise XOR)
Bitwise XOR of the numbers
5 ^ 3 gives 6

~ (bit-wise invert)
The bit-wise inversion of x is -(x+1)
~5 gives -6. More details at 

not (boolean NOT)
If x is True, it returns False. If x is False, it returns True.
x = True; not x returns False.

and (boolean AND)
x and y returns False if x is False, else it returns evaluation of y
x = False; y = True; x and y returns False since x is False. In this case, 
Python will not evaluate y since it knows that the left hand side of the and 
expression is False which implies that the whole expression will be False 
irrespective of the other values. This is called short-circuit evaluation.

or (boolean OR)
If x is True, it returns True, else it returns evaluation of y
x = True; y = False; x or y returns True. Short-circuit evaluation applies here as well.


''')


print('''------Python expression operators and precedence------------------------------------
Operators                            Description

yield x                              Generator function send protocol
lambda args: expression              Anonymous function generation
x if y else z                        Ternary selection (x is evaluated only if y is true)
x or y                               Logical OR (y is evaluated only if x is false)
x and y                              Logical AND (y is evaluated only if x is true)
not x                                Logical negation
x in y, x not in y                   Membership (iterables, sets)
x is y, x is not y                   Object identity tests
x < y, x <= y, x > y, x >= y         Magnitude comparison, set subset and superset;
x == y, x != y                       Value equality operators
x | y                                Bitwise OR, set union
x ^ y                                Bitwise XOR, set symmetric difference
x & y                                Bitwise AND, set intersection
x << y, x >> y                       Shift x left or right by y bits
x + y                                Addition, concatenation;
x – y                                Subtraction, set difference
x * y                                Multiplication, repetition;
x % y                                Remainder, format;
x / y, x // y                        Division: true and floor
−x, +x                               Negation, identity
~x                                   Bitwise NOT (inversion)
x ** y                               Power (exponentiation)
x[i]                                 Indexing (sequence, mapping, others)
x[i:j:k]                             Slicing
x(...)                               Call (function, method, class, other callable)
x.attr                               Attribute reference
(...)                                Tuple, expression, generator expression
[...]                                List, list comprehension
{...}                                Dictionary, set, set and dictionary comprehensions

(# ------ In Python 2.X, value inequality can be written as either X != Y or X <> Y. In Python
3.X, the latter of these options is removed because it is redundant. In either version,
best practice is to use X != Y for all value inequality tests.)

(# ------ The X // Y floor division expression always truncates fractional remainders in both
Python 2.X and 3.X. The X / Y expression performs true division in 3.X (retaining
remainders) and classic division in 2.X (truncating for integers).)

(# ------ In Python 2.X, a backquotes expression 'X' works the same as repr(X) and converts
objects to display strings. Due to its obscurity, this expression is removed in Python
3.X; use the more readable str and repr built-in functions, described in "Numeric
Display Formats.")

(# ------ the slice expression X[I:J:K] is equivalent to indexing with a
slice object: X[slice(I, J, K)].)

(# ------ Comparison operators may be chained: X < Y < Z produces the same result as X <
Y and Y < Z.)

(# ------ In Python 2.X, magnitude comparisons of mixed types are allowed, and convert
numbers to a common type, and order other mixed types according to type names.
In Python 3.X, nonnumeric mixed-type magnitude comparisons are not allowed
and raise exceptions; this includes sorts by proxy)

(# ------ Magnitude comparisons for dictionaries are also no longer supported in Python
3.X (though equality tests are); comparing sorted(aDict.items()) is one possible
replacement)





''')