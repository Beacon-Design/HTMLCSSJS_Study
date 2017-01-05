# Input & Touch Keyboard

# 触屏键盘设计准则

 [Reference 1](https://www.smashingmagazine.com/2013/08/guide-to-designing-touch-keyboards-with-cheat-sheet/) [Reference 2](http://baymard.com/blog/mobile-touch-keyboards) [Reference 3](http://mxd.tencent.com/%E8%A7%A6%E5%B1%8F%E9%94%AE%E7%9B%98%E8%AE%BE%E8%AE%A1%E5%87%86%E5%88%99%EF%BC%88%E5%86%85%E9%99%84%E7%BB%9D%E5%AF%86%E5%B0%8F%E6%8A%84%EF%BC%89%E3%80%90%E8%AF%91%E3%80%91)

1. 适当的使用自动更正的字典
2. 贴切的将字母自动大写
3. 提示输入类型
4. 保持标签顺序
5. 保持自定义键盘的一致性



### 1. 当词典匮乏时，禁用自动更正

**自动更正通常在以下情况表现非常糟糕：缩写，街道名称，email地址以及其他词典里没有的词汇。**

**关于自动更正的一个主要问题就是，用户通常不会注意到更正（因为用户通常关注的是他们正在输入什么，而不是已经输入的内容）。**

如果更正是正确的，那就没问题，但如果更正是错误的，由于被试者并没有注意到自动更正，原本有效的地址信息被自动更正为无效信息并被提交。在没有地址验证的网站上，这会导致订单被送到错误的地址，除非被试者特意仔细的查看订单确认页（毕竟，自动更正的信息通常看起来与输入的信息非常相似，这也使得用户很少会注意到信息是错误的）

自动更正在其他场景还是有用处的，会将无效数据更正为有效数据。因此，并不推荐在所有场景（如评论区）禁用自动更正。相反，**要慎重使用自动更正，只在词典匮乏的场景禁用。**这通常包括各式各样的正确名称（街道，城市，人物）以及其他标识（email地址，优惠券代码，等等）。

你可以在 `<input>` 标签上增加 `<autocorrect>` 并设置为关闭，来禁用自动更正，就像这样：

```html
<input type=“text” autocorrect=“off” />
```



### 2. 弹出合适的键盘

**弹出不合适的键盘会降低输入速度，用户经常会因为标准键盘上数字的很小的点击区域以及间距而打错很长一串数字。**

智能手机上触屏键盘的一个很大局限就是它的尺寸。字符本身也都是非常小的。事实上，在iPhone4竖屏时一个字符的大小是4x5.9毫米。

再来对照一下苹果自己的设计准则，其中提到所有可点击的界面元素至少要有6.85x6.85毫米，因为任何小于这个尺寸的元素点击准确度都会非常的差（微软和诺基亚同样制定了最小点击区域为7x7毫米）。可以预见，这将会导致拼写错误。

通过更改输入框代码的一到两个属性，你就可以让用户的手机自动显示所需输入的最合适的键盘。例如，你可以为信用卡号输入框调用数字键盘，为电话号码输入框调用拨号键盘，为电子邮件地址输入框调用电子邮件的键盘。这样可以节省用户必须切换传统键盘的时间，并且在输入数字的场景中，最大限度的减少输入错误，因为这样的**专用键盘按键尺寸更大，会减少意外输错的机率。**

在iOS中，数字键盘的点击区域要比标准键盘大471%（数字键盘209x108像素vs标准键盘52x76像素）。更重要的是，我们发现在数字输入框里采用数字键盘时错别字明显减少。这会导致更少的验证错误，反过来，也可以将网站引向一个更好更无缝的购物体验。这对于长数字队列尤为明显，比如电话号码以及信用卡号。

**调用专用键盘的另一个好处就是可以表明需要输入的是什么内容，如果输入框标题滑出视线范围或是用户不确定要输入什么的时候，这会很有用。**然而，数字键盘也有一定的局限性，因为它不允许用户输入拼音字符，只有少量特殊字符或分隔符，也可能连这个都没有。所以，只有最合适的时候再调用这样的键盘，这很重要，比如输入电话号码、邮政编码、信用卡号以及信用卡安全码。同样的，在调用键盘时，确保你给出的格式样例是可以复制的。

根据给出的样例格式（比如“555-555-5555”）输入电话号码在iOS上是不可能的，因为调出的键盘是没有横划线的。（有趣的是，在Android系统上输入是可以的，这也说明了为什么在多个平台测试有助于确保在格式样例只在有些平台上必须。）

技术上来说，有很多种方式可以调出数字键盘，每种键盘之间略有差别（如拨号键盘和数字键盘），不同平台间行为也会有轻微的不同（iOS，Android等）。大体来说有两种HTML属性可以调用数字键盘，分别是type和pattern属性。

Type属性承载语义的含义，仅仅当输入时有合适的类型可调用时才会被用到，这主要是针对电话号码和电子邮件地址的场景。不过对于数字输入，更推荐使用pattern属性来替代。（注意如果你仅仅是想要浏览器调用键盘，并不强制格式，可以加入novalidate属性。）

针对任何电话号码框，用如下代码：

```html
<input type=“tel” />
```

针对其他你想要调用数字键盘的输入框，用如下代码：

```html
<input type=“text” pattern=“\d*” novalidate />
```

针对任何电子邮件地址框，用如下代码：

```html
<input type=“email” />
```

各种数字键盘之间会有一些区别，在不同平台之间也会有一些不同。例如，在iOS平台上，上述代码调出的电话键盘可以让用户输入数字以及少量电话相关的特殊字符和分隔符，而调起的数字键盘只能输入数字。与此同时，在Android平台上，调起的电话键盘则有着更多的特殊字符，支持更多格式的电话号码。

但是，由pattern属性调起数字键盘在Android上根本不支持，相反，它只会调起常用的字母键盘。虽然在iOS和Android平台上，你都可以使用type=“number”调起数字键盘，但将type设置为number带有语义含义，在很多场景下并不合适（比如信用卡号是一个数字队列，不单单是一个数字）。

所以，我们推荐更为保守的策略，使用pattern=“\d*”，这样在iOS平台上可以有更好的体验，在其他不支持该属性的平台上也不会有什么影响。（当然了，如果输入框就是针对一个数字的，比如价格或是数量，那么显然应该使用type=“number”了。）



### 3. 保持一致，调用合适的键盘

如果一个输入框调用了专用键盘而其他类似的输入框却没有，那么在没有调用专用键盘时用户会感到困惑，并开始质疑这个输入框所需输入的类型。

例如，当看到“信用卡安全码”输入框弹出了标准键盘时，被试者开始怀疑这是否就是填写信用卡背面的那三个数字，或是印在卡上的其他字符串。



### 4. 兑现“上一项”和“下一项”按钮的行为

**如果“上一项”和“下一项”按钮把用户带去了不合逻辑顺序的输入框，用户会很烦恼和困惑。**

在测试中，被试者在未能兑现“上一项”“下一项”按钮行为的网站上感到烦恼。用户预期的行为很简单：当用户点击“下一项”按钮，他们会预期跳到表单中下一个合乎逻辑的输入框，没有其他变化，甚至提交表单。“上一项”按钮也一样，当然是换个相反的方向。

这不仅仅是**需要有正确的标签序列**（虽说这是一个好的开始）。当需要依赖于用户先前的选择处理动态输入控件时，事情往往会出差错。在这些情况下，我们已经看到用户数据被删除或是标签序列被违反。**我们也必须要格外注意自定义表单的接口。例如，定制化的状态选择器不属于标签序列（因为从技术上来说它并不是一个输入元素），所以用户就会跳过这个状态控件。**

这些按钮的功能基本上是充当键盘上tab键的移动版；所以，它们应该采用和电脑键盘tab一样的序列规则。它们应该提供从一个输入框到下一个输入框的快捷方式，不需要任何点击（不论是鼠标还是手指）。这在手机上是尤为重要的，因为当键盘呼出的时候，屏幕空间是有限的，下一个输入框可能被部分遮挡，这个时候“下一项”按钮则用起来很方便。所以，尽管“上一项”和“下一项”按钮有可能不会被所有用户用到，但禁用这些按钮的行为会导致很严重的后果。

**只要代码是清晰的，手机浏览器会默认将输入框出现的顺序作为标签序列。**



### 5. 在适当的情况下，禁用自动大写

几乎所有的被试者都认为他们的电子邮件地址必须要小写，所以这项数据自动大写会给整个过程带来不必要的麻烦。

**智能手机默认会把标准文本输入框的首字母大写，这在大部分情况下是合适的。然而，在有些情况下禁用自动大写是更合适的，特别是像电子邮件地址这种绝大多数用户都以为要小写的情况。**

**推荐大家在电子邮件或是其他合适的场景（如网址URL）禁用自动大写。**

可以在 `<input>` 标签上加入 `autocapitalize` 属性并设置为 `off` ，来禁用自动大写。

```html
<input tyoe=“text” autocapitalize=“off” />
```

针对电子邮件输入框，你也可以设置一个 `type` 属性为 `email` ：

```html
<input tyoe=“email” autocapitalize=“off” />
```

**在iOS系统上，设置 `type` 属性为 `email` 将会自动禁用自动大写。然而，最好仍然设置 `autocapitalize` 属性，因为这不仅在iOS系统上奏效，而且在其他还不支持email输入框类型或是实现方式不同的平台也可以使用。**



> 虽然这些基本原理看上去是显而易见的，但是要记得全球最大的移动电子商务网站中98%的网站违反了至少一条。70%的网站违反了两条甚至更多的“基础“触摸键盘准则。事实上，24%的网站根本没有为触屏键盘输入做过什么优化
>
> 不遵守设计准则的一个原因可能是，针对一个大型网站所做的全局测试需要去发现所有的明显缺陷——故而，理想情况下的第三项建议中提到调用键盘的一致性问题，是不必要被提及的。另外一个原因是，在前一篇文章中提到的，手机和触屏界面是一个相对较新的平台，它的全新的界面理论需要大家去关注无数的小的细节——这些细节对于我们网页设计师和开发者来说还不习惯去主动寻找和设计。



------



# Touch Keyboard Types

HTML5 code and demos for invoking different touch keyboards depending on input type.

[Reference](http://baymard.com/labs/touch-keyboard-types)

**Code & Demos**  / Updated October 11, 2016

### E-mail field

Disable auto-correct and disable auto-capitalization. Invoke special @ keyboard.

```html
 <input type="email" autocapitalize="off" autocorrect="off" autocomplete="email">
```

### Phone field

Invoke special phone keyboard. *(Note: iOS doesn't allow input of special characters such as parenthesis and dash with the phone keyboard. Thus, never require phone numbers to be formatted with such characters.)*

```html
<input type="tel" autocorrect="off" autocomplete="tel">
```

### Name field

Disable auto-correct. *(Note: while it is recommended to use [a single name field](http://baymard.com/blog/mobile-form-usability-single-input-fields), if you split it across multiple fields, be sure to assign the [appropriate autocomplete values](https://html.spec.whatwg.org/multipage/forms.html#attr-fe-autocomplete-name).)*

```html
<input type="text" autocorrect="off" autocomplete="name">
```

### Address line fields

Disable auto-correct. *(Note: be sure to update the autocomplete attribute accordingly if using multiple address line fields.)*

```html
<input type="text" autocorrect="off" autocomplete="address-line1">
```

### City

Disable auto-correct.

```html
<input type="text" autocorrect="off" autocomplete="address-level2">
```

### State

Disable auto-correct.

```html
<input type="text" autocorrect="off" autocomplete="address-level1">
```

### ZIP code field

Set input pattern to numeric input. *(Note: Argentina, Canada, Netherlands, and UK, may use letters in their postal code. To support these, dynamically change the input pattern depending on selected country. Also, for the numeric keyboard to be invoked on all Android devices, the field type must be changed to type=number, however, this may cause issues with leading zeroes in some browser versions – therefore if changing to type=number, make absolutely sure to handle these exceptions.)*

```html
<input type="text" inputmode="numeric" pattern="[0-9]*" novalidate autocorrect="off" autocomplete="postal-code">
```

### Credit card number field

Numeric keyboard. *(Note: for the numeric keyboard to be invoked on all Android devices, the field type must be changed to type=number, however, this may cause issues with leading zeroes in some browser versions – therefore if changing to type=number, make absolutely sure to handle these exceptions.)*

```html
<input type="text" inputmode="numeric" pattern="[0-9]*" novalidate autocorrect="off" autocomplete="cc-number">
```

### Credit card security code field

Numeric keyboard. *(Note: for the numeric keyboard to be invoked on all Android devices, the field type must be changed to type=number, however, this may cause issues with leading zeroes in some browser versions – therefore if changing to type=number, make absolutely sure to handle these exceptions.)*

```html
<input type="text" inputmode="numeric" pattern="[0-9]*" novalidate autocorrect="off" autocomplete="cc-csc">
```

### Quantity field

Semantic numeric keyboard.

```html
<input type="number">
```

### Month input

```html
<input type="month" name="month">
```

### Date field

Date picker keyboard. *(Note: you may want to implement an actual calendar date picker.)*

> 在iOS上的 date input 类型会提示显示一个日期选择器。不幸的是，Android浏览器还未支持任何datetime 的input类型。

```html
<input type="date">
```

### Time Input

使用time类型时会提示iOS显示一个简单的拾取器来选择小时和分钟。

```html
<input type="time" name="time">
```

### Submit button

For the 'Go' button on keyboard to work, avoid using *type=button*. *(Thanks to Todd Gilbert for the tip.)*

```html
<input type="submit">
```

### URL input

url  input 类型可以用来帮助用户输入网址

```html
<input type="url" name="url">
```