

# module base64  



## Base64 简介

标准的Base64并不适合直接放在URL里传输，因为URL编码器会把标准Base64中的“`/`”和“`+`”字符变为形如“`%XX`”的形式，而这些“`%`”号在存入数据库时还需要再进行转换，因为ANSI SQL中已将“`%`”号用作通配符。

为解决此问题，可采用一种用于**URL的改进Base64编码**，它在末尾填充'`=`'号，并将标准Base64中的“`+`”和“`/`”分别改成了“`-`”和“`_`”，这样就免去了在URL编解码和数据库存储时所要作的转换，避免了编码信息长度在此过程中的增加，并统一了数据库、表单等处对象标识符的格式。

另有一种用于**正则表达式的改进Base64变种**，它将“`+`”和“`/`”改成了“`!`”和“`-`”，因为“`+`”,“`*`”以及前面在IRCu中用到的“[”和“]”在正则表达式中都可能具有特殊含义。

此外还有一些变种，它们将“`+/`”改为“`_-`”或“`._`”（用作编程语言中的标识符名称）或“`.-`”（用于XML中的Nmtoken）甚至“`_:`”（用于XML中的Name）。

Base64要求把每三个8Bit的字节转换为四个6Bit的字节（`3*8 = 4*6 = 24`），然后把6Bit再添两位高位0，组成四个8Bit的字节，也就是说，转换后的字符串理论上将要比原来的长1/3。



### 规则

关于这个编码的规则：

1. 把3个字符变成4个字符。
2. 每76个字符加一个换行符。
3. 最后的结束符也要处理。



### The Base64 Alphabet

转换前 11111111, 11111111, 11111111 （二进制）

转换后 00111111, 00111111, 00111111, 00111111 （二进制）

上面的三个字节是原文，下面的四个字节是转换后的Base64编码，其前两位均为0。

转换后，我们用一个码表来得到我们想要的字符串（也就是最终的Base64编码），这个表是这样的：（摘自RFC2045）

转换表

Table 1: **The Base64 Alphabet**

| **索引** | **对应字符** | **索引** | **对应字符** | **索引** | **对应字符** | **索引** | **对应字符** |
| ------ | -------- | ------ | -------- | ------ | -------- | ------ | -------- |
| 0      | **A**    | 17     | **R**    | 34     | **i**    | 51     | **z**    |
| 1      | **B**    | 18     | **S**    | 35     | **j**    | 52     | **0**    |
| 2      | **C**    | 19     | **T**    | 36     | **k**    | 53     | **1**    |
| 3      | **D**    | 20     | **U**    | 37     | **l**    | 54     | **2**    |
| 4      | **E**    | 21     | **V**    | 38     | **m**    | 55     | **3**    |
| 5      | **F**    | 22     | **W**    | 39     | **n**    | 56     | **4**    |
| 6      | **G**    | 23     | **X**    | 40     | **o**    | 57     | **5**    |
| 7      | **H**    | 24     | **Y**    | 41     | **p**    | 58     | **6**    |
| 8      | **I**    | 25     | **Z**    | 42     | **q**    | 59     | **7**    |
| 9      | **J**    | 26     | **a**    | 43     | **r**    | 60     | **8**    |
| 10     | **K**    | 27     | **b**    | 44     | **s**    | 61     | **9**    |
| 11     | **L**    | 28     | **c**    | 45     | **t**    | 62     | **+**    |
| 12     | **M**    | 29     | **d**    | 46     | **u**    | 63     | **/**    |
| 13     | **N**    | 30     | **e**    | 47     | **v**    |        |          |
| 14     | **O**    | 31     | **f**    | 48     | **w**    |        |          |
| 15     | **P**    | 32     | **g**    | 49     | **x**    |        |          |
| 16     | **Q**    | 33     | **h**    | 50     | **y**    |        |          |



### 例子

转换前 10101101,10111010,01110110

转换后 00101011, 00011011 ,00101001 ,00110110

十进制 43 27 41 54

对应码表中的值 r b p 2

所以上面的24位编码，编码后的Base64值为 rbp2

解码同理，把 rbq2 的二进制位连接上再重组得到三个8位值，得出原码。

（解码只是编码的逆过程，有关MIME的RFC还有很多）

> 第一个字节，根据源字节的第一个字节处理。
>
> 规则：源第一字节右移两位，去掉低2位，高2位补零。
>
> 既：00 + 高6位
>
> 第二个字节，根据源字节的第一个字节和第二个字节联合处理。
>
> 规则如下，第一个字节高6位去掉然后左移四位，第二个字节右移四位
>
> 即：源第一字节低2位 + 源第2字节高4位
>
> 第三个字节，根据源字节的第二个字节和第三个字节联合处理，
>
> 规则第二个字节去掉高4位并左移两位（得高6位），第三个字节右移6位并去掉高6位（得低2位），相加即可
>
> 第四个字节，规则，源第三字节去掉高2位即可

用更接近于编程的思维来说，编码的过程是这样的：

//第一个字符通过右移2位获得第一个目标字符的Base64表位置，根据这个数值取到表上相应的字符，就是第一//个目标字符。

//然后将第一个字符与0x03(00000011)进行与(&)操作并左移4位,接着第二个字符右移4位与前者相或(|)，即获得第二个目标字符。

//再将第二个字符与0x0f(00001111)进行与(&)操作并左移2位,接着第三个字符右移6位与前者相或(|)，获得第三个目标字符。

//最后将第三个字符与0x3f(00111111)进行与(&)操作即获得第四个目标字符。

//在以上的每一个步骤之后，再把结果与 0x3F 进行 AND 位操作，就可以得到编码后的字符了。

可是等等……聪明的你可能会问到，原文的字节数量应该是3的倍数啊，如果这个条件不能满足的话，那该怎么办呢？

我们的解决办法是这样的：原文剩余的字节根据编码规则继续单独转(1变2,2变3;不够的位数用0补全)，再用=号补满4个字节。这就是为什么有些Base64编码会以一个或两个等号结束的原因，但等号最多只有两个。因为：

一个原字节至少会变成两个目标字节

所以余数任何情况下都只可能是0，1，2这三个数中的一个。如果余数是0的话，就表示原文字节数正好是3的倍数（最理想的情况）。如果是1的话，转成2个Base64编码字符，为了让Base64编码是4的倍数，就要补2个等号；同理，如果是2的话，就要补1个等号。







## help(base64)

```
>>> import base64
>>> help(base64)

Help on module base64:

NAME
    base64 - Base16, Base32, Base64 (RFC 3548), Base85 and Ascii85 data encodings

MODULE REFERENCE
    http://docs.python.org/3.4/library/base64
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

FUNCTIONS
    a85decode(b, *, foldspaces=False, adobe=False, ignorechars=b' \t\n\r\x0b')
        Decode an Ascii85 encoded byte string.
        
        s is the byte string to decode.
        
        foldspaces is a flag that specifies whether the 'y' short sequence should be
        accepted as shorthand for 4 consecutive spaces (ASCII 0x20). This feature is
        not supported by the "standard" Adobe encoding.
        
        adobe controls whether the input sequence is in Adobe Ascii85 format (i.e.
        is framed with <~ and ~>).
        
        ignorechars should be a byte string containing characters to ignore from the
        input. This should only contain whitespace characters, and by default
        contains all whitespace characters in ASCII.
    
    a85encode(b, *, foldspaces=False, wrapcol=0, pad=False, adobe=False)
        Encode a byte string using Ascii85.
        
            b is the byte string to encode. The encoded byte string is returned.
        
            foldspaces is an optional flag that uses the special short sequence 'y'
            instead of 4 consecutive spaces (ASCII 0x20) as supported by 'btoa'. This
            feature is not supported by the "standard" Adobe encoding.
        
            wrapcol controls whether the output should have newline ('
        ') characters
            added to it. If this is non-zero, each output line will be at most this
            many characters long.
        
            pad controls whether the input string is padded to a multiple of 4 before
            encoding. Note that the btoa implementation always pads.
        
            adobe controls whether the encoded byte sequence is framed with <~ and ~>,
            which is used by the Adobe implementation.
    
    b16decode(s, casefold=False)
        Decode a Base16 encoded byte string.
        
        s is the byte string to decode.  Optional casefold is a flag
        specifying whether a lowercase alphabet is acceptable as input.
        For security purposes, the default is False.
        
        The decoded byte string is returned.  binascii.Error is raised if
        s were incorrectly padded or if there are non-alphabet characters
        present in the string.
    
    b16encode(s)
        Encode a byte string using Base16.
        
        s is the byte string to encode.  The encoded byte string is returned.
    
    b32decode(s, casefold=False, map01=None)
        Decode a Base32 encoded byte string.
        
        s is the byte string to decode.  Optional casefold is a flag
        specifying whether a lowercase alphabet is acceptable as input.
        For security purposes, the default is False.
        
        RFC 3548 allows for optional mapping of the digit 0 (zero) to the
        letter O (oh), and for optional mapping of the digit 1 (one) to
        either the letter I (eye) or letter L (el).  The optional argument
        map01 when not None, specifies which letter the digit 1 should be
        mapped to (when map01 is not None, the digit 0 is always mapped to
        the letter O).  For security purposes the default is None, so that
        0 and 1 are not allowed in the input.
        
        The decoded byte string is returned.  binascii.Error is raised if
        the input is incorrectly padded or if there are non-alphabet
        characters present in the input.
    
    b32encode(s)
        Encode a byte string using Base32.
        
        s is the byte string to encode.  The encoded byte string is returned.
    
    
    b64decode(s, altchars=None, validate=False)
        Decode a Base64 encoded byte string.
        
        s is the byte string to decode.  Optional altchars must be a
        string of length 2 which specifies the alternative alphabet used
        instead of the '+' and '/' characters.
        
        The decoded string is returned.  A binascii.Error is raised if s is
        incorrectly padded.
        
        If validate is False (the default), non-base64-alphabet characters are
        discarded prior to the padding check.  If validate is True,
        non-base64-alphabet characters in the input result in a binascii.Error.
    
    b64encode(s, altchars=None)
        Encode a byte string using Base64.
        
        s is the byte string to encode.  Optional altchars must be a byte
        string of length 2 which specifies an alternative alphabet for the
        '+' and '/' characters.  This allows an application to
        e.g. generate url or filesystem safe Base64 strings.
        
        The encoded byte string is returned.
    
    b85decode(b)
        Decode base85-encoded byte array
    
    b85encode(b, pad=False)
        Encode an ASCII-encoded byte array in base85 format.
        
        If pad is true, the input is padded with "^@" so its length is a multiple of
        4 characters before encoding.
    
    decode(input, output)
        Decode a file; input and output are binary files.
    
    decodebytes(s)
        Decode a bytestring of base-64 data into a bytestring.
    
    encode(input, output)
        Encode a file; input and output are binary files.
    
    encodebytes(s)
        Encode a bytestring into a bytestring containing multiple lines
        of base-64 data.
    
    standard_b64decode(s)
        Decode a byte string encoded with the standard Base64 alphabet.
        
        s is the byte string to decode.  The decoded byte string is
        returned.  binascii.Error is raised if the input is incorrectly
        padded or if there are non-alphabet characters present in the
        input.
    
    standard_b64encode(s)
        Encode a byte string using the standard Base64 alphabet.
        
        s is the byte string to encode.  The encoded byte string is returned.
    
    urlsafe_b64decode(s)
        Decode a byte string encoded with the standard Base64 alphabet.
        
        s is the byte string to decode.  The decoded byte string is
        returned.  binascii.Error is raised if the input is incorrectly
        padded or if there are non-alphabet characters present in the
        input.
        
        The alphabet uses '-' instead of '+' and '_' instead of '/'.
    
    urlsafe_b64encode(s)
        Encode a byte string using a url-safe Base64 alphabet.
        
        s is the byte string to encode.  The encoded byte string is
        returned.  The alphabet uses '-' instead of '+' and '_' instead of
        '/'.

DATA
    __all__ = ['encode', 'decode', 'encodebytes', 'decodebytes', 'b64encod...

FILE
    /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/base64.py

(END)
```





## dir(base64)

```
>>> import base64
>>> dir(base64)
['MAXBINSIZE', 'MAXLINESIZE', '_85encode', '_A85END', '_A85START', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_a85chars', '_a85chars2', '_b32alphabet', '_b32rev', '_b32tab2', '_b85alphabet', '_b85chars', '_b85chars2', '_b85dec', '_bytes_from_decode_data', '_input_type_check', '_urlsafe_decode_translation', '_urlsafe_encode_translation', 'a85decode', 'a85encode', 'b16decode', 'b16encode', 'b32decode', 'b32encode', 'b64decode', 'b64encode', 'b85decode', 'b85encode', 'binascii', 'bytes_types', 'decode', 'decodebytes', 'decodestring', 'encode', 'encodebytes', 'encodestring', 'main', 're', 'standard_b64decode', 'standard_b64encode', 'struct', 'test', 'urlsafe_b64decode', 'urlsafe_b64encode']
```



## base64模块方法

Python base64模块真正用的上的方法只有8个，分别是`encode`, `decode`, `encodestring`, `decodestring`, `b64encode`,`b64decode`, `urlsafe_b64decode`,`urlsafe_b64encode`。

他们8个可以两两分为4组:

1. `encode`,`decode`一组，专门用来编码和解码文件的,也可以对StringIO里的数据做编解码；
2. `encodestring`,`decodestring`一组，专门用来编码和解码字符串；
3.  `b64encode` , `b64decode`一组，用来编码和解码字符串，并且有一个替换符号字符的功能。这个功能是这样的：因为base64编码后的字符除了英文字母和数字外还有三个字符 `+` `/` `=`, 其中`=`只是为了补全编码后的字符数为4的整数，而`+`和`/`在一些情况下需要被替换的，`b64encode`和`b64decode`正是提供了这样的功能。至于什么情况下`+`和`/`需要被替换，最常见的就是对url进行base64编码的时候。
4. `urlsafe_b64encode` , `urlsafe_b64decode` 一组，这个就是用来专门对url进行base64编解码的，实际上也是调用的前一组函数。





### encode

```
Help on function encode in module base64:

encode(input, output)
    Encode a file; input and output are binary files.
```



### decode

```
Help on function decode in module base64:

decode(input, output)
    Decode a file; input and output are binary files.
```



### encodestring

```
Help on function encodestring in module base64:

encodestring(s)
    Legacy alias of encodebytes().
```



### decodestring

```
Help on function decodestring in module base64:

decodestring(s)
    Legacy alias of decodebytes().
```



### b64encode

```
Help on function b64encode in module base64:

b64encode(s, altchars=None)
    Encode a byte string using Base64.
    
    s is the byte string to encode.  Optional altchars must be a byte
    string of length 2 which specifies an alternative alphabet for the
    '+' and '/' characters.  This allows an application to
    e.g. generate url or filesystem safe Base64 strings.
    
    The encoded byte string is returned.
```

#### 例子:

```
>>> import base64
>>> base64.b64encode(b'How are you?')			
b'SG93IGFyZSB5b3U/'
>>> base64.b64decode(b'SG93IGFyZSB5b3U/')
b'How are you?'
```



### b64decode

```
Help on function b64decode in module base64:

b64decode(s, altchars=None, validate=False)
    Decode a Base64 encoded byte string.
    
    s is the byte string to decode.  Optional altchars must be a
    string of length 2 which specifies the alternative alphabet used
    instead of the '+' and '/' characters.
    
    The decoded string is returned.  A binascii.Error is raised if s is
    incorrectly padded.
    
    If validate is False (the default), non-base64-alphabet characters are
    discarded prior to the padding check.  If validate is True,
    non-base64-alphabet characters in the input result in a binascii.Error.
```

#### 例子:

```
>>> import base64
>>> base64.b64encode(b'How are you?')			
b'SG93IGFyZSB5b3U/'
>>> base64.b64decode(b'SG93IGFyZSB5b3U/')
b'How are you?'
```









### urlsafe_b64decode

```
Help on function urlsafe_b64decode in module base64:

urlsafe_b64decode(s)
    Decode a byte string encoded with the standard Base64 alphabet.
    
    s is the byte string to decode.  The decoded byte string is
    returned.  binascii.Error is raised if the input is incorrectly
    padded or if there are non-alphabet characters present in the
    input.
    
    The alphabet uses '-' instead of '+' and '_' instead of '/'.
```

#### 例子:

```
>>> import base64
>>> base64.urlsafe_b64encode(b'http://www.baidu.com')
b'aHR0cDovL3d3dy5iYWlkdS5jb20='
>>> base64.urlsafe_b64decode(b'aHR0cDovL3d3dy5iYWlkdS5jb20=')
b'http://www.baidu.com'
```











### urlsafe_b64encode

```
Help on function urlsafe_b64encode in module base64:

urlsafe_b64encode(s)
    Encode a byte string using a url-safe Base64 alphabet.
    
    s is the byte string to encode.  The encoded byte string is
    returned.  The alphabet uses '-' instead of '+' and '_' instead of
    '/'.
```

#### 例子:

```
>>> import base64
>>> base64.urlsafe_b64encode(b'http://www.baidu.com')
b'aHR0cDovL3d3dy5iYWlkdS5jb20='
>>> base64.urlsafe_b64decode(b'aHR0cDovL3d3dy5iYWlkdS5jb20=')
b'http://www.baidu.com'
```