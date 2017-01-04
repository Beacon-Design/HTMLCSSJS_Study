# Emmet Keyboard Shortcuts_Syntax

## Child: >

```html
nav>ul>li
```

> ```html
> <nav>
>     <ul>
>         <li></li>
>     </ul>
> </nav>
> ```



## Sibling: +

```
div+p+bq
```

> ```html
> <div></div>
> <p></p>
> <blockquote></blockquote>
> ```



## Climb-up: ^

```
div+div>p>span+em^bq
```

> ```html
> <div></div>
> <div>
>     <p><span></span><em></em></p>
>     <blockquote></blockquote>
> </div>
> ```



```
div+div>p>span+em^^bq
```

> ```html
> <div></div>
> <div>
>     <p><span></span><em></em></p>
> </div>
> <blockquote></blockquote>
> ```



## Grouping: ()

```
div>(header>ul>li*2>a)+footer>p
```

> ```html
> <div>
>     <header>
>         <ul>
>             <li><a href=""></a></li>
>             <li><a href=""></a></li>
>         </ul>
>     </header>
>     <footer>
>         <p></p>
>     </footer>
> </div>
> ```



```
(div>dl>(dt+dd)*3)+footer>p
```

> ```html
> <div>
>     <dl>
>         <dt></dt>
>         <dd></dd>
>         <dt></dt>
>         <dd></dd>
>         <dt></dt>
>         <dd></dd>
>     </dl>
> </div>
> <footer>
>     <p></p>
> </footer>
> ```



## Multiplication: *

```
ul>li*5
```

> ```html
> <ul>
>     <li></li>
>     <li></li>
>     <li></li>
>     <li></li>
>     <li></li>
> </ul>
> ```



## Item numbering: $

```
ul>li.item$*5
```

> ```html
> <ul>
>     <li class="item1"></li>
>     <li class="item2"></li>
>     <li class="item3"></li>
>     <li class="item4"></li>
>     <li class="item5"></li>
> </ul>
> ```



```
h$[title=item$]{Header $}*3
```

> ```html
> <h1 title="item1">Header 1</h1>
> <h2 title="item2">Header 2</h2>
> <h3 title="item3">Header 3</h3>
> ```



```
ul>li.item$$$*5
```

> ```html
> <ul>
>     <li class="item001"></li>
>     <li class="item002"></li>
>     <li class="item003"></li>
>     <li class="item004"></li>
>     <li class="item005"></li>
> </ul>
> ```



```html
ul>li.item$@-*5
```

> ```html
> <ul>
>     <li class="item5"></li>
>     <li class="item4"></li>
>     <li class="item3"></li>
>     <li class="item2"></li>
>     <li class="item1"></li>
> </ul>
> ```



```
ul>li.item$@3*5
```

> ```html
> <ul>
>     <li class="item3"></li>
>     <li class="item4"></li>
>     <li class="item5"></li>
>     <li class="item6"></li>
>     <li class="item7"></li>
> </ul>
> ```



## ID and CLASS attributes

```
#header
```

> ```html
> <div id="header"></div>
> ```



```
.title
```

> ```html
> <div class="title"></div>
> ```



```
form#search.wide
```

> ```html
> <form id="search" class="wide"></form>
> ```



```html
p.class1.class2.class3
```

> ```html
> <p class="class1 class2 class3"></p>
> ```



## Custom attributes

```
p[title="Hello world"]
```

> ```html
> <p title="Hello world"></p>
> ```



```
td[rowspan=2 colspan=3 title]
```

> ```html
> <td rowspan="2" colspan="3" title=""></td>
> ```



```
[a='value1' b="value2"]
```

> ```html
> <div a="value1" b="value2"></div>
> ```



## Text: {}

```
a{Click me}
```

> ```html
> <a href="">Click me</a>
> ```



```
p>{Click }+a{here}+{ to continue}
```

> ```html
> <p>Click <a href="">here</a> to continue</p>
> ```



## Implicit tag names

```
.class
```

> ```html
> <div class="class"></div>
> ```



```
em>.class
```

> ```html
> <em><span class="class"></span></em>
> ```



```
ul>.class
```

> ```html
> <ul>
>     <li class="class"></li>
> </ul>
> ```



```
table>.row>.col
```

> ```html
> <table>
>     <tr class="row">
>         <td class="col"></td>
>     </tr>
> </table>
> ```

