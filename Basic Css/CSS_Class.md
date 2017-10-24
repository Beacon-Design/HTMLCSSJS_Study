#  CSS Selectors (CSS 选择器)

## [Type selectors (元素选择器)](https://developer.mozilla.org/en-US/docs/Web/CSS/Type_selectors)

CSS type selectors match elements by node name. Used alone, therefore, a type selector for a particular node name selects all elements of that type — that is, with that node name — in the document.

**Syntax**

```css
element { style properties }		
```

CSS

```css
span {
  background-color: DodgerBlue;
  color: #ffffff;
}
```

HTML

```css
<span>Here's a span with some text.</span>
<p>Here's a p with some text.</p>
<span>Here's a span with more text.</span>
```

> CSS 元素选择器（类型选择器）可以设置 XML 文档中元素的样式。

------



## [Class selectors (类选择器)](https://developer.mozilla.org/en-US/docs/Web/CSS/Class_selectors)

In an HTML document, CSS class selectors match an element based on the contents of the element's class attribute. The `class`attribute is defined as a space-separated list of items, and one of those items must match exactly the class name given in the selector.

在一个HTML文档中，CSS类选择器会根据元素的类属性中的内容匹配元素。类属性被定义为一个以空格分隔的列表项，在这组类名中，必须有一项与类选择器中的类名完全匹配，此条样式声明才会生效。

**Syntax**

```css
.classname { style properties }
```

Note this is equivalent to the following [attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors):

```css
[class~=classname] { style properties }
```

CSS

```css
span.apple {
  background-color: DodgerBlue;
}
```

> 选择器现在会匹配 class 属性包含 apple 的所有 span 元素，但是其他任何类型的元素都不匹配，不论是否有此 class 属性。

HTML

```css
<span class="apple">Here's a span with some text.</span>
<span>Here's another.</span>
```



### CSS 多类选择器

在 HTML 中，一个 class 值中可能包含一个词列表，各个词之间用空格分隔。例如，如果希望将一个特定的元素同时标记为 apple 和 banana. 这两个词的顺序无关紧要，写成 banana apple 也可以。

**通过把两个类选择器链接在一起，仅可以选择*同时包含这些类名*的元素（类名的顺序不限）。**

选择同时包含类名 apple 和 banana 的p元素（类名的顺序不限）

CSS

```css
.apple.banana{background:blue;}
```

HTML

```html
<p class="apple banana pear">
This paragraph is a very important warning.
</p>
```

------



## [ID selectors (ID选择器)](https://developer.mozilla.org/en-US/docs/Web/CSS/ID_selectors)

In an HTML document, CSS ID selectors match an element based on the contents of that element's `id` attribute, which must match exactly the value given in the selector.

**Syntax**

```css
#id_value { style properties }
```

Note this is equivalent to the following [attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors):

```css
[id=id_value] { style properties }
```

CSS

```css
span#identified {
  background-color: DodgerBlue;
}
```

HTML

```html
<span id="identified">Here's a span with some text.</span>
<span>Here's another.</span>
```

------



## [Universal selectors (通配选择器)](https://developer.mozilla.org/en-US/docs/Web/CSS/Universal_selectors)

An asterisk (`*`) is the universal selector for CSS. It matches a single element of any type. Omitting the asterisk with simple selectors has the same effect. For instance, `*.warning` and `.warning` are considered equal.

In CSS 3, the asterisk may be used in combination with namespaces:

- `ns|*` - matches all elements in namespace ns
- `*|*` - matches all elements
- `|*` - matches all elements without any declared namespace

CSS

```css
* [lang^=en] {
  color:green;
}

*.warning {
  color:red;
}

*#maincontent {
  border: 1px solid blue;
}
```

HTML

```html
<p class="warning">
  <span lang="en-us">A green span</span> in a red paragraph.
</p>
<p id="maincontent" lang="en-gb">
  <span class="warning">A red span</span> in a green paragraph.
</p>
```

------



## [Attribute selectors (属性选择器)](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors)

Attribute selectors select an element using the presence of a given attribute or attribute value.

属性选择器通过已经存在的属性名或属性值匹配元素。

- `[*attr*]`

  Represents an element with an attribute name of attr.

  表示带有以 attr 命名的属性的元素。

  ​

- `[*attr*=*value*]`

  Represents an element with an attribute name of attr and whose value is exactly "value".

  表示带有以 attr 命名的，且值为"value"的属性的元素。

  ​

- `[*attr*~=*value*]`

  Represents an element with an attribute name of attr whose value is a whitespace-separated list of words, one of which is exactly "value".

  表示带有以 attr 命名的属性的元素，并且该属性是一个以空格作为分隔的值列表，其中至少一个值为"value"。

  ​

- `[*attr*|=*value*]`

  Represents an element with an attribute name of attr. Its value can be exactly “value” or can begin with “value” immediately followed by “-” (U+002D). It can be used for language subcode matches.

  表示带有以 attr 命名的属性的元素，并且该属性是一个以空格作为分隔的值列表，其中至少一个值为"value"或者至少一个值以"value-"（"-"为连字符，Unicode编码为U+002D）开头。典型的应用场景是用来来匹配语言简写代码（如zh-CN，zh-TW可以用zh作为value）。

  ​

- `[*attr*^=*value*]`

  Represents an element with an attribute name of attr and whose first value is prefixed by "value".

  表示带有以 attr 命名的，且值是以"value"开头的属性的元素。

  ​

- `[*attr*$=*value*]`

  Represents an element with an attribute name of attr and whose last value is suffixed by "value".

  表示带有以 attr 命名的，且值是以"value"结尾的属性的元素。

  ​

- `[*attr**=*value*]`

  Represents an element with an attribute name of attr and whose value contains at least one occurrence of string "value" as substring.

  表示带有以 attr 命名的，且值包含有"value"的属性的元素

  ​

- `[*attr* *operator* *value* i]`

  Adding an `i` (or `I`) before the closing bracket causes the value to be compared case-insensitively (for characters within the ASCII range).

  在带有属性值的属性选型选择器表达式的右括号（]括号）前添加**用空格间隔开**的字母i（或I）可以忽略属性值的大小写（ASCII字符范围内的字母）

CSS

```css
/* 所有具有"lang"属性的 span 元素的字体加粗 */
/* All spans with a "lang" attribute are bold */
span[lang] {font-weight:bold;}
 
/* 所有具有"lang"属性,且值为"pt"的 span 元素的字体为绿色 */
/* All spans in Portuguese are green */
span[lang="pt"] {color:green;}

/* 所有具有"lang"属性,且值为"en-us"的 span 元素的字体为蓝色*/
/* All spans in US English are blue  */
span[lang~="en-us"] {color: blue;}

/* 任意具有"lang"属性,且值带有"zh"字符串的 span 元素的字体为红色, 它会匹配简体中文(zh-CN)以及繁体中文(zh-TW) */
/* Any span in Chinese is red, matches simplified (zh-CN) or traditional (zh-TW) */
span[lang|="zh"] {color: red;}

/* 所有内部链接背景都为金色 */
/* All internal links have a gold background */
a[href^="#"] {background-color:gold}

/* All spans whose first declared class begins with "main" have a yellow background */
/* Span with the class="banner main" would not be affected. */
span[class^="main"] {background-color: yellow;}

/* 所有以".cn"结尾的链接字体都为红色 */
/* All links to urls ending in ".cn" are red */
a[href$=".cn"] {color: red;}

/* 所有带有"example"的链接背景都为灰色 */
/* All links with "example" in the url have a grey background */
a[href*="example"] {background-color: #CCCCCC;}

/*所有email输入框的边框都为蓝色*/
/*这里匹配的输入框类型"emeil"可以忽略其大小写，比如 "email"，"EMAIL"，"eMaiL"等等都能匹配*/
/* All email inputs have a blue border */
/* This matches any capitalization of
   "email", e.g. "email", "EMAIL", "eMaIL", etc. */
input[type="email" i] {border-color: blue;}
```

HTML

```html
<div class="hello-example">
    <a href="http://example.com">English:</a>
    <span lang="en-us en-gb en-au en-nz">Hello World!</span>
</div>
<div class="hello-example">
    <a href="#portuguese">Portuguese:</a>
    <span lang="pt">Olá Mundo!</span>
</div>
<div class="hello-example">
    <a href="http://example.cn">Chinese (Simplified):</a>
    <span lang="zh-CN">世界您好！</span>
</div>
<div class="hello-example">
    <a href="http://example.cn">Chinese (Traditional):</a>
    <span lang="zh-TW">世界您好！</span>
</div>
```

------



## [Adjacent sibling selectors (相邻兄弟选择器)](https://developer.mozilla.org/en-US/docs/Web/CSS/Adjacent_sibling_selectors)

This is referred to as an adjacent selector or next-sibling selector. It will select only the specified element that immediately follows the former specified element.

**Syntax**

```css
former_element + target_element { style properties }
```

CSS

```css
li + li {
  color: red;
}
```

HTML

```html
<ul>
  <li>One</li>
  <li>Two</li>
  <li>Three</li>
</ul>
```

另一个示例就是紧跟 <img>元素后的"captioin span"的样式 :

CSS

```css
img + span.caption {
  font-style: italic;
}
```

当上面的CSS作用于下面的HTML后,它会匹配下面的 <span> 元素:

HTML

```html
<img src="photo1.jpg"><span class="caption">The first photo</span>
<img src="photo2.jpg"><span class="caption">The second photo</span>
```

------



## [General sibling selectors (通用兄弟选择器)](https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_selectors)

The `~` combinator separates two selectors and matches the second element only if it is preceded by the first, and both share a common parent.

在使用 ~ 连接两个元素时,它会匹配第二个元素,条件是它必须跟(不一定是紧跟)在第一个元素之后,且他们都有一个共同的父元素 .

**Syntax**

```css
element ~ element { style properties }
```

CSS

```css
p ~ span {
  color: red;
}
```

HTML

```html
<span>This is not red.</span>
<p>Here is a paragraph.</p>
<code>Here is some code.</code>
<span>And here is a span.</span>
<code>More code...</code>
<span>And this is also red.</span>
```

------



## [Child selectors (子选择器)](https://developer.mozilla.org/en-US/docs/Web/CSS/Child_selectors)

The `>` combinator separates two selectors and matches only those elements matched by the second selector that are **direct** **children** of elements matched by the first. By contrast, when two selectors are combined with the [descendant selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Descendant_selectors), the combined selector expression matches those elements matched by the second selector for which there exists an ancestor element matched by the first selector, regardless of the number of "hops" up the DOM.

当使用  `>` 选择符分隔两个元素时,它只会匹配那些作为第一个元素的**直接后代(**子元素)的第二元素. 与之相比, 当两个元素由 [后代选择器 ](https://developer.mozilla.org/en/CSS/Descendant_selectors)相连时, 它表示匹配存在的所有由第一个元素作为祖先元素(但不一定是父元素)的第二个元素, 无论它在 DOM 中"跳跃" 多少次.

**Syntax**

```css
selector1 > selector2 { style properties }
```

CSS

```css
span { background-color: white; }
div > span {
  background-color: DodgerBlue;
}
```

HTML

```html
<div>
  <span>Span #1, in the div.
    <span>Span #2, in the span that's in the div.</span>
  </span>
</div>
<span>Span #3, not in the div at all.</span>
```

------



## [Descendant selectors (后代选择器)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Descendant_selectors)

The **descendant combinator** — typically represented by a single space ( ) character — combines two selectors such that elements matched by the second selector are selected if they have an ancestor element matching the first selector. Selectors that utilize a descendant combinator are called descendant selectors.

The descendant combinator is technically one or more CSS white space characters — the space character and/or one of four control characters: carriage return, form feed, new line, and tab characters — between two selectors in the absence of another combinator. Additionally, the white space characters of which the combinator is comprised may contain any number of CSS comments.

The abstract nature of this combinator makes it different from the other standardized combinators as these combinators are all represented by a distinct, finite character sequence. This inconsistency was addressed with the addition of a redundant descendant combinator represented by two greater‐than characters in sequence (`>>`), giving it a form that is particularly similar to the [child combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Child_selectors), which shares a similar function.

当使用 `␣` 选择符 (这里代表一个空格,更确切的说是一个或多个的空白字符) 连接两个元素时使得该选择器可以**只匹配那些由第一个元素作为祖先元素的所有第二个元素(后代元素)** . 后代选择器与 [子选择器](https://developer.mozilla.org/en/CSS/Child_selectors) 很相似, 但是**后代选择器不需要相匹配元素之间要有严格的父子关系**.

**Syntax**

```css
selector1 selector2 { /* property declarations */ }
```

```css
selector1 >> selector2 { /* property declarations */ }
```

CSS

```css
span { background-color: white; }
div span { background-color: DodgerBlue; }
```

HTML

```html
<div>
  <span>Span 1.
    <span>Span 2.</span>
  </span>
</div>
<span>Span 3.</span>
```

>**Desktop**
>
>| Feature       | Chrome     | Firefox (Gecko) | Internet Explorer | Opera      | Safari |
>| ------------- | ---------- | --------------- | ----------------- | ---------- | ------ |
>| Basic support | (Yes)      | (Yes)           | (Yes)             | (Yes)      | (Yes)  |
>| `>>` form     | No support | No support      | No support        | No support | 10     |















## CSS_Class

### CSS 类选择器

HTML 代码

```html
<h1 class="apple">
This heading is very important.
</h1>

<p class="apple">
This paragraph is very important.
</p>
```

匹配 class 属性包含 apple 的所有 p 元素

```css
p.apple {color:red;}
```



