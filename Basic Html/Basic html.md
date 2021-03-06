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



## px, pt, em 换算

- **pt (point，磅)：**

  是一个物理长度单位，指的是72分之一英寸。


- **px (pixel，像素)：**

  是一个虚拟长度单位，是计算机系统的数字化图像长度单位，如果px要换算成物理长度，需要指定精度DPI(Dots Per Inch，每英寸像素数)，在扫描打印时一般都有DPI可选。Windows系统默认是96dpi，Apple系统默认是72dpi。


- **em(相对长度单位，相对于当前对象内文本的字体尺寸)：**

  是一个相对长度单位，最初是指字母M的宽度，故名em。现指的是字符宽度的倍数，用法类似百分比，如：0.8em, 1.2em,2em等。通常1em=16px。

  > 1. em的值并不是固定的；
  > 2. em会继承父级元素的字体大小。
  >
  > **注意：**任意浏览器的默认字体高都是16px。所有未经调整的浏览器都符合: 1em=16px。那么12px=0.75em,10px=0.625em。为了简化font-size的换算，需要在css中的body选择器中声明Font-size=62.5%，这就使em值变为 16px*62.5%=10px, 这样12px=1.2em, 10px=1em, 也就是说只需要将你的原来的px数值除以10，然后换上em作为单位就行了。
  >
  > 所以我们在写CSS的时候，需要注意两点：
  >
  > 1. body选择器中声明Font-size=62.5%；
  > 2. 将你的原来的px数值除以10，然后换上em作为单位；
  > 3. 重新计算那些被放大的字体的em数值。避免字体大小的重复声明。
  >
  > 也就是避免1.2 * 1.2= 1.44的现象。比如说你在#content中声明了字体大小为1.2em，那么在声明p的字体大小时就只能是1em，而不是1.2em, 因为此em非彼em，它因继承#content的字体高而变为了1em=12px。


- **字号：**

  是中文字库中特有的一种单位，以中文代号表示特定的磅值pt，便于记忆、表述。

- **REM:**

  rem是CSS3新增的一个相对单位（root em，根em），这个单位引起了广泛关注。这个单位与em有什么区别呢？区别在于使用rem为元素设定字体大小时，仍然是相对大小，但相对的只是HTML根元素。这个单位可谓集相对大小和绝对大小的优点于一身，通过它既可以做到只修改根元素就成比例地调整所有字体大小，又可以避免字体大小逐层复合的连锁反应。目前，除了IE8及更早版本外，所有浏览器均已支持rem。对于不支持它的浏览器，应对方法也很简单，就是多写一个绝对单位的声明。这些浏览器会忽略用rem设定的字体大小。

  > **注意：** 选择使用什么字体单位主要由你的项目来决定，如果你的用户群都使用最新版的浏览器，那推荐使用rem，如果要考虑兼容性，那就使用px,或者两者同时使用。

  下面就是一个例子：

  ```
  p {font-size:14px; font-size:.875rem;}
  ```



### pt和px的换算公式

可以根据pt的定义得出:

```
pt = 1/72(英寸), px = 1/dpi(英寸)
```

因此 pt = px * dpi / 72

以 Windows 下的 96dpi 来计算，1 pt = px * 96/72 = px * 4/3

| 字号   | pt     | px   | em       |
| ---- | ------ | ---- | -------- |
| 初号   | 42pt   | 56px | 3.5em    |
| 小初   | 36pt   | 48px | 3em      |
|      | 34pt   | 45px | 2.75em   |
|      | 32pt   | 42px | 2.55em   |
|      | 30pt   | 40px | 2.45em   |
|      | 29pt   | 38px | 2.35em   |
|      | 28pt   | 37px | 2.3em    |
|      | 27pt   | 36px | 2.25em   |
| 一号   | 26pt   | 35px | 2.2em    |
|      | 25pt   | 34px | 2.125em  |
| 小一   | 24pt   | 32px | 2em      |
| 二号   | 22pt   | 29px | 1.8em    |
|      | 20pt   | 26px | 1.6em    |
| 小二   | 18pt   | 24px | 1.5em    |
|      | 17pt   | 23px | 1.45em   |
| 三号   | 16pt   | 22px | 1.4em    |
| 小三   | 15pt   | 21px | 1.3em    |
|      | 14.5pt | 20px | 1.25em   |
| 四号   | 14pt   | 19px | 1.2em    |
|      | 13.5pt | 18px | 1.125em  |
|      | 13pt   | 17px | 1.05em   |
| 小四   | 12pt   | 16px | 1em      |
|      | 11pt   | 15px | 0.95em   |
| 五号   | 10.5pt | 14px | 0.875em  |
|      | 10pt   | 13px | 0.8em    |
| 小五   | 9pt    | 12px | 0.75em   |
|      | 8pt    | 11px | 0.7em    |
| 六号   | 7.5pt  | 10px | 0.625em  |
|      | 7pt    | 9px  | 0.55em   |
| 小六   | 6.5pt  | 8px  | 0.5em    |
| 七号   | 5.5pt  | 7px  | 0.4375em |
| 八号   | 5pt    | 6px  | 0.375em  |



### px 与 rem 的选择？

对于只需要适配少部分手机设备，且分辨率对页面影响不大的，使用px即可 。

对于需要适配各种移动设备，使用rem，例如只需要适配iPhone和iPad等分辨率差别比较挺大的设备。



### 文本字体大小

下表列出了在**网页字体默认值为 16px** 时， px 和 em 及网页字体百分比的换算数据。

| px       | em           | 百分比         |
| -------- | ------------ | ----------- |
| 5px      | 0.3125em     | 31.25%      |
| 6px      | 0.3750em     | 37.50%      |
| 7px      | 0.4375em     | 43.75%      |
| 8px      | 0.5000em     | 50.00%      |
| 9px      | 0.5625em     | 56.25%      |
| 10px     | 0.6250em     | 62.50%      |
| 11px     | 0.6875em     | 68.75%      |
| 12px     | 0.7500em     | 75.00%      |
| 13px     | 0.8125em     | 81.25%      |
| 14px     | 0.8750em     | 87.50%      |
| 15px     | 0.9375em     | 93.75%      |
| **16px** | **1.0000em** | **100.00%** |
| 17px     | 1.0625em     | 106.25%     |
| 18px     | 1.1250em     | 112.50%     |
| 19px     | 1.1875em     | 118.75%     |
| 20px     | 1.2500em     | 125.00%     |
| 21px     | 1.3125em     | 131.25%     |
| 22px     | 1.3750em     | 137.50%     |
| 23px     | 1.4375em     | 143.75%     |
| 24px     | 1.5000em     | 150.00%     |
| 25px     | 1.5625em     | 156.25%     |



## 网站图标Icon

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



### URI & URL

**RFC(Request For Comments)** ，RFC文档是一系列关于Internet（早期为ARPANET）的技术资料汇总，于1969年开始发布。它制定了我们很多常见和不常见的Internet的各种文字资料和规范。

**URI(Universal Resource Identifiers)** 统一资源标识符， [RFC 文献1630](http://www.ietf.org/rfc/rfc1630.txt)中定义了它详细的规范(1994年6月)

 **URL(Uniform Resource Locators)** 统一资源定位符，[RFC文献1738](http://www.ietf.org/rfc/rfc1738.txt)中定义了它详细的规范(1994年12月)

#### Generic URI Syntax

```
BNF of Generic URI Syntax

    This is a BNF-like description of the URI syntax. at the level at
which specific schemes are not considered.
    A vertical line "|" indicates alternatives, and [brackets] indicate
optional parts.  Spaces are represented by the word "space", and the
vertical line character by "vline".  Single letters stand for single
letters.  All words of more than one letter below are entities
described somewhere in this description.
    The "generic" production gives a higher level parsing of the same
URIs as the other productions.  The "national" and "punctuation"
characters do not appear in any productions and therefore may not
appear in URIs.
   
     fragmentaddress        uri [ # fragmentid ]
--------------------------------------------------------------------------
     uri                    scheme :  path [ ? search ]
--------------------------------------------------------------------------
     scheme                 ialpha
--------------------------------------------------------------------------
     path                   void |  xpalphas  [  / path ]
--------------------------------------------------------------------------
     search                 xalphas [ + search ]
--------------------------------------------------------------------------
     fragmentid             xalphas
--------------------------------------------------------------------------
     xalpha                 alpha | digit | safe | extra | escape
--------------------------------------------------------------------------
     xalphas                xalpha [ xalphas ]
--------------------------------------------------------------------------
     xpalpha                xalpha | +
--------------------------------------------------------------------------
     xpalphas               xpalpha [ xpalpha ]
--------------------------------------------------------------------------
     ialpha                 alpha [ xalphas ]
--------------------------------------------------------------------------
     alpha                  a | b | c | d | e | f | g | h | i | j | k |
                            l | m | n | o  | p | q | r | s | t | u | v |
                            w | x | y | z | A | B | C  | D | E | F | G |
                            H | I | J | K | L | M | N | O | P |  Q | R |
                            S | T | U | V | W | X | Y | Z
--------------------------------------------------------------------------
     digit                  0 |1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
--------------------------------------------------------------------------
     safe                   $ | - | _ | @ | . | &
--------------------------------------------------------------------------
     extra                  ! | * | " |  ' | ( | ) | ,
--------------------------------------------------------------------------
     reserved               = | ; | / | # | ? | : | space
--------------------------------------------------------------------------
     escape                 % hex hex
--------------------------------------------------------------------------
     hex                    digit | a | b | c | d | e | f | A | B | C |
                            D | E | F
--------------------------------------------------------------------------
     national               { | } | vline | [ | ] | \ | ^ | ~
--------------------------------------------------------------------------
     punctuation            < | >
--------------------------------------------------------------------------
     void
--------------------------------------------------------------------------
      (end of URI BNF)
```

在**URI**的规范中，资源描述文字，只允许使用字母，数字，安全字符，特殊字符，和转义字符

转义字符在**URL**中规定是使用**%**和两个**hex**进行表示，所以也就是为什么浏览器的**form post**会自动进行转义成**%xx**的关系而不使用**unicode常用的%uxxxx**（同时ECMAScript v3也不推荐在js中使用escape）。

但是值得注意的是在URI中，空格是作为保留字的，所以URI规范中空格被辅以一个快速标记符号(short hand notation)来进行标识，就是我们看到的**+**号。所以在php中提供的**urlencode**方法是为了把字符串转换成URI规范用的, 保留空格转换成+号，可以模拟出浏览器form post的结果。

#### URL







### Data URI scheme

Data URI scheme 允许我们使用内联（inline-code）的方式在网页中包含数据.

Data URI scheme是在RFC2397中定义的，目的是将一些小的数据，直接嵌入到网页中，从而不用再从外部文件载入。常用于将图片嵌入网页。(比如上面那串字符，其实是一张小图片，将这些字符复制黏贴到浏览器的地址栏中并转到，就能看到它了。）

```
Data URI的图片内嵌式是这样用的:

img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAkUlEQVQ4jWOUO87Q8J+RoZ6BDMD4n6GRUfYEw39yNMMAEyWaqW9AoUw9wyPz/3BswWfPwMDAwLBKcx9crFCmHrcB6KBPaQFpLkAHMuwKGDaiAxZCNhRKNzA8+fmAdBcga5JhVyDHgPsM/U8bCDkQfxj0P2nE63yCBjAwMDAU3UvAKz8ckjLjf4ZGcjUz/mdoBADXpy5umvCg6AAAAABJRU5ErkJggg=="/
--------------------------------------------------------------------------

Data URI的直接通过url传递方式:

data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAkUlEQVQ4jWOUO87Q8J+RoZ6BDMD4n6GRUfYEw39yNMMAEyWaqW9AoUw9wyPz/3BswWfPwMDAwLBKcx9crFCmHrcB6KBPaQFpLkAHMuwKGDaiAxZCNhRKNzA8+fmAdBcga5JhVyDHgPsM/U8bCDkQfxj0P2nE63yCBjAwMDAU3UvAKz8ckjLjf4ZGcjUz/mdoBADXpy5umvCg6AAAAABJRU5ErkJggg==
```

在上面的Data URI中，data表示取得数据的协定名称，image/png 是数据类型名称，base64 是数据的编码方法，逗号后面就是这个image/png文件base64编码后的数据。

```
Data URI的格式规范:

data:[<mime type>][;charset=<charset>][;<encoding>],<encoded data>
1.  data ：协议名称；
2.  [<mime type>] ：可选项，数据类型（image/png、text/plain等）
3.  [;charset=<charset>] ：可选项，源文本的字符集编码方式
4.  [;<encoding>] ：数据编码方式（默认US-ASCII，BASE64两种）
5.  ,<encoded data> ：编码后的数据
```

```
Data URI scheme支持的类型有：

data:,                              文本数据
data:text/plain,                    文本数据
data:text/html,                     HTML代码
data:text/html;base64,              base64编码的HTML代码
data:text/css,                      CSS代码
data:text/css;base64,               base64编码的CSS代码
data:text/javascript,               Javascript代码
data:text/javascript;base64,        base64编码的Javascript代码
data:image/gif;base64,              base64编码的gif图片数据
data:image/png;base64,              base64编码的png图片数据
data:image/jpeg;base64,             base64编码的jpeg图片数据
data:image/x-icon;base64,           base64编码的icon图片数据

base64简单地说，它把一些 8-bit 数据翻译成标准 ASCII 字符.
```

#### 例子

```
data:,hello
(copy to browser address will display: 'hello!')
------------------------------------------------------------------------------------------------

data:text/plain,hello!
(copy to browser address will display: 'hello!')
------------------------------------------------------------------------------------------------

data:text/html,www.baidu.com
(copy to browser address will display: 'www.baidu.com')
------------------------------------------------------------------------------------------------

data:text/html;base64,aHR0cDovL3d3dy5iYWlkdS5jb20=
(copy to browser address will display: 'http://www.baidu.com')
------------------------------------------------------------------------------------------------

data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAkUlEQVQ4jWOUO87Q8J+RoZ6BDMD4n6GRUfYEw39yNMMAEyWaqW9AoUw9wyPz/3BswWfPwMDAwLBKcx9crFCmHrcB6KBPaQFpLkAHMuwKGDaiAxZCNhRKNzA8+fmAdBcga5JhVyDHgPsM/U8bCDkQfxj0P2nE63yCBjAwMDAU3UvAKz8ckjLjf4ZGcjUz/mdoBADXpy5umvCg6AAAAABJRU5ErkJggg==
(copy to browser address will display a image)
```

网上有很多免费的base64 编码和解码的工具，在PHP中可以用函数base64_encode() 进行编码，如:

```
echo base64encode(file_get_contents(‘wg.png’));
```

目前，IE8、Firfox、Chrome、Opera浏览器都支持这种小文件嵌入。

举个图片的例子, 网页中一张图片可以这样显示：

```
<img src="http://mail.163.com/images/x.png" />
```

也可以这样显示：

```
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAJAQMAAADaX5RTAAAAA3NCSVQICAjb4U/gAAAABlBMVEX///+ZmZmOUEqyAAAAAnRSTlMA/1uRIrUAAAAJcEhZcwAACusAAArrAYKLDVoAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDkvMjAvMTIGkKG+AAAAHHRFWHRTb2Z0d2FyZQBBZG9iZSBGaXJld29ya3MgQ1M26LyyjAAAAB1JREFUCJljONjA8LiBoZyBwY6BQQZMAtlAkYMNAF1fBs/zPvcnAAAAAElFTkSuQmCC" />
```



#### Data URI Scheme优缺点

优点：

```
1. 减少资源请求链接数。
2. 当访问外部资源很麻烦或受限时，可以很好的利用Data URI Scheme
```

缺点：

```
1. Data URL形式的图片不会被浏览器缓存，这意味着每次访问这样页面时都被下载一次，
   但可通过在css文件的background-image样式规则使用Data URI Scheme，使其随css文件一同被浏览器缓存起来）。
2. Base64编码的数据体积通常是原数据的体积4/3，
   也就是Data URL形式的图片会比二进制格式的图片体积大1/3。
3. 移动端性能比较低。 
```

#### Data URI Scheme适用场景：

```
1. 当访问外部资源很麻烦或受限时。
2. 当图片是在服务器端用程序动态生成，每个访问用户显示的都不同时。
3. 当图片的体积太小，占用一个HTTP会话不是很值得时。
```

#### base64

参考 python module base64

http://baike.baidu.com/link?url=70MjSwBpM2r_woKdjRXSO3SUD95DUwCairxxoszaRpOWmkx5aBeehNGKTks38_WnrrkbdZ7tUI_YG_Jr9h8iBa