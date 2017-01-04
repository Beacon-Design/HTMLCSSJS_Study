# Variables, Scope, and Memory

# PRIMITIVE AND REFERENCE VALUES

ECMAScript variables may contain two different types of data: primitive values and reference values. Primitive values are simple atomic pieces of data, while reference values are objects that may be made up of multiple values.

When a value is assigned to a variable, the JavaScript engine must determine if it’s a primitive or a reference. 

The **ﬁve primitive types: Undeﬁned, Null, Boolean, Number, and String**. These variables are said to be accessed by value, because you are manipulating the actual value stored in the variable.

**Reference values are objects stored in memory**.When you manipulate an object, you’re really working on a reference to that object rather than the actual object itself. For this reason, such values are said to be accessed by reference.



## Dynamic Properties

a variable is created and assigned a value.

**Reference values**, you can add, change, or delete properties and methods at any time.

```javascript
var person = new Object();
person.name = "Nicholas";
alert(person.name);		//"Nicholas"
```

**Primitive values** can’t have properties added to them 

```javascript
var name = "Nicholas";
name.age = 27;
alert(name.age);		//undefined
```



## Copying Values

- **A primitive value is assigned from one variable to another**, the value stored on the variable object is created and copied into the location for the new variable. **Each of these variables can now be used separately with no side effects.**

> ![primitive value is assigned from one variable to another](/Users/yl/Documents/HUB/HTMLCSSJS_Study/Basic Javascript/Chapter 4_Variables Scope and Memory/primitive value is assigned from one variable to another.png)



- **A reference value is assigned from one variable to another**, the value stored on the variable object is also copied into the location for the new variable. The difference is that **this value is actually a pointer to an object** stored on the heap. Once the operation is complete, **two variables point to exactly the same object, so changes to one are reﬂected on the other**

> ```javascript
> var obj1 = new Object(); 
> var obj2 = obj1; 
> obj1.name = “Nicholas”; 
> alert(obj2.name); 	//”Nicholas”
> ```
>
> ![Reference value is assigned from one variable to another](/Users/yl/Documents/HUB/HTMLCSSJS_Study/Basic Javascript/Chapter 4_Variables Scope and Memory/Reference value is assigned from one variable to another.png)



## Argument Passing

- **All function arguments in ECMAScript are passed by value.** This means that the value outside of the function is copied into an argument on the inside of the function **the same way a value is copied from one variable to another.**


- If the value is **primitive**, then it acts just **like a primitive variable copy**,

  > ```javascript
  > function addTen(num) { 
  > 	num += 10;
  >     return num; 
  > }
  >
  > var count = 20; 
  > var result = addTen(count); 
  > alert(count); //20，没有变化 
  > alert(result); //30
  > ```


- if the value is a **reference**, it acts just **like a reference variable copy**

  > ```javascript
  > function setName(obj) { 
  > 	obj.name = "Nicholas"; 
  > }
  >
  > var person = new Object(); 
  > setName(person); 
  > alert(person.name); //"Nicholas"
  > ```

  > ```javascript
  > function setName(obj) { 
  > 	obj.name = "Nicholas"; 
  > 	obj = new Object(); 
  > 	obj.name = "Greg"; 
  > }
  >
  > var person = new Object(); 
  > setName(person); 
  > alert(person.name); //"Nicholas"
  > ```
  >
  > When obj is overwritten inside the function, it becomes a pointer to a local object. That local object is destroyed as soon as the function ﬁnishes executing.
  >
  > **Think of function arguments in ECMAScript as nothing more than local variables.**




## Determining Type

The typeof operator, is the best way to **determine if a variable is a primitive type.**

> ```javascript
> var s = “Nicholas”; 
> var b = true; 
> var i = 22; 
> var u; 
> var n = null; 
> var o = new Object();
>
> alert(typeof s);	//string 
> alert(typeof i);	//number  
> alert(typeof b);	//boolean  
> alert(typeof u);	//undefined  
> alert(typeof n);	//object 
> alert(typeof o);	//object
> ```



**what type of object it is**. ECMAScript provides the `instanceof` operator, which is used with the following syntax:

> `result = variable instanceof constructor`

The instanceof operator returns true if the variable is an instance of the given reference type

> ```javascript
> alert(person instanceof Object);	
> //is the variable person an Object? 
>
> alert(colors instanceof Array); 
> //is the variable colors an Array?
>
> alert(pattern instanceof RegExp);
> //is the variable pattern a RegExp?
> ```



> All reference values, by deﬁnition, are instances of Object, so the `instanceof` operator always returns true when used with a reference value and the Object constructor. Similarly, if instanceof is used with a primitive value, it will always return false, because primitives aren’t objects.



# EXECUTION CONTEXT AND SCOPE

The execution context of a variable or function deﬁnes what other data it has access to, as well as how it should behave. Each execution context has an associated variable object upon which all of its deﬁned variables and functions exist. This object is not accessible by code but is used behind the scenes to handle data.