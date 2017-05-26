如果你是使用URL取图片地址，地址中带有空格是读不到图片的，需要把地址中的空格改为%20。
根据URL的编码：空格的是%20



### inline elements(phrasing content)

you need to define *what* you want to say (HTML) before defining *how* you want to say it (CSS)

##### **emphasis(italic) elements**

1em = 16px

```
this is <em>em</em>.
```

##### **strong(bold) elements**

```
this is <strong>Strong</strong>.
```

> structure versus presentation
>
> You might be wondering why we’re using the terms “emphasis” and “strong” instead of “italic” and “bold”. That brings us to an important distinction between HTML and CSS. HTML markup should provide semantic information about your content—not presentational information. In other words, HTML should define the structure of your document, leaving its appearance to CSS.

```
this is <b>BOLD</b>.this is <i>i</i>. 
```

> The pseudo-obsolete <b> and <i> elements are classic examples of this. They used to stand for “bold” and “italic”, respectively, but HTML5 attempted to create a clear separation between a document’s structure and its presentation. Thus, <i> was replaced with <em>, since emphasized text can be displayed in all sorts of ways aside from being italicized (e.g., in a different font, a different color, or a bigger size). Same for <b> and <strong>.

##### **line breaks**

```
<br/>
```

##### **horizontal rules**

```
<hr/>
```

> The <hr/> element is a “horizontal rule”, which represents a thematic break. The transition from one scene of a story into the next or between the end of a letter and a postscript are good examples of when a horizontal rule may be appropriate.
>
> Like <br/>, <hr/> should carry meaning—don’t use it when you just want to display a line for the sake of aesthetics.
>
> Another way to think about the <hr/> element is that it carries *less* significance than the separation created by a new heading element, but *more* significance than a new paragraph.

##### **optional trailing slash**

> The trailing slash (/) in all empty HTML elements is entirely optional. 
>
> ```
> note the lack of / in the <br> and <hr> tags
> ```
> It doesn’t really make a difference which convention you choose, but pick one and stick to it for the sake of consistency.
>
> we’ll be including the trailing / character because it clearly shows that it’s a self-closing element. This will help prevent your eyes from searching for the closing tag elsewhere in the document.

### Link

##### **Absolute Links**

> “Absolute” links are the most detailed way you can refer to a web resource. They start with the “scheme” (typically http:// or https://), followed by the domain name of the website, then the path of the target web page.
>
> It’s usually a better idea to reserve absolute links only for directing users to a different website.
>
> ```
> <a href='https://developer.mozilla.org/en-US/docs/Web/HTML'>Mozilla
>     Developer Network</a>
> ```

##### **Relative links**

> “Relative” links point to another file in your website from the vantage point of the file you’re editing. It’s implied that the scheme and domain name are the same as the current page, so the only thing you need to supply is the path.
>
> ```
> <a href='misc/extras.html'>extras
>     page</a>
> ```

##### **Parent folders**

> That works for referring to files that are in the same folder or a deeper folder.
>
> ```
> <a href='../links.html'>links</a>
> ```

##### **Root-relative links**

> “Root-relative” links are relative to the “root” of the entire website.
>
> if your website is hosted on our-site.com, all root-relative URLs will be relative to our-site.com.
>
> ```
> <li>Root-relative links, like to the <a href='/'>home page</a> of our website,
>     but those aren't useful to us right now.</li>
> ```

### HTML Attributes

##### **document language**

> A web page’s default language is defined by the lang attribute on the top-level <html> element. Our document is in English, so we’ll use the en country code as the attribute value
>
> ```
> <html lang='en'>
> ```

##### **character sets**

> A “character set” is kind of like a digital alphabet for your browser. It’s different from the language of your document in that it only affects how the letters themselves are rendered, not the language of the content.
>
> The special characters should now render correctly. These days, UTF-8 is sort of like a universal alphabet for the Internet. Every web page you create should have this line in its <head>.
>
> ```
> <meta charset='UTF-8'/>
> ```

### HTML Entities

An “HTML entity” is a special character that can’t be represented as plain text in an HTML document. This typically either means it’s a reserved character in HTML or you don’t have a key on your keyboard for it.

##### reserved characters

> Entities always begin with an ampersand (`&`) and end with a semicolon (`;`). In between, you put a special code that your browser will interpret as a symbol
>
> ```
> <p>There are three reserved characters in HTML: &lt; &gt; and &amp;. You
>    should always use HTML entities for these three characters.</p>
>    <a href="https://dev.w3.org/html5/html-author/charref">HTML entities</a>
> ```



### 网站图标Icon

只需要将这个图标文件（favicon.ico）上传到您的网站所在的服务器的根目录下。(也就是你的主页index.html所在的那个文件夹)您不需要对您的网页文件作任何的修改，IE5会自动的不停的搜索您的网站的根目录，只要它一发现了favicon.ico 这个文件，就会将该图标显示在访问者的地址栏和收藏夹列表中了。 
如果您希望为不同的页面设置不同的“收藏夹”图标，那么您就需要在该网页文件的HEAD部分加入下面的内容: 

```
<link rel="shortcut icon"href="myicon.ico"> 
```

注意：该图标的路径一定要使用绝对路径。 
2、第二种方法:在首页HTML文件中，加入link命令，`<link>`是放在`<head>`与`</head>`之间 
例如下面这样： 

```
<HEAD> 
<link rel = "Shortcut Icon" href=/favicon.ico> 
</HEAD> 
```

其中的href="/favicon.icon（只是一个例子，你只要将他替换成你的网址）将favicon.ico替换成你制作的ICO文件名即可 
这样只有当网友把你的网站加到Internet Explorer的收藏夹中并重新打开Internet Explorer浏览器之后，你自行制作的图标才会显示出来。 

常用方法： 

```
<link rel="icon" href="/jb51.ico" type="image/x-icon"/> 
<link rel="shortcut icon" href="/jb51.ico" type="image/x-icon"/> 
```



#### Data URI scheme `data:image/png;base64`

大家可能注意到了，网页上有些图片的src或css背景图片的url后面跟了一大串字符，比如：

```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAJAQMAAADaX5RTAAAAA3NCSVQICAjb4U/gAAAABlBMVEX///+ZmZmOUEqyAAAAAnRSTlMA/1uRIrUAAAAJcEhZcwAACusAAArrAYKLDVoAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDkvMjAvMTIGkKG+AAAAHHRFWHRTb2Z0d2FyZQBBZG9iZSBGaXJld29ya3MgQ1M26LyyjAAAAB1JREFUCJljONjA8LiBoZyBwY6BQQZMAtlAkYMNAF1fBs/zPvcnAAAAAElFTkSuQmCC
```

那么这是什么呢？这是Data URI scheme。

Data URI scheme是在RFC2397中定义的，目的是将一些小的数据，直接嵌入到网页中，从而不用再从外部文件载入。比如上面那串字符，其实是一张小图片，将这些字符复制黏贴到火狐的地址栏中并转到，就能看到它了，一张1X36的白灰png图片。

在上面的Data URI中，data表示取得数据的协定名称，image/png 是数据类型名称，base64 是数据的编码方法，逗号后面就是这个image/png文件base64编码后的数据。

```
Data URI scheme支持的类型有：

data:,文本数据
data:text/plain,文本数据
data:text/html,HTML代码
data:text/html;base64,base64编码的HTML代码
data:text/css,CSS代码
data:text/css;base64,base64编码的CSS代码
data:text/javascript,Javascript代码
data:text/javascript;base64,base64编码的Javascript代码
data:image/gif;base64,base64编码的gif图片数据
data:image/png;base64,base64编码的png图片数据
data:image/jpeg;base64,base64编码的jpeg图片数据
data:image/x-icon;base64,base64编码的icon图片数据

base64简单地说，它把一些 8-bit 数据翻译成标准 ASCII 字符.
```

网上有很多免费的base64 编码和解码的工具，在PHP中可以用函数base64_encode() 进行编码，

如

```
echo base64encode(file_get_contents(‘wg.png’));
```

目前，IE8、Firfox、Chrome、Opera浏览器都支持这种小文件嵌入。

 

举个图片的例子：

网页中一张图片可以这样显示：

```
<img src="http://mail.163.com/images/x.png" />
```

 

也可以这样显示：

```
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAJAQMAAADaX5RTAAAAA3NCSVQICAjb4U/gAAAABlBMVEX///+ZmZmOUEqyAAAAAnRSTlMA/1uRIrUAAAAJcEhZcwAACusAAArrAYKLDVoAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDkvMjAvMTIGkKG+AAAAHHRFWHRTb2Z0d2FyZQBBZG9iZSBGaXJld29ya3MgQ1M26LyyjAAAAB1JREFUCJljONjA8LiBoZyBwY6BQQZMAtlAkYMNAF1fBs/zPvcnAAAAAElFTkSuQmCC" />
```

 把图像文件的内容直接写在了HTML 文件中，这样做的好处是，节省了一个HTTP 请求。坏处是浏览器不会缓存这种图像。

 



#### base64

http://baike.baidu.com/link?url=70MjSwBpM2r_woKdjRXSO3SUD95DUwCairxxoszaRpOWmkx5aBeehNGKTks38_WnrrkbdZ7tUI_YG_Jr9h8iBa