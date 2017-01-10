# HTML DOM Event

## 键盘事件

### onkeydown 事件

onkeydown 事件会在用户按下一个键盘按键时发生。

**提示：** 与 onkeydown 事件相关联的事件触发次序:

1. onkeydown
2. onkeypress
3. onkeyup

**语法**

HTML 中:

```hrml
<element onkeydown="SomeJavaScriptCode">
```

JavaScript 中:

```javascript
object.onkeydown=function(){SomeJavaScriptCode};
```

> *SomeJavaScriptCode* 	必需。规定该事件发生时执行的 JavaScript。
>
> onkeydown 属性可用于所有的 HTML 元素，除了：<base>, <bdo>, <br>, <head>, <html>, <iframe>, <meta>, <param>, <script>, <style>, 和 <title>.



------



### onkeypress 事件

onkeypress 事件会在键盘按键被按下并释放一个键时发生。

**提示：**与 onkeypress 事件的关联的事件发生次序:

1. onkeydown
2. onkeypress
3. onkeyup

**注意：** 在所有浏览器中 onkeypress 事件不是适用于所有按键(如： ALT, CTRL, SHIFT, ESC)。监听一个用户是否按下按键请使用 [onkeydown](http://www.runoob.com/jsref/event-onkeydown.html) 事件,所有浏览器都支持 onkeydown 事件。

**语法**

HTML 中:

```hrml
<element onkeypress="SomeJavaScriptCode">
```

JavaScript 中:

```javascript
object.onkeypress=function(){SomeJavaScriptCode};
```

> *SomeJavaScriptCode* 	必需。规定该事件发生时执行的 JavaScript。
>
> onkeypress 属性可以适用于所有 HTML 元素，除了：<base>, <bdo>, <br>, <head>, <html>, <iframe>, <meta>, <param>, <script>, <style>, 和 <title>.



------



### onkeyup 事件

onkeyup 事件会在键盘按键被松开时发生。

**提示：**与onkeyup 事件相关的事件发生次序：

1. onkeydown
2. onkeypress
3. onkeyup

**语法**

HTML 中:

```hrml
<element onkeyup="SomeJavaScriptCode">
```

JavaScript 中:

```javascript
object.onkeyup=function(){SomeJavaScriptCode};
```

> *SomeJavaScriptCode* 	必需。规定该事件发生时执行的 JavaScript。
>
> onkeyup 属性可以适用于所有 HTML 元素，除了： <base>, <bdo>, <br>, <head>, <html>, <iframe>, <meta>, <param>, <script>, <style>, 和 <title>。



------



## 鼠标/键盘事件对象



------



### charCode 事件属性

charCode 属性返回[onkeypress](http://www.runoob.com/jsref/event-onkeypress.html)事件触发键值的字母代码。

> Unicode 字符代码是一个字母的数字 (如数字 "97" 代表字母 "a")。

**提示：** 所有 Unicode 字符列表可查看我们的 [完整 Unicode 参考手册](http://www.runoob.com/charsets/ref-html-utf8.html)。

**提示：** 如果你需要将 Unicode 值转换为字符，可以使用 [fromCharCode()](http://www.runoob.com/jsref/jsref-fromcharcode.html) 方法。

**注意：** 如果该属性用于 [onkeydown](http://www.runoob.com/jsref/event-onkeydown.html) 或 [onkeyup](http://www.runoob.com/jsref/event-onkeyup.html) 事件，返回值总为 "0"。

**注意：** 该属性是只读的。

**注意：** which 和 keyCode 属性提供了解决浏览器的兼容性的方法，最新版本的 DOM 事件推荐使用 [key](http://www.runoob.com/jsref/event-key-key.html) 属性来替代该方法。

**注意：**IE8 及其更早版本不支持 which 属性。不支持的浏览器可使用 [keyCode](http://www.runoob.com/jsref/event-key-keycode.html) 属性。但是， keyCode 属性在 Firefox 浏览器的 onkeypress 事件中是无效的。 兼容这些浏览器你可以使用以下代码：

```javascript
var x = event.charCode || event.keyCode; // 使用 charCode 或 keyCode, 这样可支持不同浏览器
```

**提示：** 你同样可以使用 keyCode 属性来检测特殊的按键 (如 "caps lock" 或 箭头按键)。 keyCode 和 charCode 属性提供了解决浏览器的兼容性的方法，最新版本的 DOM 事件推荐使用 [key](http://www.runoob.com/jsref/event-key-key.html) 属性来替代该方法。

**提示：** 如果你想查看是否按下了 "ALT", "CTRL", "META" 或 "SHIFT" 键，可使用 [altKey](http://www.runoob.com/jsref/event-key-altkey.html), [ctrlKey](http://www.runoob.com/jsref/event-key-ctrlkey.html), [metaKey](http://www.runoob.com/jsref/event-key-metakey.html) 或 [shiftKey](http://www.runoob.com/jsref/event-key-shiftkey.html) 属性。

**语法**

```
event.charCode
```



------



### key 事件属性

key 事件在按下按键时返回按键的标识符。

按键标识符是表示键盘按钮的字符串，该属性的返回值可以是：

- 单个字母 (如 "a", "W", "4", "+" 或 "$")
- 多个字母 (如 "F1", "Enter", "HOME" 或 "CAPS LOCK")

**提示：** 如果你想查看是否按下了 "ALT", "CTRL", "META" 或 "SHIFT" 键，可使用 [altKey](http://www.runoob.com/jsref/event-key-altkey.html), [ctrlKey](http://www.runoob.com/jsref/event-key-ctrlkey.html), [metaKey](http://www.runoob.com/jsref/event-key-metakey.html) 或 [shiftKey](http://www.runoob.com/jsref/event-key-shiftkey.html) 属性。

**注意：** Chrome，Safari 和 Opera浏览器返回 undefined

**DOM 版本**: DOM Level 3 Events

**语法**

```
event.key
```

**Example**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
    <meta charset="utf-8">
    <title>HTML DOM Event_key</title>

    <script>
        function myPress(event) {
            var x = event.key;
            document.getElementById("demo").innerHTML = "onkeypress 按键为: " + x;
        }

        function myDown(event) {
            var x = event.key;
            document.getElementById("demo").innerHTML = "onkeydown 按键为: " + x;
        }
    </script>
</head>

<body>
    <form name="rkCode">
        onkeypress:
        <input type="text" name="press" onkeypress="myPress(event)"> <br> onkeydown:
        <input type="text" name="down" onkeydown="myDown(event)">
    </form>
    <p id="demo"></p>
</body>
</html>
```



------



### keyCode 事件属性

keyCode 属性返回[onkeypress](http://www.runoob.com/jsref/event-onkeypress.html)事件触发的键的值的字符代码，或者 [onkeydown](http://www.runoob.com/jsref/event-onkeydown.html) 或 [onkeyup](http://www.runoob.com/jsref/event-onkeyup.html) 事件的键的代码。

两种代码类型的区别是:

- 字符代码 - 表示 ASCII 字符的数字
- 键盘代码 - 表示键盘上真实键的数字

> 两种类型的值不是都相等的，例如小写字符 "w" 和大写字符 "W" 有相同的键盘代码（键盘上 "W" 代码为 "87")。但是它们有不同的字符代码，( "w" 和 "W" 字符代码为 "119" 和 "87") 
>
> **提示：**如果需要知道用户按下的是打印键 (如 "a" 或 "5")，建议使用 onkeypress 事件。如果需要知道用户按下的是功能键(如 "F1", "CAPS LOCK" 或 "Home") 可使用 onkeydown 或 onkeyup 事件。
>
> **注意：**在 Firefox 中，, keyCode 属性在 onkeypress 事件中是无效的 (返回 0)。浏览器兼容问题，可以一起使用 [which](http://www.runoob.com/jsref/event-key-which.html) 和 keyCode 属性来解决:
>
> ```javascript
> var x = event.which || event.keyCode;  // 使用 which 或 keyCode, 这样可支持不同浏览器
> ```
> **提示：** 所有 Unicode 字符列表可查看我们的 [完整 Unicode 参考手册](http://www.runoob.com/charsets/ref-html-utf8.html)。
>
> **提示：** 如果你需要将 Unicode 值转换为字符，可以使用 [fromCharCode()](http://www.runoob.com/jsref/jsref-fromcharcode.html) 方法。
>
> **注意：** 该属性是只读的。
>
> **注意：** which 和 keyCode 属性提供了解决浏览器的兼容性的方法，最新版本的 DOM 事件推荐使用 [key](http://www.runoob.com/jsref/event-key-key.html) 属性来替代该方法。
>
> **提示：** 如果你想查看是否按下了 "ALT", "CTRL", "META" 或 "SHIFT" 键，可使用 [altKey](http://www.runoob.com/jsref/event-key-altkey.html), [ctrlKey](http://www.runoob.com/jsref/event-key-ctrlkey.html), [metaKey](http://www.runoob.com/jsref/event-key-metakey.html) 或 [shiftKey](http://www.runoob.com/jsref/event-key-shiftkey.html) 属性。

**语法**

```javascript
event.keyCode
```
**Example**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
    <meta charset="UTF-8">
    <title>Keyboard_Key</title>

    <script>
        // keycode()
        function kCode(event) {
            //alert(event.keyCode)
            var x = event.keyCode;
            document.getElementById("rtext").innerHTML = " Unicode 值为: " + x;
        }
    </script>
</head>

<body>
    <form name="rkCode">
        <input type="text" name="key" onKeyDown="kCode(event)">
    </form>
    <p id="rtext"></p>
</body>

</html>
```



------



### which 事件属性

which 属性返回[onkeypress](http://www.runoob.com/jsref/event-onkeypress.html)事件触发的键的值的字符代码，或者 [onkeydown](http://www.runoob.com/jsref/event-onkeydown.html) 或 [onkeyup](http://www.runoob.com/jsref/event-onkeyup.html) 事件的键的代码。

两种代码类型的区别是:

- 字符代码 - 表示 ASCII 字符的数字
- 键盘代码 - 表示键盘上真实键的数字

两种类型的值不是都相等的，例如小写字符 "w" 和大写字符 "W" 有相同的键盘代码，因为他们他们键盘上 ( "W" 代码为 "87")，但是它们有不同的字符代码，两个字符输出是不一样的( "w" 和 "W" 字符代码为 "119" 和 "87") 。

**提示：** 如果需要知道用户按下的是打印键 (如 "a" 或 "5")，建议使用 onkeypress 事件。如果需要知道用户按下的是功能键(如 "F1", "CAPS LOCK" 或 "Home") 可使用 onkeydown 或 onkeyup 事件。

**注意：**IE8 及其更早版本不支持 which 属性。不支持的浏览器可使用 [keyCode](http://www.runoob.com/jsref/event-key-keycode.html) 属性。但是， keyCode 属性在 Firefox 浏览器的 onkeypress 事件中是无效的。 兼容这些浏览器你可以使用以下代码：

```javascript
var x = event.which || event.keyCode;  // 使用 which 或 keyCode, 这样可支持不同浏览器
```

**提示：** 所有 Unicode 字符列表可查看我们的 [完整 Unicode 参考手册](http://www.runoob.com/charsets/ref-html-utf8.html)。

**提示：** 如果你需要将 Unicode 值转换为字符，可以使用 [fromCharCode()](http://www.runoob.com/jsref/jsref-fromcharcode.html) 方法。

**注意：** 该属性是只读的。

**注意：** which 和 keyCode 属性提供了解决浏览器的兼容性的方法，最新版本的 DOM 事件推荐使用 [key](http://www.runoob.com/jsref/event-key-key.html) 属性来替代该方法。

**提示：** 如果你想查看是否按下了 "ALT", "CTRL", "META" 或 "SHIFT" 键，可使用 [altKey](http://www.runoob.com/jsref/event-key-altkey.html), [ctrlKey](http://www.runoob.com/jsref/event-key-ctrlkey.html), [metaKey](http://www.runoob.com/jsref/event-key-metakey.html) 或 [shiftKey](http://www.runoob.com/jsref/event-key-shiftkey.html) 属性。

**语法**

```
event.which
```



------

