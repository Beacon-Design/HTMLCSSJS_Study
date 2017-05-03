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

