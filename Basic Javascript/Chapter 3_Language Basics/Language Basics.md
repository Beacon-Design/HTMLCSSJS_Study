[TOC]



##Syntax

###<u>Case-sensitivity</u>

> everything is case-sensititive,variables,function names and operators.

### <u>Identifiers</u>

An identifier is the name of a variable, function, property, or function argument, Identifiers may be one or more characters in following format:

> 1. The first character must be a letter, an underscore(_), or a dollar sign($).
> 2. All other characters may be letters, underscores, dollar signs, or numbers.
> 3. may include extended ASCII or Unicode letter characters such as À and Æ

identifiers use camel case, like`myCar`.

(*Keywords, reserved words, true, false, and null cannot be used as identiﬁers.*)

### <u>Comments</u>

```JavaScript
//single line comment
```

```JavaScript
/*
   This is a multi-line 
   Comment
 */
```

### <u>Strict Mode</u>

enable strict at the top

```
"use strict";
```

function to execute in strict mode

```
function doSomething(){
  "use strict";
  //function body
}
```

### <u>Statement</u>

Statements are terminate  by a semicolon

```
var sum = a + b		//valid - not recommended
var diff = a - b;	//valid - preferred
```

*omitting the semicolon makes the  parser determine where the end of a statement occurs.*



------







## Keywords and Reserved Words



------







## Variables

a variable can hold any type of data, is a named placeholder for a value.

**Define a variable:**

```
var message;
// Without initialization, it holds the special value "undefined"
```

**Variable initialization**

```
var message = "hi";
message = 100;	//legal, but not recommended

// It is simply the assignment of a value to the variable .
// still not only change the value, but also change the type of value.
```



1. using the var operator to define a variable makes it local to the scope in which it was defined.

```
function test(){
  var message = "hi";	//local variable
}
test();
alert(message);		//error!

// the variable is destroyed as soon as the function exits.
```



2. possible to define a variable globally by omitting the var operator

```
function test(){
  message = "hi";	//global variable, but not recommended
}
test();
alert(message);		//"hi"

// the variable is defined and becomes accessible outside of the function once it has been executed.
```



3. define variables

```
var message = "hi",
	found = false,
	age = 29;
```



------







## Values

Inside the computer, there is only data. All this data is stored as long sequences of bits. 

**Bits** are any kind of **two-valued things**, as zeros and ones.Inside the computer, they take forms such as a high or low electrical charge, a strong or weak signal, a shiny or dull sport on the surface of a CD. Any piece of disvrete information can be reduced to a sequence of zeros and ones thus represented in bits.

The number 13 in bits, the weight of each increases by a factor of 2 from right to left. 

|    0 |    0 |    0 |    0 |    1 |    1 |    0 |    1 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|  128 |   64 |   32 |   16 |    8 |    4 |    2 |    1 |

the binary number 00001101, or 8+4+1, which equals 13.



------







## Data Types

Undefined, Null, Boolean, Number, String, Object.

1. *functions are considered **Object**s and don't represent another data type*
2. *null is considered to be an empty **Object** reference*



### <u>The typeof Operator</u>

Using the **typeof** operati on a value returns one of the following strings: 

> "undefined" if the value is undefined
>
> "boollean" if the value is a Boolean
>
> "string" if the value is a string
>
> "number" if the value is a number
>
> "object" if the value is an object(other than a function) or null
>
> "function" if the value is a function

```
var message = "some string";
alert(typeof message);		//"string"
alert(tyoeof (message));	//"string"
alert(typeof 95);			//"number"
```



### <u>The Undefined Type</u>

The Underfined type has only one special value **undefined**. When a variable is declared using **var** but not initialised, it is assigned the value of  **undefined** .

```
var message;
alert(message == undefined);	//true
```

> _use "undefined" to compare difference between an empty object pointer (null) and an uninitialised value_

```
var message;	//this variable is declared but has a value of undefined
alert(message);	//"undefined"
alert(age);		//causes an error
```



call on an ***uninitialised variable*** returns "undefined"

call on an ***undeclared variable*** returns "undefined"

```
var message;	//variable is declared, has a value of undefined
alert(typeof message);	//"undefined"
alert(typeof age);		//"undefined" , variable isn't declared
```

> 1. Uninitialized variables are automatically assigned a value of **undefined**.
>
>
> 2. It is advisiable to **always initialise variables**. That way,
>
>
> 3. When **typeof** returns"**undefined**" ,because a given variable has **not been declared** rather than was simply **not initialized**.



### <u>The Null Type</u>

The Null type has only one special value **null**.

**A null value is an empty object pointer.**

> var car = null;
>
> alert(typeof car);		//"object"



**When defining a variable that is meant to later hold an object, it is advisable to initialise the variable to null.** That way, you can explicitly check for the value null to determine if the variable has been filled with an object reference at a later time.

```
if (car != null){
  	//do domething with car
}
alert(null == undefined);	//true
//the value underfined is a derivative of null
```



### <u>The Boolean Type</u>

The Boolean type has only two literal values: **true** and **false** .

(true is not equal  to 1, false in not equal to 0)

The Boolean literals **true** and **false** are **case-sensitive**

```
var found = true;
var lost = false;

var message = "hello";
var messageAsBoolean = Boolean(message);
//the Boolean() casting function can be called on any type of data and will always return a Boolean value.
```



**It's important to understand what variable you're using in a flow control statement because of this  automatic conversion.**

| DATA TYPE | VALUES CONVERTED TO TRUE               | VALUES CONVERTED TO FALSE |
| :-------- | :------------------------------------- | :------------------------ |
| Boolean   | true                                   | false                     |
| String    | Any nonempty string                    | " "(empty string)         |
| Number    | Any nonzero number(including infinity) | 0, NaN                    |
| Object    | Any object                             | null                      |
| Undefined | n/a(not applicable)                    | undefined                 |



### <u>The Number Type</u>

JavaScript uses a fixed number of bits, namely 64 of them. given 64 binary digits represent 2 power 64 different numbers(an 18 with 18 zeros after it)

The Number Type represent both integers and floating-point values(called double-precision values in some languages). There are several different number literal formats.

#### 1. Integer

**A decimal integer:**

```
var intNum = 55;	//integer
```



Integers can be represented as either octal (base 8) or hexadecimal (base 16) literals.

**Octal literal**

An octal literal, the first digit must be a zero(0) followed by a sequence of octal digits(0~7). If a number out of this range, the leading zero is ignored and the number is treated as a decimal.

```
var octalNum1 = 070;	//octal for 56
var octalNum2 = 079;	//invalid octal - interpreted as 79
var octalNum3 = 08;		//invalid octal - interpreted as 8
```

 *Octal literals are invalid when running in strict mode and will case the JavaScript engine to throw a syntax error.*



**Hexadecimal literal**

A hexadecimal literal, the first two characters 0x (case insensitive), followed by any number of hexadecimal digits (0~9, A~F, uppercase or lowercase).

```
var haxNum1 = 0xA;		//hexadecimal for 10
var hexNum2 = 0x1f;		//hexadecimal for 31
```

**Octal or hexadecimal format are treated as decimal numbers in all arithmetic operations.**

*it is possiable to have a value of +0 and -0, are considered equivalent*



#### 2. Floating-Point Values

To define a floating-point value, you must include a decimal point and at least one number after the decimal point.

```
var floatNum1 = 1.1;
var floatNum2 = 0.1;
var floatNum3 = .1;		//valid, but not recommended
```



ECMAScript always looks for ways to convert values into integers.

*(Because storing floating-point values use twice as much memory as storing integer values.)*

```
var floatNum1 = 1.;		//missing digit after decimal - interpreted as integer 1
var floatNum2 = 10.0;	//whole number - interpreted as integer 10
```



**E-notation** is used to indicate a number that should be multiplied by 10 raised to a given power.

```
var floatNum = 3.125e7;		//equal to 31250000

//The format of e-notation, a number(integer or floating-point) followed by an uppercase or lowercase letter E, followed by the power of 10 to multiply by.
```

1. ECMAScript converts any floating-point value with at least six zeros after the decimal point into e-notation (0.0000003 become 3e-7 ).

2. Floating-point values are accurate up to 17 decimal places but are far accurate in arithmetic computations than whole numbers (adding 0.1 and 0.2 yields 0.30000000000000004 instead of 0.3)

   ```
   if (a + b == 0.3){		//avoid! this test will fail. 
     alert("you got 0.3");
   }
   //This will work for 0.05 and 0.25, never test for specific floating-point value
   ```

   ​

#### 3. Range of Values

The smallest number is stored in Number.MIN_VALUE and is 5e-324 on most browsers.

The last number is stored in Number.MAX_VALUE and is 1.7976931348623157e+308 on most browsers.

The **isFinite()** function returns true only if the argument is between the minimum and the maximum values.

```
var result = Number.MAX_VALUE + Number.MAX_VALUE;
alert(isFinite(result));	//false
```



#### 4. NaN

NaN (*Not a Number*) is a special value, used to indicate when an operation intended to return a number has failed (as opposed to throwing an error).

1. Any operation involving NaN always returns NaN (for instance, NaN/10), which can be problematic in the case of multistep computations.

2. NaN is not equal to any value, including NaN.

   ```
   alert(NaN == NaN);		//false
   ```



The **isNaN()** function accepts a single argument, which can be of any data type, to determine if the value is "not a number".

```
alert(isNaN(NaN));		//true
alert(isNaN(10));		//false - 10 is a number
alert(isNaN("10"));		//false - can be converted to number 10
alert(isNaN("blue"));	//true - cannot be converted to a number
alert(isNaN(true));		//false - can be converted to number 1
```

*isNaN( ) can be applied to object.*



#### 5. Number Conversions

Number( ) can be used on any data type.

parseInt( ), parseFloat( )  are used for converting strings to numbers.



The **Number( )** function

> Applied to Boolean values, true and false get converted into 1 and 0.
>
> Applied to numbers, the value is passed through and returned
>
> Applied to null, return 0
>
> Applied to undefined, return NaN.
>
> Applied to strings, the following rules are applied:
>
> > 1. If the string contains only numbers, optionally preceded by a plus or minus sign, it is converted to a decimal number, so “1” becomes 1, “123” becomes 123, and “011” becomes 11 (note: leading zeros are ignored).
> > 2. If the string contains a valid ﬂoating-point format, such as “1.1”, it is converted into the appropriate ﬂoating-point numeric value (once again, leading zeros are ignored).
> > 3. If the string contains a valid hexadecimal format, such as “0xf”, it is converted into an integer that matches the hexadecimal value.
> > 4. If the string is empty (contains no characters), it is converted to 0.
> > 5. If the string contains anything other than these previous formats, it is converted into NaN.
>
> Applied to objects, the valueOf() method is called and the returned value is converted based on the previously described rules. If that conversion results in NaN, the toString() method is called and the rules for converting strings are applied.

```
var num1 = Number("hello");		//NaN
var num2 = Number("");			//0
var num3 = Number("000011");	//11
var num4 = Number(true);		//1
```



The **parseInt( )** function

a better option when dealing with integers.

1. Leading white space in the string is ignored until the first non-white space character is found.

2. If this ﬁrst character isn’t a number, the minus sign, or the plus sign, parseInt() always returns NaN. the empty string returns NaN (Number( ) returns 0).

3. If the ﬁrst character is a number, plus, or minus, then the conversion goes on to the second character and continues on until either the end of the string is reached or a nonnumeric character is found. For instance, “1234blue” is converted to 1234 because “blue” is completely ignored. Similarly, “22.5” will be converted to 22 because the decimal is not a valid integer character.

4. if the string begins with “0x”, it is interpreted as a hexadecimal integer.

5. if it begins with “0” followed by a number, it is interpreted as an octal value.

```
var num1 = parseInt("1234blue");	//1234
var num2 = parseInt("");			//NaN
var num3 = parseInt("0xA");			//10 - hexadecimal
var num4 = parseInt(22.5);			//22
var num5 = parseInt("70");			//70 - decimal
var num6 = parseInt("0xf");			//15 - hexadecimal
```

```
var num = parseInt("0xAF", 16);		//175
```

```
 //providing the hexadecimal radix, you can leave off the leading"0x"
 var num1 = parseInt("AF", 16);		//175
 var num2 = parseInt("AF");			//NaN
```

   ```
var num1 = parseInt("10", 2);		//2 - parsed as binary
var num2 = parseInt("10", 8);		//8 - parsed as octal
var num3 = parseInt("10", 10);		//10 - parse as decimal
var num4 = parseInt("10", 16);		//16 - parse as hexadecimal
   ```



The **parseFloat( )** function

Works in a similar way to parseInt().

1. Looking at each character starting in position 0, parse the string until it reaches either the end of the string or a character that is invalid in a floating-point number (a decimal point is valid the first time, a second decimal point is invalid and the rest of the string is ignored, "22.34.5" converted to 22.34)
2. initial zeros are ignored.
3. Hexadecimal numbers become 0.
4. if the string represents a whole number (no decimal point or only a zero after the decimal point), parseFloat( ) returns an integer

```
var num1 =parseFloat("1234blue");	//1234 - integer
var num1 =parseFloat("0xA");		//0
var num1 =parseFloat("22.5");		//22.5
var num1 =parseFloat("22.34.5");	//22.34
var num1 =parseFloat("0908.5");		//908.5
var num1 =parseFloat("3.125e7");	//31250000
```


### <u>The String Type</u>

The String data type represents a sequence of zero or more 16-bit Unicode characters.

#### Character Literals

| LITERAL | MEANING                                  |
| ------- | ---------------------------------------- |
| \n      | New Line                                 |
| \t      | Tab                                      |
| \b      | Backspace                                |
| \r      | Carriage return                          |
| \f      | Form feed                                |
| \\\     | Backslash(\\)                            |
| \\`     | Single quote( ' ). Example: 'He said, \'hey.\''. |
| \''     | Double quote( '' ). Example: "He said, \"hey.\"". |
| \xnn    | A character represented by hexadecimal code nn(where n is a hexadecimal digit 0-F). Example: \x41 is equivalent to "A". |
| \unnnn  | A Unicode character represented by the hexadecimal code nnn(where n is a hexadecimal digit 0-F). Example: \u03a3 is equivalent to the Greek character . |

```
var text = "This is the letter sigma: \u03a3.";
```

```
alert(text.length);		//outputs 28
//If a string contains double-byte characters, the length property may not accurately return the number of characters in the string.
```



**The Nature of Strings**

Strings are immutable in ECMAScript, once they are created, their values cannot change. To change the string held by a variable, the original string must be destroyed  and the variable filled with another string containing a new value.

```
var lang = "Java";
lang = lang + "Script";
```



#### Converting to a String

The **toString( )** method

is available on values that are numbers, Booleans, objects, strings.

is not available if a value is null or undefined.

```
var num = 10;
alert(num.toString());		//"10"
alert(num.toString(2));		//"1010"
alert(num.toString(8));		//"12"
alert(num.toString(10));	//"10"
alert(num.toString(16));	//"a"
```









### <u>The Object Type</u>