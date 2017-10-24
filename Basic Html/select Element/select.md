

# HTML `<select>` 标签

select 元素可创建单选或多选菜单。

<select> 元素中的 [<option>](http://www.w3school.com.cn/tags/tag_option.asp) 标签用于定义列表中的可用选项。

提示：select 元素是一种表单控件，可用于在表单中接受用户输入。

```html
<form>
<select name="cars">
<option value="volvo">Volvo</option>
<option value="saab">Saab</option>
<option value="fiat">Fiat</option>
<option value="audi">Audi</option>
</select>
</form>
```



| 属性                                       | 值         | 描述                                       |
| ---------------------------------------- | :-------- | ---------------------------------------- |
| [autofocus](http://www.w3school.com.cn/tags/att_select_autofocus.asp) | autofocus | 规定在页面加载后文本区域自动获得焦点。                      |
| [disabled](http://www.w3school.com.cn/tags/att_select_disabled.asp) | disabled  | 规定禁用该下拉列表。                               |
| [form](http://www.w3school.com.cn/tags/att_select_form.asp) | *form_id* | 规定文本区域所属的一个或多个表单。 规定 <select> 元素所属的 form 元素。该属性的值必须是同一文档中的某个 <form> 元素的 id 属性。 |
| [multiple](http://www.w3school.com.cn/tags/att_select_multiple.asp) | multiple  | 规定可选择多个选项。                               |
| [name](http://www.w3school.com.cn/tags/att_select_name.asp) | *name*    | 规定下拉列表的名称。                               |
| [required](http://www.w3school.com.cn/tags/att_select_required.asp) | required  | 规定文本区域是必填的。                              |
| [size](http://www.w3school.com.cn/tags/att_select_size.asp) | *number*  | 规定下拉列表中可见选项的数目。                          |



### autofocus

autofocus 属性是逻辑属性。

当设置该属性后，它规定在页面加载后下拉列表应该自动获得焦点。

```html
<select autofocus>
   <option value="volvo">Volvo</option>
   <option value="saab">Saab</option>
   <option value="opel">Opel</option>
   <option value="audi">Audi</option>
</select> 
```

### disabled

disabled 属性规定禁用下拉列表。被禁用的下拉列表既不可用，也不可点击。

可以设置 disabled 属性，直到满足某些条件（比如选择一个复选框），才恢复用户对该下拉列表的使用。然后，可以使用 JavaScript 来清除 disabled 属性，以使下拉列表变为可用状态。

```html
<select disabled="disabled">
  <option value ="volvo">Volvo</option>
  <option value ="saab">Saab</option>
  <option value="opel">Opel</option>
  <option value="audi">Audi</option>
</select>	
```

### form

form 属性规定下拉列表所属的一个或多个表单。

```html
<form action="" id="carform">
  名字：<input type="text" name="fname">
  <input type="submit">
</form>
<br>
<select name="carlist" form="carform">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="opel">Opel</option>
  <option value="audi">Audi</option>
</select>

<p>下拉列表位于表单之外，但仍然属于该表单的一部分。</p>
```

### multiple

multiple 属性规定可同时选择多个选项。

在不同操作系统中，选择多个选项的差异：

- 对于 windows：按住 Ctrl 按钮来选择多个选项
- 对于 Mac：按住 command 按钮来选择多个选项

由于上述差异的存在，同时由于需要告知用户可以使用多项选择，对用户更友好的方式是使用复选框。

提示：可以把 multiple 属性与 size 属性配合使用，来定义可见选项的数目。

```html
<select multiple="multiple" size="2">
  <option value ="volvo">Volvo</option>
  <option value ="saab">Saab</option>
  <option value="opel">Opel</option>
  <option value="audi">Audi</option>
</select>
```

### name

name 属性规定 select 元素的名称。

name 属性用于对提交到服务器后的表单数据进行标识，或者在客户端通过 JavaScript 引用表单数据。

```html
<select name="carlist">
  <option value ="volvo">Volvo</option>
  <option value ="saab">Saab</option>
  <option value="opel">Opel</option>
  <option value="audi">Audi</option>
</select>
```

### required

required 属性是逻辑属性。

如果设置该属性，它规定用户在提交表单之前必须选择一个值。

所有主流浏览器都不支持 required 属性。

```html
<form action="demo_form.asp">
 <select required>
   <option value="volvo">Volvo</option>
   <option value="saab">Saab</option>
   <option value="mercedes">Mercedes</option>
   <option value="audi">Audi</option>
 </select>
 <input type="submit">
</form> 
```

### size

size 属性规定下拉列表中可见选项的数目。

如果 size 属性的值大于 1，但是小于列表中选项的总数目，浏览器会显示出滚动条，表示可以查看更多选项。

移动端该效果不可用

```html
<select size="2">
  <option value ="volvo">Volvo</option>
  <option value ="saab">Saab</option>
  <option value="opel">Opel</option>
  <option value="audi">Audi</option>
</select>
```