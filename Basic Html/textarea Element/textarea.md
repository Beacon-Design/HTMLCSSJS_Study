# `<textarea>`

`<textarea>` 标签定义一个多行的文本输入控件。

文本区域中可容纳无限数量的文本，其中的文本的默认字体是等宽字体（通常是 Courier）。

可以通过 cols 和 rows 属性来规定 textarea 的尺寸大小，不过更好的办法是使用 CSS 的 height 和 width 属性。

**DOM interface :**

HTML TextAreaElement

**Inheritance Hierarchy :**

 Node  <==  Element  <==  HTMLElement  <==  HTMLTextAreaElement



## Attribute / 属性

`<textarea>` 标签支持 [HTML 的全局属性](http://www.runoob.com/tags/ref-standardattributes.html) , [HTML 的事件属性](http://www.runoob.com/tags/ref-eventattributes.html)。



HTML5 中的新属性: (H5)

| 属性                                       | 值         | 描述                       |
| ---------------------------------------- | --------- | ------------------------ |
| [autofocus](http://www.runoob.com/tags/att-textarea-autofocus.html) (H5) | autofocus | 规定当页面加载时，文本区域自动获得焦点。     |
| [cols](http://www.runoob.com/tags/att-textarea-cols.html) | *number*  | 规定文本区域内可见的列数。            |
| [disabled](http://www.runoob.com/tags/att-textarea-disabled.html) | disabled  | 规定禁用文本区域。                |
| [form](http://www.runoob.com/tags/att-textarea-form.html) (H5) | *form_id* | 定义文本区域所属的一个或多个表单。        |
| [maxlength](http://www.runoob.com/tags/att-textarea-maxlength.html) (H5) | *number*  | 规定文本区域允许的最大字符数。          |
| [name](http://www.runoob.com/tags/att-textarea-name.html) | *text*    | 规定文本区域的名称。               |
| [placeholder](http://www.runoob.com/tags/att-textarea-placeholder.html) (H5) | *text*    | 规定一个简短的提示，描述文本区域期望的输入值。  |
| [readonly](http://www.runoob.com/tags/att-textarea-readonly.html) | readonly  | 规定文本区域为只读。               |
| [required](http://www.runoob.com/tags/att-textarea-required.html) (H5) | required  | 规定文本区域是必需的/必填的。          |
| [rows](http://www.runoob.com/tags/att-textarea-rows.html) | *number*  | 规定文本区域内可见的行数。            |
| [wrap](http://www.runoob.com/tags/att-textarea-wrap.html) (H5) | hardsoft  | 规定当提交表单时，文本区域中的文本应该怎样换行。 |





## Attribute :

### autofocus (H5)

> **autofocus**
>
> This Boolean attribute lets you specify that a form control should have input focus when the page loads, unless the user overrides it, for example by typing in a different control. Only one form-associated element in a document can have this attribute specified. 
>
> *boolean* : Returns / Sets the element's `autofocus` attribute, indicating that the control should have input focus when the page loads

#### 浏览器支持 :

Internet Explorer 10、Firefox、Opera、Chrome 和 Safari 支持 autofocus 属性。

**注意：**Internet Explorer 9 及之前的版本支持 `<textarea>` 标签的 autofocus 属性。

#### 定义和用法 :

autofocus 属性是一个布尔属性。

autofocus 属性规定文本区域应该在页面加载时自动获得焦点。

autofocus 属性是 HTML5 中 `<textarea>` 标签的新属性。

在 XHTML 中，禁止属性最小化，autofocus 属性必须定义为 `<textarea autofocus="autofocus">`。

#### 语法 :

```
<textarea autofocus>
```

#### Example:

```html
<!--textarea autofocus-->
<textarea autofocus>&lt;textarea autofocus&gt; (H5)</textarea>
```



### cols

> **cols**
>
> The visible width of the text control, in average character widths. If it is specified, it must be a positive integer. If it is not specified, the default value is 20 (HTML5).
>
> *unsigned long* : Returns / Sets the element's `cols` attribute, indicating the visible width of the text area.

#### 浏览器支持 :

所有主流浏览器都支持 cols 属性。

**注意：** textarea 的尺寸大小也可以通过 CSS 的 height 和 width 属性设置。

#### 语法 :

```
<textarea cols="*number*">
```

#### 属性值:

| 值        | 描述                           |
| -------- | ---------------------------- |
| *number* | 规定文本区域的宽度（以平均字符宽度计）。默认值是 20。 |

#### Example:

```html
<!--textarea cols-->
<textarea cols="30">&lt;textaera cols&gt;</textarea>
```



### disabled

> **disabled**
>
> This Boolean attribute indicates that the user cannot interact with the control. (If this attribute is not specified, the control inherits its setting from the containing element, for example `<firldset>`; if there is no containing element with the `disabled`attribute set, then the control is enabled.)
>
> *boolean* : Returns / Sets the element's `disabled` attribute, indicating that the control is not available for interaction.

#### 浏览器支持 :

所有主流浏览器都支持 disabled 属性。

#### 定义和用法 :

disabled 属性是一个布尔属性。

disabled 属性规定文本区域应该被禁用。

被禁用的文本区域既不可用，文本也不可选择（不能被复制）。

可以设置 disabled 属性，直到满足某些条件（比如选择一个复选框），才恢复用户对该文本区域的使用。然后，可以使用 JavaScript 来移除 disabled 属性的值，以使文本区域变为可用状态。

#### HTML 与 XHTML 之间的差异 :

在 XHTML 中，禁止属性最小化，disabled 属性必须定义为 `<textarea disabled="disabled">`。

#### 语法 :

```
<textarea disabled>
```

#### Example:

```html
<!--textarea disable-->
<textarea disabled>&lt;textarea disable&gt;</textarea>
```



### form (H5)

> **form** 
>
> The form element that the textarea element is associated with (its "form owner"). The value of the attribute must be an ID of a form element in the same document. If this attribute is not specified, the textarea element must be a descendant of a form element. This attribute enables you to place textarea elements anywhere within a document, not just as descendants of their form elements.
>
> *object* : Returns a reference to the parent form element. If this element is not contained in a form element, it can be the `id` attribute of any `<form>` element in the same document or the value `null`.

#### 浏览器支持 :

除了 Internet Explorer，其他主流浏览器都支持 form 属性。

#### 定义和用法 :

form 属性规定文本区域所属的一个或多个表单。

form 属性是 HTML5 中的新属性。

#### 语法 :

```
<textarea form="form_id">
```

#### 属性值 :

| 值         | 描述                             |
| --------- | ------------------------------ |
| *form_id* | 规定文本区域所属的一个或多个表单的 id 列表，以空格分隔。 |

#### Example:

```html
<!--textarea form-->
<form action="" id="userform"><textarea form="user_form">&lt;textarea form&gt; (H5)</textarea></form>
```



### maxlength (H5)

> **maxlength** 
>
> The maximum number of characters (Unicode code points) that the user can enter. If it is not specified, the user can enter an unlimited number of characters.
>
> *long* : Returns / Sets the element's `maxlength` attribute, indicating the maximum number of characters the user can enter. This constraint is evaluated only when the value changes.

#### 浏览器支持 :

Internet Explorer 10、Firefox、Chrome 和 Safari 支持 maxlength 属性。

**注意：**Opera 或者 Internet Explorer 9 及之前的版本不支持 `<textarea>` 标签的 maxlength 属性。

除了 Internet Explorer 和 Opera，其他主流浏览器都支持 maxlength 属性。

#### 定义和用法 :

maxlength 属性规定文本区域的最大长度（以字符计）。

maxlength 属性是 HTML5 中的 `<textarea>` 标签的新属性。

#### 语法 :

```
<textarea maxlength="number">
```

#### 属性值 :

| 值        | 描述              |
| -------- | --------------- |
| *number* | 在文本区域中允许的最大字符数。 |

#### Example:

```html
<!--textarea maxlength-->
<textarea maxlength="30">&lt;textarea maxlength&gt; (H5)</textarea>
```



### name

> **name**
>
> The name of the control.
>
> *string* : Returns / Sets the element's `name` attribute, containing the name of the control.

#### 浏览器支持 :

所有主流浏览器都支持 name 属性。

#### 定义和用法 :

name 属性为文本区域规定名称。

name 属性用于在 JavaScript 中对元素进行引用，或者在表单提交之后，对表单数据进行引用。

#### 语法 :

```
<textarea name="text">
```

#### 属性值 :

| 值      | 描述         |
| ------ | ---------- |
| *text* | 规定文本区域的名称。 |

#### Example:

```html
<!--textarea name-->
<textarea name="n1">&lt;textarea name&gt;</textarea>
```



### placeholder (H5)

> **placeholder** 
>
> A hint to the user of what can be entered in the control. Carriage returns or line-feeds within the placeholder text must be treated as line breaks when rendering the hint.
>
> *string* : Returns / Sets the element's `placeholder` attribute, containing a hint to the user about what to enter in the control.

#### 浏览器支持 :

Internet Explorer 10、Firefox、Opera、Chrome 和 Safari 支持 placeholder 属性。

**注意：**Internet Explorer 9 及之前的版本不支持 `<textarea>` 标签的 placeholder 属性。

#### 定义和用法 :

placeholder 属性规定一个简短的提示，它描述了文本区域的期望值。

当文本区域为空，且当字段获得焦点后又失去焦点时，文本区域中显示该提示.

placeholder 属性是 HTML5 中的新属性。

#### 语法 :

```
<textarea placeholder="text">
```

#### 属性值 :

| 值      | 描述                    |
| ------ | --------------------- |
| *text* | 规定一个简短的提示，描述文本区域的期望值。 |

#### Example:

```html
<!--textarea placeholder-->
<textarea placeholder="&lt;textarea placeholder&gt; (H5)"></textarea>
```



### readonly

> **readonly**
>
> This Boolean attribute indicates that the user cannot modify the value of the control. Unlike the `disabled` attribute, the `readonly` attribute does not prevent the user from clicking or selecting in the control. The value of a read-only control is still submitted with the form.
>
> *boolean*: Returns / Sets the element's `readonly` attribute, indicating that the user cannot modify the value of the control.

#### 浏览器支持 :

所有主流浏览器都支持 readonly 属性。

#### 定义和用法 :

readonly 属性是一个布尔属性。

readonly 属性规定文本区域为只读。

在只读的文本区域中，无法对内容进行修改，但用户可以通过 tab 键切换到该控件，选取或复制其中的内容。

可以设置 readonly 属性，直到满足某些条件（比如选择一个复选框），才恢复用户对该文本区域的使用。然后，可以使用 JavaScript 来移除 readonly 属性的值，以使文本区域变为可编辑状态。

#### HTML 与 XHTML 之间的差异 :

在 XHTML 中，禁止属性最小化，readonly 属性必须定义为 `<textarea readonly="readonly">`。

#### 语法 :

```
<textarea readonly>
```

#### Example:

```html
<!--textarea readonly-->
<textarea readonly>&lt;textarea readonly&gt;</textarea>
```



### required (H5)

> **required** 
>
> This attribute specifies that the user must fill in a value before submitting a form.
>
> *boolean* : Returns / Sets the element's `required` attribute, indicating that the user must specify a value before submitting the form.

#### 浏览器支持 : 

除了 Internet Explorer 和 Safari，其他主流浏览器都支持 required 属性。

#### 定义和用法 :

required 属性是一个布尔属性。

required 属性规定一个文本区域是必需的/必须填写（以提交表单）。

required 属性是 HTML5 中的新属性。

#### HTML 与 XHTML 之间的差异

在 XHTML 中，禁止属性最小化，required 属性必须定义为 `<textarea required="required">`。

#### 语法 :

```
<textarea required>
```

#### Example:

```html
<!--textarea required-->
<form action=""><textarea require>&lt;textarea requred&gt; (H5)</textarea></form>
```



### rows

> **rows**
>
> The number of visible text lines for the control.
>
> *unsigned long* : Returns / Sets the element's `rows` attribute, indicating the number of visible text lines for the control.

#### 浏览器支持 :

所有主流浏览器都支持 rows 属性。

#### 定义和用法 :

rows 属性规定文本区域的可见高度，以行数计。

**注意：** textarea 的尺寸大小也可以通过 CSS 的 height 和 width 属性设置。

#### 语法 :

```
<textarea rows="number">
```

#### 属性值 :

| 值        | 描述                      |
| -------- | ----------------------- |
| *number* | 规定文本区域的高度（以行数计）。默认值是 2。 |

#### Example:

```html
<!--textarea rows-->
<textarea rows="4">&lt;textarea rows&gt;</textarea>
```



### wrap (H5)

> **wrap**
>
> Indicates how the control wraps text. Possible values are:
>
> - hard: The browser automatically inserts line breaks (CR+LF) so that each line has no more than the width of the control; the `cols` attribute must be specified.
> - soft: The browser ensures that all line breaks in the value consist of a CR+LF pair, but does not insert any additional line breaks.
>
> If this attribute is not specified, soft is its default value.
>
> *string* : Returns / Sets the `wrap` HTML attribute, indicating how the control wraps text.

#### 浏览器支持 :

所有主流浏览器都支持 wrap 属性。

#### 定义和用法 :

wrap 属性规定在表单提交时文本区域中的文本是如何换行的。

wrap 属性是 HTML5 中 `<textarea>` 标签的新属性。

#### 语法 :

```
<textarea wrap="soft|hard">
```

#### 属性值 :

| 值    | 描述                                       |
| ---- | ---------------------------------------- |
| soft | 在表单提交时，textarea 中的文本不换行。默认。              |
| hard | 在表单提交时，textarea 中的文本换行（包含换行符）。当使用 "hard" 时，必须指定 cols 属性。 |

#### Example:

```html
<!--textarea wrap-->
<form action="" name="wr">
  <textarea name="wr" wrap="soft">&lt;textarea wrap&gt; (H5)</textarea>
</form>
```