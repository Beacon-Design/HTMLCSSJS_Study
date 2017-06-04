## HTML 全局属性

> HTML5新增属性: (H5)

| 属性                                       | 描述                            |
| ---------------------------------------- | ----------------------------- |
| [accesskey](http://www.runoob.com/tags/att-global-accesskey.html) | 设置访问元素的键盘快捷键。                 |
| [class](http://www.runoob.com/tags/att-global-class.html) | 规定元素的类名（classname）            |
| [contenteditable](http://www.runoob.com/tags/att-global-contenteditable.html) (H5) | 规定是否可编辑元素的内容。                 |
| [contextmenu](http://www.runoob.com/tags/att-global-contextmenu.html) (H5) | 指定一个元素的上下文菜单。当用户右击该元素，出现上下文菜单 |
| [data-*](http://www.runoob.com/tags/att-global-data.html) (H5) | 用于存储页面的自定义数据                  |
| [dir](http://www.runoob.com/tags/att-global-dir.html) | 设置元素中内容的文本方向。                 |
| [draggable](http://www.runoob.com/tags/att-global-draggable.html) (H5) | 指定某个元素是否可以拖动                  |
| [dropzone](http://www.runoob.com/tags/att-global-dropzone.html) (H5) | 指定是否将数据复制，移动，或链接，或删除          |
| [hidden](http://www.runoob.com/tags/att-global-hidden.html) (H5) | hidden 属性规定对元素进行隐藏。           |
| [id](http://www.runoob.com/tags/att-global-id.html) | 规定元素的唯一 id                    |
| [lang](http://www.runoob.com/tags/att-global-lang.html) | 设置元素中内容的语言代码。                 |
| [spellcheck](http://www.runoob.com/tags/att-global-spellcheck.html) (H5) | 检测元素是否拼写错误                    |
| [style](http://www.runoob.com/tags/att-global-style.html) | 规定元素的行内样式（inline style）       |
| [tabindex](http://www.runoob.com/tags/att-global-tabindex.html) | 设置元素的 Tab 键控制次序。              |
| [title](http://www.runoob.com/tags/att-global-title.html) | 规定元素的额外信息（可在工具提示中显示）          |
| [translate](http://www.runoob.com/tags/att-global-translate.html) (H5) | 指定是否一个元素的值在页面载入时是否需要翻译        |



## accesskey

> **accesskey**
>
> Provides a hint for generating a keyboard shortcut for the current element. This attribute consists of a space-separated list of characters. The browser should use the first one that exists on the computer keyboard layout.

#### 浏览器支持 :

所有主流浏览器都支持 accesskey 属性

#### 定义和用法 :

accesskey 属性规定激活（使元素获得焦点）元素的快捷键。

**注意：** 在不同操作系统中不同的浏览器中访问快捷键的方式不同：

| Browser           | Windows                                  | Linux                         | Mac                             |
| ----------------- | ---------------------------------------- | ----------------------------- | ------------------------------- |
| Internet Explorer | [Alt] + *accesskey*                      | N/A                           |                                 |
| Chrome            | [Alt] + *accesskey*                      | [Alt] + *accesskey*           | [Control] + [Alt] + *accesskey* |
| Firefox           | [Alt] + [Shift] + *accesskey*            | [Alt] + [Shift] + *accesskey* | [Control] + [Alt] + *accesskey* |
| Safari            | [Alt] + *accesskey*                      | N/A                           | [Control] + [Alt] + *accesskey* |
| Opera             | Opera 15 or newer: [Alt] + *accesskey*Opera 12.1 or older: [Shift] + [Esc] + *accesskey* | same                          | same                            |

但是，在大多浏览器中快捷键可以设置为另外一组组合。

**提示：** 各种浏览器下accesskey快捷键的使用方法：

**IE浏览器**

按住Alt键，点击accesskey定义的快捷键(焦点将移动到链接)，再按回车.

**FireFox浏览器**

按住Alt+Shift键，点击accesskey定义的快捷键.

**Chrome浏览器**

按住Alt键，点击accesskey定义的快捷键.

**Opera浏览器**

按住Shift键，点击esc，出现本页定义的accesskey快捷键列表可供选择.

**Safari浏览器**

按住Alt键，点击accesskey定义的快捷键.

在 HTML5 中, accesskey 属性可用于任何 HTML 元素 (它会 验证任何HTML元素。但不一定是有用)。

在 HTML 4.01 中, accesskey 属性可使用于: `<a>` , `<area>` , `<button>` , `<input>` , `<label>` , `<legend>`, 和 `<textarea>`。

#### 语法 :

```html
<element accesskey="character">
```

#### 属性值 :

| 值           | 描述         |
| ----------- | ---------- |
| c*haracter* | 指定激活元素的快捷键 |



## class

> **class**
>
> Is a space-separated list of the classes of the element. Classes allows CSS and JavaScript to select and access specific elements via the class selectors or functions like the method `Document.getElementsByClassName()`.

#### 浏览器支持 :

所有主流浏览器都支持 class 属性

#### 定义和用法 :

class 属性定义了元素的类名。

class 属性通常用于指向样式表的类。但是，它也可以用于 JavaScript 中（通过 HTML DOM）, 来修改 HTML 元素的类名。

在 HTML5 中, class 属性可用于任何的 HTML 元素 (它会 验证任何HTML元素。但不一定是有用)。

在 HTML 4.01 中, class 属性不能用于: `<base>` , `<head>` , `<html>` , `<meta>` , `<param>` , `<script>` , `<style>` , 和 `<title>`。

#### 语法 :

```html
<element class="classname">
```

#### 属性值 :

| 值           | 描述                                       |
| ----------- | ---------------------------------------- |
| *classname* | 规定元素的类的名称。如需为一个元素规定多个类，用空格分隔类名。 `<span class="left important">`. HTML 元素允许使用多个类。名称规则：1. 必须以字母 A-Z 或 a-z 开头。 2. 可以是以下字符： (A-Za-z), 数字 (0-9), 横杆 ("-"), 和 下划线 ("_")。 3.在 HTML 中, 类名是区分大小写的。 |



## contenteditable (H5)

> **contenteditable**
>
> Is an enumerated attribute indicating if the element should be editable by the user. If so, the browser modifies its widget to allow editing. The attribute must take one of the following values:
>
> - `true` or the *empty string*, which indicates that the element must be editable;
>
>
> - `false`, which indicates that the element must not be editable.
>
> If this attribute is not set, its default value is *inherited* from its parent element.
>
> This attribute is an *enumerated* one and not a Boolean one. This means that the explicit usage of one of the values `true`, `false` or the empty string is mandatory and that a shorthand like `<label contenteditable>Example Label</label>` is not allowed. The correct usage is `<label contenteditable="true">Example Label</label>`.

#### 浏览器支持 :

所有主流浏览器都支持 contenteditable 属性

#### 定义和用法 :

contenteditable 属性指定元素内容是否可编辑。

**注意：** 当元素中没有设置 contenteditable 属性时，元素将从父元素继承。

contenteditable 属性是 HTML5 新增的。

#### 语法 :

```html
<element contenteditable="true|false">
```

#### 属性值 :

| 值     | 描述         |
| ----- | ---------- |
| true  | 指定元素是可编辑的  |
| false | 指定元素是不可编辑的 |



## contextmenu (H5)

> **contextmenu**
>
> Is the `id` of an `<menu>` to use as the contextual menu for this element.

#### 浏览器支持 :

目前只有 Firefox 浏览器支持 contextmenu 属性。

#### 定义和用法 :

contextmenu 属性规定了元素的上下文菜单。当用户右击元素时将显示上下文菜单。

contextmenu 属性的值是需要打开的 `<menu>` 元素的 id。

contextmenu 属性是 HTML5 中的新属性。

#### 语法 :

```html
<element contextmenu="menu_id">
```

#### 属性值 :

| 值         | 描述                    |
| --------- | --------------------- |
| *menu_id* | 要打开的 `<menu>` 元素的 id。 |



## data-* (H5)

> **data-***
>
> Forms a class of attributes, called custom data attributes, that allow proprietary information to be exchanged between the `HTML` and its `DOM` representation that may be used by scripts. All such custom data are available via the `HTMLElement`interface of the element the attribute is set on. The `HTMLElement.dataset` property gives access to them.
>
> The `*` may be replaced by any name following the production rule of xml names with the following restrictions:
>
> - the name must not start with `xml`, whatever case is used for these letters;
> - the name must not contain any semicolon (`U+003A`);
> - the name must not contain capital `A` to `Z` letters.
>
> Note that the `HTMLElement.dataset` property is a `DOMStringMap`, and the name of the custom data attribute *data-test-value* will be accessible via `HTMLElement.dataset.testValue `( or` HTMLElement.dataset["testValue"] `) as any dash (`U+002D`) is replaced by the capitalization of the next letter, converting the name to camelcase.

#### 浏览器支持 :

所有主流浏览器都支持 data-* 属性。

#### 定义和用法 :

data-* 属性用于存储私有页面后应用的自定义数据。

data-* 属性可以在所有的 HTML 元素中嵌入数据。

自定义的数据可以让页面拥有更好的交互体验（不需要使用 Ajax 或去服务端查询数据）。

data-* 属性由以下两部分组成：

1. 属性名不要包含大写字母，在 data- 后必须至少有一个字符。
2. 该属性可以是任何字符串

**注意：** 自定义属性前缀 "data-" 会被客户端忽略。

data-* 属性是 HTML5 新增的。

#### 语法 :

```html
<element data-="somevalue*">
```

#### 属性值 :

| 值           | 描述            |
| ----------- | ------------- |
| *somevalue* | 指定属性值 (一个字符串) |



## dir

> **dir**
>
> - `ltr`, which means left to right and is to be used for languages that are written from the left to the right (like English);
> - `rtl`, which means *right to left* and is to be used for languages that are written from the right to the left (like Arabic);
> - `auto`, which let the user agent decides. It uses a basic algorithm as it parses the characters inside the element until it finds a character with a strong directionality, then apply that directionality to the whole element.

#### 浏览器支持 :

所有主流浏览器都支持 dir 属性

#### 定义和用法 :

dir 属性规定元素内容的文本方向。

在 HTML5 中, dir 属性可用于任何的 HTML 元素 (它会验证任何HTML元素。但不一定是有用)。

在 HTML 4.01 中, dir 元素不能用于: `<base>` , `<br>` , `<frame>` , `<frameset>` , `<hr>` , `<iframe>` , `<param>` , 和 `<script>`。

#### 语法 :

```html
<element dir="ltr|rtl|auto">
```

#### 属性值 :

| 值    | 描述                             |
| ---- | ------------------------------ |
| ltr  | 默认。从左向右的文本方向。                  |
| rtl  | 从右向左的文本方向。                     |
| auto | 让浏览器根据内容来判断文本方向。仅在文本方向未知时推荐使用。 |



# draggable (H5)

> **draggable** 
>
> Is an enumerated attribute indicating whether the element can be dragged, using the [Drag and Drop API](https://developer.mozilla.org/en-us/docs/DragDrop/Drag_and_Drop). It can have the following values:
>
> - `true`, which indicates that the element may be dragged
> - `false`, which indicates that the element may not be dragged.
>
> If this attribute is not set, its default value is `auto`, meaning the behavior should be the one defined by default by the browser.
>
> This attribute is an *enumerated* one and not a *Boolean* one. This means that the explicit usage of one of the values `true` or `false` is mandatory and that a shorthand like `<label draggable>Example Label</label>`is not allowed. The correct usage is `<label draggable="true">Example Label</label>`.
>
> By default, only text selections, images, and links can be dragged. For all others elements, the event `ondragstart` must be set for the drag and drop mechanism to work, as shown in this [comprehensive example](https://developer.mozilla.org/en-US/docs/DragDrop/Drag_Operations).

#### 浏览器支持 :

Internet Explorer 9+, Firefox, Opera, Chrome, 和 Safari 浏览器支持 draggable 属性。

**注意：** Internet Explorer 8 及更早 IE 版本不支持 draggable 属性。

#### 定义和用法 :

draggable 属性规定元素是否可拖动。

**提示：** 链接和图像默认是可拖动的。

**提示：** draggable 属性经常用于拖放操作。

draggable 属性是 HTML5 新增的。

#### 语法 :

```html
<element draggable="true|false|auto">
```

#### 属性值 :

| 值     | 描述          |
| ----- | ----------- |
| true  | 规定元素是可拖动的。  |
| false | 规定元素是不可拖动的。 |
| auto  | 使用浏览器的默认特性。 |



## dropzone (H5)

> **dropzone** 
>
> Is an enumerated attribute indicating what types of content can be dropped on an element, using the [Drag and Drop API](https://developer.mozilla.org/en-US/docs/DragDrop/Drag_and_Drop). It can have the following values:
>
> - `copy`, which indicates that dropping will create a copy of the element that was dragged
> - `move`, which indicates that the element that was dragged will be moved to this new location.
> - `link`, will create a link to the dragged data.

没有主流浏览器支持 dropzone 属性。

#### 定义和用法 :

dropzone 属性规定当被拖动的数据在拖放到元素上时，是否被复制、移动或链接。

dropzone 属性是 HTML5 中的新属性。

#### 语法 :

```html
<element dropzone="copy|move|link">
```

#### 属性值 :

| 值    | 描述                 |
| ---- | ------------------ |
| copy | 拖动数据会导致被拖数据产生副本。   |
| move | 拖动数据会导致被拖数据移动到新位置。 |
| link | 拖动数据会生成指向原始数据的链接。  |



## hidden (H5)

> **hidden**
>
> Is a Boolean attribute indicates that the element is not yet, or is no longer, *relevant*. For example, it can be used to hide elements of the page that can't be used until the login process has been completed. The browser won't render such elements. This attribute must not be used to hide content that could legitimately be shown.
>
> The `hidden` attribute must not be used to hide content that could legitimately be shown in another presentation. For example, it is incorrect to use hidden to hide panels in a tabbed dialog, because the tabbed interface is merely a kind of overflow presentation — one could equally well just show all the form controls in one big page with a scrollbar. It is similarly incorrect to use this attribute to hide content just from one presentation — if something is marked hidden, it is hidden from all presentations, including, for instance, screen readers.
>
> Hidden elements shouldn't be linked from non-hidden elements and elements that are descendants of a hidden element are still active, which means that script elements can still execute and form elements can still submit.
>
> Elements and scripts may, however, refer to elements that are hidden in other contexts.
>
> For example, it would be incorrect to use the `href` attribute to link to a section marked with the `hidden` attribute. If the content is not applicable or relevant, then there is no reason to link to it.
>
> It would be fine, however, to use the ARIA `aria-describedby` attribute to refer to descriptions that are themselves hidden. While hiding the descriptions implies that they are not useful alone, they could be written in such a way that they are useful in the specific context of being referenced from the element that they describe.
>
> Similarly, a canvas element with the hidden attribute could be used by a scripted graphics engine as an off-screen buffer, and a form control could refer to a hidden form element using its form attribute.
>
> **Note:** Changing the value of the CSS [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/display) property on an element with the `hidden` attribute overrides the behavior. For instance, elements styled `display: flex` will be displayed despite the `hidden` attribute's presence.

#### 浏览器支持 :

所有主流浏览器都支持 hidden 属性，除了 Internet Explorer。

#### 定义和用法 :

hidden 属性规定对元素进行隐藏。

隐藏的元素不会被显示。

如果使用该属性，则会隐藏元素。

可以对 hidden 属性进行设置，使用户在满足某些条件时才能看到某个元素（比如选中复选框，等等）。然后，可使用 JavaScript 来删除 hidden 属性，使该元素变得可见。

hidden 属性是 HTML5 中的新属性。

#### HTML 与 XHTML 之间的差异 :

在 XHTML 中, 属性禁止简写，hidden 属性必须定义为 `<element hidden="hidden">`.

#### 语法 :

```html
<element hidden>
```



## id

> The **id** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes) defines a unique identifier (ID) which must be unique in the whole document. Its purpose is to identify the element when linking (using a fragment identifier), scripting, or styling (with CSS).
>
> This attribute's value is an opaque string: this means that web author must not use it to convey any information. Particular meaning, for example semantic meaning, must not be derived from the string.
>
> This attribute's value must not contain whitespace (spaces, tabs etc.). Browsers treat non-conforming IDs that contain whitespace as if the whitespace is part of the ID. In contrast to the **class** attribute, which allows space-separated values, elements can only have one single ID.
>
> **Note:** Using characters except ASCII letters and digits, `'_'`, `'-'` and `'.'` may cause compatibility problems, as they weren't allowed in HTML 4. Though this restriction has been lifted in HTML 5, an ID should start with a letter for compatibility.

#### 浏览器支持 :

所有主流浏览器都支持 id 属性

#### 定义和用法 :

id 属性规定 HTML 元素的唯一的 id。

id 在 HTML 文档中必须是唯一的。

id 属性可用作链接锚（link anchor），通过 JavaScript（HTML DOM）或通过 CSS 为带有指定 id 的元素改变或添加样式。

在 HTML5 中, id 属性可用于任何的 HTML 元素 (它会验证任何HTML元素。但不一定是有用)。

在 HTML 4.01 中, id 属性不能用于: `<base>`, `<head>`, `<html>`, `<meta>`, `<param>` , `<script>`, `<style>`, 和 `<title>`。

**注意:** HTML 4.01 对于 id 的值有严格的限制 (例如：在 HTML 4.01 id 值不能以数字开头)。

#### 语法 :

```html
<element id="id">
```

#### 属性值 :

| 值    | 描述                                       |
| ---- | ---------------------------------------- |
| *id* | 规定元素的唯一 id。命名规则：1. 必须以字母 A-Z 或 a-z 开头。 2. 其后的字符：字母(A-Za-z)、数字(0-9)、连字符("-")、下划线("_")、冒号(":") 以及点号(".")。3. 值对大小写敏感 |



## lang

> The **lang** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes) participates in defining the language of the element, the language that its non-editable elements are written in or the language that the editable elements should be written in. The tag contains one single entry value in the format defined in the [*Tags for Identifying Languages (BCP47)*](http://www.ietf.org/rfc/bcp/bcp47.txt) IETF document. If the tag content is the *empty string* the language is set to *unkn**own*; if the tag content is not valid, regarding BCP47, it is set to *invalid*.
>
> Even if the **lang** attribute is set, it may not be taken into account, as the [**xml:lang**](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/xml:lang) attribute has priority.
>
> For the CSS pseudo-class [`:lang`](https://developer.mozilla.org/en-US/docs/Web/CSS/:lang), two invalid language names are different if their names are different.

#### 浏览器支持 :

所有主流浏览器都支持 lang 属性

#### 定义和用法 :

lang 属性规定元素内容的语言。

在 HTML5 中, lang 属性可用于任何的 HTML 元素 (它会验证任何HTML元素。但不一定是有用)。

在 HTML 4.01 中, lang 属性不能用于: `<base>`, `<br>`, `<frame>`, `<frameset>`, `<hr>`, `<iframe>`, `<param>`, 和 `<script>`。

#### 语法 :

```html
<element lang="language_code">
```

#### 属性值 :

| 值               | 描述                                       |
| --------------- | ---------------------------------------- |
| *language_code* | 规定元素内容的语言代码。语言代码参考手册。 [语言代码参考手册](http://www.runoob.com/tags/html-language-codes.html) |



## spellcheck (H5)

> **spellcheck**
>
> - `true`, which indicates that the element should be, if possible, checked for spelling errors;
> - `false`, which indicates that the element should not be checked for spelling errors.

#### 浏览器支持 :

Internet Explorer 10, Firefox, Opera, Chrome, 和 Safari 浏览器支持 spellcheck 属性。

**注意：** Internet Explorer 9 及更早IE版本不支持 spellcheck 属性。

#### 定义和用法 :

spellcheck 属性规定是否对元素内容进行拼写检查。

可对以下文本进行拼写检查：

- 类型为 text 的 input 元素中的值（非密码）
- textarea 元素中的值
- 可编辑元素中的值

spellcheck 属性是 HTML5 新增的。

#### 语法 :

```html
<element spellcheck="true|false">
```

#### 属性值 :

| 值     | 描述                |
| ----- | ----------------- |
| true  | 规定应当对元素的文本进行拼写检查。 |
| false | 规定不应对元素的文本进行拼写检查。 |



## style

> **style**
>
> Contains [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) styling declarations to be applied to the element. Note that it is recommended for styles to be defined in a separate file or files. This attribute and the [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style) element have mainly the purpose of allowing for quick styling, for example for testing purposes.
>
> **Usage note: **This attribute must not be used to convey semantic information. Even if all styling is removed, a page should remain semantically correct. Typically it shouldn't be used to hide irrelevant information; this should be done using the [**hidden**](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/style#attr-hidden) attribute.

#### 浏览器支持 :

所有主流浏览器都支持 style 属性

#### 定义和用法 :

style 属性规定元素的行内样式（inline style）。

style 属性将覆盖任何全局的样式设定，例如在 `<style>` 标签或在外部样式表中规定的样式。

在 HTML5 中, style 属性可用于任何的 HTML 元素 (它会验证任何HTML元素。但不一定是有用)。

在 HTML 4.01中, style 属性不能用于: `<base>`, `<head>`, `<html>`, `<meta>`, `<param>`, `<script>`, `<style>`, 和 `<title>`。

#### 语法 :

```html
<element style="style_definitions">
```

#### 属性值 :

| 值                   | 描述                                       |
| ------------------- | ---------------------------------------- |
| *style_definitions* | 一个或多个由分号分隔的 CSS 属性和值。 (例如： `style="color:blue;text-align:center"`) |



## tabindex

> **tabindex**
>
> Is an integer attribute indicating if the element can take input focus (is *focusable*), if it should participate to sequential keyboard navigation, and if so, at what position. It can takes several values:
>
> - a *negative value* means that the element should be focusable, but should not be reachable via sequential keyboard navigation;
> - `0` means that the element should be focusable and reachable via sequential keyboard navigation, but its relative order is defined by the platform convention;
> - a *positive value* which means should be focusable and reachable via sequential keyboard navigation; its relative order is defined by the value of the attribute: the sequential follow the increasing number of the [**tabindex**](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes#attr-tabindex). If several elements share the same tabindex, their relative order follows their relative position in the document).
>
> An element with a `0` value, an invalid value, or no **tabindex** value should be placed after elements with a positive **tabindex** in the sequential keyboard navigation order.
>
> If we set the `tabindex` attribute on a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div), then its child content cannot be scrolled using arrow keys unless we set `tabindex` on the content too.[ Check out this fiddle to understand the scrolling effects of tabindex](https://jsfiddle.net/jainakshay/0b2q4Lgv/).
>
> **Note**: The maximum value for tabIndex should not exceed 32767. If not specified, it takes the default value -1.

#### 浏览器支持 :

所有主流浏览器都支持 tabindex 属性

#### 定义和用法 :

tabindex 属性规定当使用 "tab" 键进行导航时元素的顺序。

在 HTML5 中, tabindex 属性可用于任何的 HTML 元素 (它会验证任何HTML元素。但不一定是有用)。

在 HTML 4.01中, tabindex 属性可用于: `<a>`, `<area>`, `<button>`, `<input>`, `<object>`, `<select>`, 和 `<textarea>`。

#### 语法 :

```html
<element tabindex="number">
```

#### 属性值 :

| 值        | 描述                      |
| -------- | ----------------------- |
| *number* | 规定元素的 tab 键控制顺序（1 是第一）。 |



## title

> The **title** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes) contains text representing advisory information, related to the element it belongs to. This information can be typically, but not necessarily, presented to the user as a tooltip. Some typical uses:
>
> - Link: title or description of the linked document
> - Media element like an image: description or associated credits
> - Paragraph: footnote or a commentary about it
> - Quotation: information about the author, and so on.
>
> If this attribute is omitted, it means that the title of the nearest ancestor of this element is still relevant (and could be used as the tooltip for that element). If this attribute is set to the *empty string*, it explicitly means its nearest ancestor's title is not relevant (and shouldn't be used in the tooltip for this element).
>
> Additional semantics are attached to the **title** attributes of the [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link) , [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr) , [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) and [`<menuitem>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menuitem) elements.
>
> The **title** attribute may contain several lines. Each U+000A LINE FEED (LF) inserted represents such a newline. Some caution must be taken, as this means:
>
> ```html
> <p>Newlines in title should be taken into account,like this <abbr title="This is a
> multiline title">example</abbr>.</p>
> ```
>
> This example defines a two-line title.

#### 浏览器支持 :

所有主流浏览器都支持 title 属性

#### 定义和用法 :

title 属性规定关于元素的额外信息。

这些信息通常会在鼠标移到元素上时显示一段工具提示文本（tooltip text）。

在 HTML5 中, title 属性可用于任何的 HTML 元素 (它会验证任何HTML元素。但不一定是有用)。

在 HTML 4.01中, tabindex 属性不能用于: `<base>`, `<head>`, `<html>`, `<meta>`, `<param>`, `<script>`, `<style>`, 和 `<title>`。

#### 语法 :

```html
<element title="text">
```

#### 属性值 :

| 值      | 描述                         |
| ------ | -------------------------- |
| *text* | 规定元素的工具提示文本（tooltip text）。 |



## translate (H5)

> **translate**
>
> Is an enumerated attribute that is used to specify whether an element's attribute values and the values of its [Text](https://developer.mozilla.org/en-US/docs/Web/API/Text) node children are to be translated when the page is localized, or whether to leave them unchanged. It can have the following values:
>
> - empty string and `"yes"`, which indicates that the element will be translated.
> - `"no`", which indicates that the element will not be translated.  

目前没有主流浏览器支持 translate 属性。

#### 定义和用法 :

translate 属性规定元素内容是否要翻译。

**测试：使用 Google 翻译工具，查看以下单词 "ice cream" 会变成什么：**

这边我们使用 translate="no": ice cream.

这边我们使用 class="notranslate": ice cream.

**提示：** 使用 class="notranslate" 替代。

translate 属性是 HTML5 新增属性。

#### 语法 :

```html
<element translate="yes|no">
```

#### 属性值 :

| 值    | 描述          |
| ---- | ----------- |
| yes  | 规定元素内容需要翻译  |
| no   | 规定元素内容不需要翻译 |