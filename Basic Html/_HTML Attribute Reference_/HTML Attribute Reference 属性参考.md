# HTML Attribute Reference 属性参考

HTML中的元素是有属性的；这些额外的属性值可以配置元素或者以各种方式来调整元素的行为，进而满足用户所需的标准。

## 属性列表:

| 属性名             |                    元素                    | 描述                                       |      |
| :-------------- | :--------------------------------------: | ---------------------------------------- | :--: |
| accept          |           `<form>` , `<imput>`           | 服务器接受内容或文件类型的列表。                         |  1   |
| accept-charset  |                 `<form>`                 | 支持的字符集列表。                                |  2   |
| accesskey       |             Global attribute             | 定义键盘快捷键来激活或者聚焦元素                         |  3   |
| action          |                 `<form>`                 | 表单信息提交的url地址，指向进行处理的程序。                  |      |
| align           | `<applet>`, [`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/caption), , ,  [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/hr), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/iframe), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/table), ,  [`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/td),   , [`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/th), , | 设置元素的水平对齐。                               |      |
| alt             | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/applet), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/area), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input) | 在图片无法呈现时的替代文本。                           |      |
| async           | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/script) | 表示该脚本应该异步执行。                             |      |
| autocomplete    | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/form), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input) | 表示该表单中是否可以由浏览器自动完成填值。                    |      |
| autofocus       | `<button>` ,  `<input>` ,  `<keygen>` ,  `<select>` ,  `<textarea>` | 在网页加载后该元素应该自动聚焦。                         |      |
| autoplay        | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/audio), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/video) | audio或video应该自动播放                        |      |
| bgcolor         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/body), , , [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/marquee), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/table), , , [`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/td), [`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/th), | 元素的背景颜色。NOTE：这是一个遗留属性，请使用css{“background-color":}代替。 |      |
| border          | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/object), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/table) | 边框宽度。Note:这是遗留属性，请使用 CSS `border` 属性代替。 |                                          |      |
| buffered        | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/audio), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/video) | 包含已缓存媒体的时间范围。                            |      |
| challenge       | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/keygen) | 与公钥一起提交的挑战字符。                            |      |
| charset         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meta), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/script) | 申明该页面或脚本的字符编码。                           |      |
| checked         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/command), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input) | 指出该元素在页面加载后是否处于选中状态。                     |      |
| cite            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/blockquote), [`~~`~~](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/del), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/ins), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/q) | 包含一个URI，用来指明引用或修改的源地址。                   |      |
| class           | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | 经常和CSS一起配合使用来修饰元素。                       |      |
| code            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/applet) | 标明被加载和执行的applet类文件的URL。                  |      |
| codebase        | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/applet) | This attribute gives the absolute or relative URL of the directory where applets' .class files referenced by the code attribute are stored. |      |
| color           | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/basefont), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/font), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/hr) | This attribute sets the text color using either a named color or a color specified in the hexadecimal #RRGGBB format.Note: This is a legacy attribute. Please use the CSS `color` property instead. |                                          |      |
| cols            |               `<textarea>`               | 定义一个textarea中包含多少列。                      |      |
| colspan         | [`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/td), [`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/th) | The colspan attribute defines the number of columns a cell should span. |      |
| content         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meta) | A value associated with `http-equiv` or `name` depending on the context. |                                          |      |
| contenteditable | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | Indicates whether the element's content is editable. |      |
| contextmenu     | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | Defines the ID of a [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/menu) element which will serve as the element's context menu. |      |
| controls        | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/audio), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/video) | Indicates whether the browser should show playback controls to the user. |      |
| coords          | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/area) | A set of values specifying the coordinates of the hot-spot region. |      |
| data            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/object) | Specifies the URL of the resource.       |      |
| data-*          | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | 允许你对于一个HTML元素绑定自定义的属性。                   |      |
| datetime        | [`~~`~~](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/del), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/ins), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/time) | Indicates the date and time associated with the element. |      |
| default         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/track) | Indicates that the track should be enabled unless the user's preferences indicate something different. |      |
| defer           | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/script) | Indicates that the script should be executed after the page has been parsed. |      |
| dir             | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left) |      |
| dirname         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/textarea) |                                          |      |
| disabled        | `<button>` ,  `<command>` ,  `<fieldset>` ,  `<input>` ,  `<keygen>` ,  `optgroup` ,  `<option>` ,  `<select>` ,  `<textarea>` | Indicates whether the user can interact with the element. |      |
| download        | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/area) | Indicates that the hyperlink is to be used for downloading a resource. |      |
| draggable       | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | Defines whether the element can be dragged. |      |
| dropzone        | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | Indicates that the element accept the dropping of content on it. |      |
| enctype         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/form) | Defines the content type of the form date when the `method` is POST. |                                          |      |
| for             | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/label), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/output) | 描述与当前元素绑定的元素。                            |      |
| form            | `<button>` ,  `<fieldset>` ,  `<input>` ,  `<keygen>` ,  `<label>` ,  `<meter>` ,  `<object>` ,  `<output>` ,  `<progress>` ,  `<select>` ,  `<textarea>` | Indicates the form that is the owner of the element. |      |
| headers         | [`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/td), [`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/th) | IDs of the ` elements which applies to this element. |      |
| height          | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/canvas), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/embed), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/iframe), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/object), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/video) | Note: In some instances, such as [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/div), this is a legacy attribute, in which case the CSS [`height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/height) property should be used instead. In other cases, such as [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/canvas), the height must be specified with this attribute. |                                          |      |
| hidden          | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | Indicates the relevance of an element.   |      |
| high            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meter) | Indicates the lower bound of the upper range. |      |
| href            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/area), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/base), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/link) | 关联资源的URL。                                |      |
| hreflang        | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/area), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/link) | Specifies the language of the linked resource. |      |
| http-equiv      | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meta) |                                          |      |
| icon            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/command) | Specifies a picture which represents the command. |      |
| id              | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | Often used with CSS to style a specific element. The value of this attribute must be unique. |      |
| ismap           | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img) | Indicatesthat the image is part of a server-side image map. |      |
| itemprop        | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) |                                          |      |
| keytype         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/keygen) | Specifies the type of key generated.     |      |
| kind            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/track) | Specifies the kind of text track.        |      |
| label           | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/track) | Specifies a user-readable title of the text track. |      |
| lang            | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | Defines the language used in the element. |      |
| language        | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/script) | Defines the script language used in the element. |      |
| list            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input) | Identifies a list of pre-defined options to suggest to the user. |      |
| loop            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/audio), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/bgsound), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/marquee), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/video) | Indicates whether the media should start playing from the start when it's finished. |      |
| low             | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meter) | Indicates the upper bound of the lower range. |      |
| manifest        | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/html) | Specifies the URL of the document's cache manifest. |      |
| max             | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meter), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/progress) | Indicates the maximum value allowed.     |      |
| maxlength       |        `<input>` ,  `<textarea>`         | Defines the maximum number of characters allowed in the element. |      |
| media           | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/area), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/link), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/source), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/style) | Specifies a hint of the media for which the linked resource was designed. |      |
| method          | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/form) | Defines which HTTP method to use when submitting the form. Can be GET (default) or POST. |      |
| min             | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meter) | Indicates the minimum value allowed.     |      |
| multiple        | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/select) | Indicates whether multiple values can be entered in an input of the type `email` or `file`. |      |
| name            | `<button>` ,  `<form>` ,  `<fieldset>` ,  `<iframe>` ,  `<input>` ,  `<keygen>` ,  `<object>` ,  `<output>` ,  `<select>` ,  `<textarea>` ,  `<map>` ,  `<meta>` ,  `<param>` | Name of the element. For example used by the server to identify the fields in form submits. |      |
| novalidate      | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/form) | This attribute indicates that the form shouldn't be validated when submitted. |      |
| open            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/details) | Indicates whether the details will be shown on page load. |      |
| optimum         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meter) | Indicates the optimal numeric value.     |      |
| pattern         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input) | Defines a regular expression which the element's value will be validated against. |      |
| ping            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/area) |                                          |      |
| placeholder     |        `<input>` ,  `<textarea>`         | Provides a hint to the user of what can be entered in the field. |      |
| poster          | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/video) | A URL indicating a poster frame to show until the user plays or seeks. |      |
| preload         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/audio), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/video) | Indicates whether the whole resource, parts of it or nothing should be preloaded. |      |
| pubdate         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/time) | Indicates whether this date and time is the date of the nearest [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/article) ancestor element. |                                          |      |
| radiogroup      | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/command) |                                          |      |
| readonly        |        `<input>` ,  `<textarea>`         | Indicates whether the element can be edited. |      |
| rel             | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/area), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/link) | Specifies the relationship of the target object to the link object. |      |
| required        | `<input>` ,  `<select>` ,  `<textarea>`  | Indicates whether this element is required to fill out or not. |      |
| reversed        | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/ol) | Indicates whether the list should be displayed in a descending order instead of a ascending. |      |
| rows            |               `<textarea>`               | Defines the number of rows in a textarea. |      |
| rowspan         | [`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/td), [`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/th) | Defines the number of rows a table cell should span over. |      |
| sandbox         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/iframe) |                                          |      |
| spellcheck      | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | Indicates whether spell checking is allowed for the element. |      |
| scope           | [`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/th) |                                          |      |
| scoped          | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/style) |                                          |      |
| seamless        | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/iframe) |                                          |      |
| selected        | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/option) | Defines a value which will be selected on page load. |      |
| shape           | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/area) |                                          |      |
| size            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/select) | Defines the width of the element (in pixels). If the element's `type`attribute is `text` or `password` then it's the number of characters. |      |
| sizes           | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/link) |                                          |      |
| span            |                    ,                     |                                          |      |
| src             | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/audio), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/embed), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/iframe), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/script), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/source), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/track), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/video) | The URL of the embeddable content.       |      |
| srcdoc          | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/iframe) |                                          |      |
| srclang         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/track) |                                          |      |
| start           | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/ol) | Defines the first number if other than 1. |      |
| step            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input) |                                          |      |
| style           | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | 定义CSS样式，这些样式会覆盖之前设置的样式。                  |      |
| summary         | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/table) |                                          |      |
| tabindex        | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | Overrides the browser's default tab order and follows the one specified instead. |      |
| target          | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/area), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/base), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/form) |                                          |      |
| title           | [Global attribute](https://developer.mozilla.org/en/HTML/Global_attributes) | 当鼠标悬停在元素上面时，提示框显示的文本。                    |      |
| type            | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/button), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/command), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/embed), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/object), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/script), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/source), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/style), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/menu) | 定义元素的类型。                                 |      |
| usemap          | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img),  [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/object) |                                          |      |
| value           | [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/button), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/option), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/li), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meter), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/progress), [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/param) | 定义页面加载时，在元素内显示的默认值。                      |      |
| width           | `<canvas>` , `<embed>` , `<iframe>`, `<img>` , `<input>` ,  `<object>` , `<video>` | Note: In some instances, such as `<div>`, this is a legacy attribute, in which case the CSS `width` property should be used instead. In other cases, such as `<canvas>`, the width must be specified with this attribute. |      |
| wrap            |               `<textarea>`               | Indicates whether the text should be wrapped. |      |



## autofocus (H5)

This Boolean attribute lets you specify that a form control should have input focus when the page loads, unless the user overrides it, for example by typing in a different control. Only one form-associated element in a document can have this attribute specified. 

## cols

The visible width of the text control, in average character widths. If it is specified, it must be a positive integer. If it is not specified, the default value is 20 (HTML5).

## disabled

This Boolean attribute indicates that the user cannot interact with the control. (If this attribute is not specified, the control inherits its setting from the containing element, for example `<fieldset>`; if there is no containing element with the `disabled`attribute set, then the control is enabled.)

## form (H5)

The form element that the textarea element is associated with (its "form owner"). The value of the attribute must be an ID of a form element in the same document. If this attribute is not specified, the textarea element must be a descendant of a form element. This attribute enables you to place textarea elements anywhere within a document, not just as descendants of their form elements.

## **maxlength** (H5)

The maximum number of characters (Unicode code points) that the user can enter. If it is not specified, the user can enter an unlimited number of characters.

## name

The name of the control.

## placeholder (H5)

A hint to the user of what can be entered in the control. Carriage returns or line-feeds within the placeholder text must be treated as line breaks when rendering the hint.

## readonly

This Boolean attribute indicates that the user cannot modify the value of the control. Unlike the `disabled` attribute, the `readonly` attribute does not prevent the user from clicking or selecting in the control. The value of a read-only control is still submitted with the form.

## **required** 

This attribute specifies that the user must fill in a value before submitting a form.

## rows

The number of visible text lines for the control.

## wrap (H5)

Indicates how the control wraps text. Possible values are:

- hard: The browser automatically inserts line breaks (CR+LF) so that each line has no more than the width of the control; the `cols` attribute must be specified.
- soft: The browser ensures that all line breaks in the value consist of a CR+LF pair, but does not insert any additional line breaks.

If this attribute is not specified, soft is its default value.