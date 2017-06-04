## HTML 事件属性



## 全局事件属性

HTML 4 的新特性之一是可以使 HTML 事件触发浏览器中的行为，比方说当用户点击某个 HTML 元素时启动一段 JavaScript。

下面的表格提供了标准的事件属性，可以把它们插入 HTML/XHTML 元素中，以定义事件行为。

> HTML5新增属性事件: (H5)

## 窗口事件属性（Window Event Attributes）

由窗口触发该事件 (适用于 `<body>` 标签):

| 属性                                       | 值        | 描述                                     |
| ---------------------------------------- | -------- | -------------------------------------- |
| [onafterprint](http://www.runoob.com/tags/ev-onafterprint.html) (H5) | *script* | 在打印文档之后运行脚本                            |
| [onbeforeprint](http://www.runoob.com/tags/ev-onbeforeprint.html) (H5) | *script* | 在文档打印之前运行脚本                            |
| onbeforeonload (H5)                      | *script* | 在文档加载之前运行脚本                            |
| onblur                                   | *script* | 当窗口失去焦点时运行脚本                           |
| onerror (H5)                             | *script* | 当错误发生时运行脚本                             |
| onfocus                                  | *script* | 当窗口获得焦点时运行脚本                           |
| onhaschange (H5)                         | *script* | 当文档改变时运行脚本                             |
| [onload](http://www.runoob.com/tags/ev-onload.html) | *script* | 当文档加载时运行脚本                             |
| onmessage (H5)                           | *script* | 当触发消息时运行脚本                             |
| onoffline (H5)                           | *script* | 当文档离线时运行脚本                             |
| ononline (H5)                            | *script* | 当文档上线时运行脚本                             |
| onpagehide (H5)                          | *script* | 当窗口隐藏时运行脚本                             |
| onpageshow (H5)                          | *script* | 当窗口可见时运行脚本                             |
| onpopstate (H5)                          | *script* | 当窗口历史记录改变时运行脚本                         |
| onredo (H5)                              | *script* | 当文档执行再执行操作（redo）时运行脚本                  |
| [onresize](http://www.runoob.com/tags/ev-onresize.html) (H5) | *script* | 当调整窗口大小时运行脚本                           |
| onstorage (H5)                           | *script* | 当 Web Storage 区域更新时（存储空间中的数据发生变化时）运行脚本 |
| onundo (H5)                              | *script* | 当文档执行撤销时运行脚本                           |
| [onunload](http://www.runoob.com/tags/ev-onunload.html) (H5) | *script* | 当用户离开文档时运行脚本                           |



## 表单事件(Form Events)

表单事件在HTML表单中触发 (适用于所有 HTML 元素, 但该HTML元素需在form表单内):

| 属性                                       | 值        | 描述                     |
| ---------------------------------------- | -------- | ---------------------- |
| [onblur](http://www.runoob.com/tags/ev-onblur.html) | *script* | 当元素失去焦点时运行脚本           |
| [onchange](http://www.runoob.com/tags/ev-onchange.html) | *script* | 当元素改变时运行脚本             |
| oncontextmenu (H5)                       | *script* | 当触发上下文菜单时运行脚本          |
| [onfocus](http://www.runoob.com/tags/ev-onfocus.html) | *script* | 当元素获得焦点时运行脚本           |
| onformchange (H5)                        | *script* | 当表单改变时运行脚本             |
| onforminput (H5)                         | *script* | 当表单获得用户输入时运行脚本         |
| oninput (H5)                             | *script* | 当元素获得用户输入时运行脚本         |
| oninvalid (H5)                           | *script* | 当元素无效时运行脚本             |
| onreset                                  | *script* | 当表单重置时运行脚本。HTML 5 不支持。 |
| [onselect](http://www.runoob.com/tags/ev-onselect.html) | *script* | 当选取元素时运行脚本             |
| [onsubmit](http://www.runoob.com/tags/ev-onsubmit.html) | *script* | 当提交表单时运行脚本             |

------

## 键盘事件（Keyboard Events）

| 属性                                       | 值        | 描述            |
| ---------------------------------------- | -------- | ------------- |
| [onkeydown](http://www.runoob.com/tags/ev-onkeydown.html) | *script* | 当按下按键时运行脚本    |
| [onkeypress](http://www.runoob.com/tags/ev-onkeypress.html) | *script* | 当按下并松开按键时运行脚本 |
| [onkeyup](http://www.runoob.com/tags/ev-onkeyup.html) | *script* | 当松开按键时运行脚本    |

------

## 鼠标事件（Mouse Events）

通过鼠标触发事件, 类似用户的行为:

| 属性                                       | 值        | 描述                   |
| ---------------------------------------- | -------- | -------------------- |
| [onclick](http://www.runoob.com/tags/ev-onclick.html) | *script* | 当单击鼠标时运行脚本           |
| [ondblclick](http://www.runoob.com/tags/ev-ondblclick.html) | *script* | 当双击鼠标时运行脚本           |
| ondrag (H5)                              | *script* | 当拖动元素时运行脚本           |
| ondragend (H5)                           | *script* | 当拖动操作结束时运行脚本         |
| ondragenter (H5)                         | *script* | 当元素被拖动至有效的拖放目标时运行脚本  |
| ondragleave (H5)                         | *script* | 当元素离开有效拖放目标时运行脚本     |
| ondragover (H5)                          | *script* | 当元素被拖动至有效拖放目标上方时运行脚本 |
| ondragstart (H5)                         | *script* | 当拖动操作开始时运行脚本         |
| ondropNew                                | *script* | 当被拖动元素正在被拖放时运行脚本     |
| [onmousedown](http://www.runoob.com/tags/ev-onmousedown.html) | *script* | 当按下鼠标按钮时运行脚本         |
| [onmousemove](http://www.runoob.com/tags/ev-onmousemove.html) | *script* | 当鼠标指针移动时运行脚本         |
| [onmouseout](http://www.runoob.com/tags/ev-onmouseout.html) | *script* | 当鼠标指针移出元素时运行脚本       |
| [onmouseover](http://www.runoob.com/tags/ev-onmouseover.html) | *script* | 当鼠标指针移至元素之上时运行脚本     |
| [onmouseup](http://www.runoob.com/tags/ev-onmouseup.html) | *script* | 当松开鼠标按钮时运行脚本         |
| onmousewheel (H5)                        | *script* | 当转动鼠标滚轮时运行脚本         |
| onscroll (H5)                            | *script* | 当滚动元素的滚动条时运行脚本       |



## 多媒体事件(Media Events)

通过视频（videos），图像（images）或者音频（audio） 触发该事件，多应用于HTML媒体元素比如 `<audio>`, `<embed>`, `<img>`, `<object>`, 和`<video>`:

| 属性                      | 值        | 描述                             |
| ----------------------- | -------- | ------------------------------ |
| onabort                 | *script* | 当发生中止事件时运行脚本                   |
| oncanplay (H5)          | *script* | 当媒介能够开始播放但可能因缓冲而需要停止时运行脚本      |
| oncanplaythrough (H5)   | *script* | 当媒介能够无需因缓冲而停止即可播放至结尾时运行脚本      |
| ondurationchange (H5)   | *script* | 当媒介长度改变时运行脚本                   |
| onemptied (H5)          | *script* | 当媒介资源元素突然为空时（网络错误、加载错误等）运行脚本   |
| onended (H5)            | *script* | 当媒介已抵达结尾时运行脚本                  |
| onerror (H5)            | *script* | 当在元素加载期间发生错误时运行脚本              |
| onloadeddata (H5)       | *script* | 当加载媒介数据时运行脚本                   |
| onloadedmetadata (H5)   | *script* | 当媒介元素的持续时间以及其他媒介数据已加载时运行脚本     |
| onloadstart (H5)        | *script* | 当浏览器开始加载媒介数据时运行脚本              |
| onpause (H5)            | *script* | 当媒介数据暂停时运行脚本                   |
| onplay (H5)             | *script* | 当媒介数据将要开始播放时运行脚本               |
| onplaying (H5)          | *script* | 当媒介数据已开始播放时运行脚本                |
| onprogress (H5)         | *script* | 当浏览器正在取媒介数据时运行脚本               |
| onratechange (H5)       | *script* | 当媒介数据的播放速率改变时运行脚本              |
| onreadystatechange (H5) | *script* | 当就绪状态（ready-state）改变时运行脚本      |
| onseeked (H5)           | *script* | 当媒介元素的定位属性 [1] 不再为真且定位已结束时运行脚本 |
| onseeking (H5)          | *script* | 当媒介元素的定位属性为真且定位已开始时运行脚本        |
| onstalled (H5)          | *script* | 当取回媒介数据过程中（延迟）存在错误时运行脚本        |
| onsuspend (H5)          | *script* | 当浏览器已在取媒介数据但在取回整个媒介文件之前停止时运行脚本 |
| ontimeupdate (H5)       | *script* | 当媒介改变其播放位置时运行脚本                |
| onvolumechange (H5)     | *script* | 当媒介改变音量亦或当音量被设置为静音时运行脚本        |
| onwaiting (H5)          | *script* | 当媒介已停止播放但打算继续播放时运行脚本           |

## 其他事件

| 属性                                       | 值        | 描述                         |
| ---------------------------------------- | -------- | -------------------------- |
| [onshow](http://www.runoob.com/tags/ev-onshow.html) (H5) | *script* | 当 `<menu>` 元素在上下文显示时触发     |
| [ontoggle](http://www.runoob.com/tags/ev-ontoggle.html) (H5) | *script* | 当用户打开或关闭 `<details>` 元素时触发 |