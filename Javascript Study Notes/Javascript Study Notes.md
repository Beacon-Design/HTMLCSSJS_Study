#Javascript Study Notes



# 0. Getting Started



## 0.1 Study Reference

JavaScript高级程序设计(第3版). Professional JavaScript for Web Developers, 3rd Edition

















Execution Context(Global level)
run javascript engine creat a object and a special varable:
1.Global Object 
2."this"

in Browser,the Global Object is window.
at the global level,Global Object(window)="this".
"this" refer to window object

in JavaScript when you creat variables and functions.you're not inside a function.those variables and functions get attached to the globle object 

**Hoisting**
setup memory space for variables and functions.
all variabes in JavaScript are initially set to undefined and functions are sitting in memory in their entirety


undefined is a value that JavaScript created ,it took momery space


**Single Threaded, Synchronous Execution**
Single Threaded: one command at a time
(Under the hood of the browser,maybe not )
Synchronous: one at a time
(And in order...)

**Function Invocation And The Execution Stack**
Invocation:running a function.in JavaScript,by using parenthesis() 

every function creates a new execution context which runs through the create phase and then execute the code line by line within the function

Variable Environment:where the variables live(and how they relate to each other in memory)

**The Scope Chain**
every execution context has a reference to its outer environment

JavaScript,it carries about the lexical environment when it comes to the outer reference that every execution context gets and when you ask for a variable while running a line of code inside any particular execution context if it can't find that variable it will look at the outer reference and go look for variables there somewhere down below it in the execution stack and outer reference where that points is going to depend on where the function sits lexically


**Scope**
where a variable is avaliable in your code
and if it's truly the same variable,or a new copy

**Namespace**
A Container For Variables And Functions 
(Typically to keep variables and functions with the same name separate)

**First Class Function**
Everything you can do with other types you can do with other types you can do with functions.
(Assign them to variables,padd them around,creat them on the fly)

Function ,a special type of object{Primitive, Object, Function, {NAME oprion,can be anonymous}, code(invocable)}

**expression**
 1.function is a statement, stay in the memory.
 ```
 function greet(){
    console.log("hi");
 }
 ```

 2.expression result(return) a value.

 3.function expression
 >1.putting this object into memory and pointing that anonymous variable at that address
 >
 >2.function expressions aren't hoisted

 ```
 var greet = function(){
    console.log("hi");
 }
 greet();
 ```

