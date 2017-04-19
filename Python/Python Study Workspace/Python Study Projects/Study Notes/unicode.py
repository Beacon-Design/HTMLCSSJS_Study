# encoding=utf-8
import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"你好")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print (text)

print('''---------------------------------------------------------------------------
In Python 3.X there are three string types: str is used for Unicode text (including
ASCII), bytes is used for binary data (including encoded text), and bytearray is a
mutable variant of bytes. Files work in two modes: text, which represents content
as str and implements Unicode encodings, and binary, which deals in raw bytes
and does no data translation.

In Python 2.X, unicode strings represent Unicode text, str strings handle both 8-
bit text and binary data, and bytearray is available in 2.6 and later as a back-port
from 3.X. Normal files’ content is simply bytes represented as str, but a codecs
module opens Unicode text files, handles encodings, and represents content as
unicode objects.

''')



