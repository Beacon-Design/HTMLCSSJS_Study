# CoffeeScript Study Notes



# 0. Getting Started



## 0.1 Study Reference

http://coffeescript.org/

http://coffee-script.org/

http://autotelicum.github.io/Smooth-CoffeeScript/

http://arcturo.github.io/library/coffeescript/index.html





## 0.2 Install 

To install, first make sure you have a working copy of the latest stable version of [Node.js](http://nodejs.org/). You can then install CoffeeScript globally with [npm](http://npmjs.org/):

**Terminal**


```
sudo npm -g install coffee-script
```
**Install Success**

```
/usr/local/bin/coffee -> /usr/local/lib/node_modules/coffee-script/bin/coffee
/usr/local/bin/cake -> /usr/local/lib/node_modules/coffee-script/bin/cake
/usr/local/lib
└── coffee-script@1.12.5 
```

**Run CoffeeScript in Terminal**

```
coffee
```



# 1. Introduction

The golden rule of CoffeeScript is: *“It’s just JavaScript”*.

 The code compiles one-to-one into the equivalent JS, and there is no interpretation at runtime. 

You can use any existing JavaScript library seamlessly from CoffeeScript (and vice-versa). The compiled output is readable, pretty-printed, and tends to run as fast or faster than the equivalent handwritten JavaScript.

**CoffeeScript uses significant whitespace to delimit blocks of code.** 

> You don’t need to use semicolons `;` to terminate expressions, ending the line will do just as well (although semicolons can still be used to fit multiple expressions onto a single line). 

**use indentation**

> **Instead of using curly braces** `{ }` to surround blocks of code in [functions](http://coffeescript.org/#literals), [if-statements](http://coffeescript.org/#conditionals), [switch](http://coffeescript.org/#switch), and [try/catch](http://coffeescript.org/#try).you can replace curly brackets (`{}`) with a tab. This takes inspiration from Python's syntax, and has the excellent side effect of **ensuring** that your **script is formatted in a sane manner**, **otherwise it won't even compile!**



## Comments 

 starting with a hash character.

```coffeescript
# A comment
```

Multiline comments are enclosed by three hash characters.

```coffeescript
###
  A multiline comment, perhaps a LICENSE.
###
```

> [compiled JavaScript]
>
> ```javascript
> /*
>   A multiline comment, perhaps a LICENSE.
> */
> ```



## Variables & Scope

### Local Variables

variable assignment in CoffeeScript :

```coffeescript
myVariable = "test"
```

> [compiled JavaScript]
>
> ```javascript
> var myVariable;
> myVariable = "test";
> ```

### Global Variables

You can either do this by directly setting them as properties on the global object (`window` in browsers), or with the following pattern:

```coffeescript
exports = this
exports.MyVariable = "foo-bar"
```

> [compiled JavaScript]
>
> ```javascript
> var exports;
> exports = this;
> exports.MyVariable = "foo-bar";
> ```
>
> In the root context, `this` is equal to the global object, and by creating a local `exports` variable you're making it really obvious to anyone reading your code exactly which global variables a script is creating. 



## Functions

`->`. Functions can be one liners or indented on multiple lines.

The last expression in the function is implicitly returned. In other words, you don't need to use the `return` statement unless you want to return earlier inside the function.

```coffeescript
func = -> "bar"
```

> the `->` is turned into a `function` statement, and the `"bar"` string is automatically returned.
>
> [compiled JavaScript]
>
> ```javascript
> var func;
> func = function() {
>   return "bar";
> };	
> ```

indent the function body properly version:

```coffeescript
func = ->
  # An extra line
  "bar"
```



## Function arguments

1. pecifying arguments in parentheses before the arrow.

```coffeescript
times = (a, b) -> a * b
```

> [compiled JavaScript]
>
> ```javascript
> var times;
> times = function(a, b) {
>   return a * b;
> };
> ```

2. default arguments

```coffeescript
times = (a = 1, b = 2) -> a * b
```

>[compiled JavaScript]
>
> ```javascript
> var times;
> times = function(a, b) {
>   if (a == null) {
>     a = 1;
>   }
>   if (b == null) {
>     b = 2;
>   }
>   return a * b;
> };
> ```

3. use splats to accept multiple arguments, denoted by `...`

```coffeescript
sum = (nums...) -> 
  result = 0
  nums.forEach (n) -> result += n
  result
```

> [compiled JavaScript]
>
> ```javascript
> var sum;
> var __slice = Array.prototype.slice;
> sum = function() {
>   var nums, result;
>   nums = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
>   result = 0;
>   nums.forEach(function(n) {
>     return result += n;
>   });
>   return result;
> };
> ```
> In the example above, `nums` is an array of all the arguments passed to the function. It's not an `arguments` object, but rather a real array, so you don't need to concern yourself with `Array.prototype.splice` or `jQuery.makeArray()` if you want to manipulate it.

```coffeescript
trigger = (events...) ->
  events.splice(1, 0, this)
  this.constructor.trigger.apply(events)
```

> [compiled JavaScript]
>
> ```javascript
> var trigger;
> var __slice = Array.prototype.slice;
> trigger = function() {
>   var events;
>   events = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
>   events.splice(1, 0, this);
>   return this.constructor.trigger.apply(events);
> };
> ```



## Function invocation















