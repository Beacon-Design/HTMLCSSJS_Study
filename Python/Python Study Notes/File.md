

# File

In short, the built-in open function creates a Python file object, which serves as a link to a file residing on your machine. After calling open, you can transfer strings of data to and from the associated external file by calling the returned file object’s methods.

they export only methods for common file-processing tasks. Most file methods are concerned with performing input from and output to the external file associated with a file object, but other file methods allow us to seek to a new position in the file, flush output buffers, and so on.

## Common file operations

```
Common file operations

Operation                         Interpretation

output = open(r'C:\spam', 'w')         Create output file ('w' means write)
input = open('data', 'r')              Create input file ('r' means read)
input = open('data')                   Same as prior line ('r' is the default)
aString = input.read()                 Read entire file into a single string
aString = input.read(N)                Read up to next N characters (or bytes) into a string
aString = input.readline()             Read next line (including \n newline) into a string
aList = input.readlines()              Read entire file into list of line strings (with \n)
output.write(aString)                  Write a string of characters (or bytes) into file
output.writelines(aList)               Write all line strings in a list into file
output.close()                         Manual close (done for you when file is collected)
output.flush()                         Flush output buffer to disk without closing
anyFile.seek(N)                        Change file position to offset N for next operation
for line in open('data'): use line     File iterators read line by line
open('f.txt', encoding='latin-1')      Python 3.X Unicode text files (str strings)
open('f.bin', 'rb')                    Python 3.X bytes files (bytes strings)
codecs.open('f.txt', encoding='utf8')  Python 2.X Unicode text files (unicode strings)
open('f.bin', 'rb')                    Python 2.X bytes files (str strings)
```

## 常用的函数

file 对象使用 `open()` 函数来创建，下表列出了 file 对象常用的函数：

| 序号   | 方法及描述                                    |
| ---- | ---------------------------------------- |
| 1    | [`file.close()`](http://www.runoob.com/python/file-close.html) 关闭文件。关闭后文件不能再进行读写操作。 |
| 2    | [`file.flush()`](http://www.runoob.com/python/file-flush.html) 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。 |
| 3    | [`file.fileno()`](http://www.runoob.com/python/file-fileno.html) 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。 |
| 4    | [`file.isatty()`](http://www.runoob.com/python/file-isatty.html) 如果文件连接到一个终端设备返回 True，否则返回 False。 |
| 5    | [`file.next()`](http://www.runoob.com/python/file-next.html) 返回文件下一行。 |
| 6    | [`file.read([size])`](http://www.runoob.com/python/python-file-read.html) 从文件读取指定的字节数，如果未给定或为负则读取所有。 |
| 7    | [`file.readline([size])`](http://www.runoob.com/python/file-readline.html) 读取整行，包括 "\n" 字符。 |
| 8    | [`file.readlines([sizehint]) `](http://www.runoob.com/python/file-readlines.html)读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比sizhint较大, 因为需要填充缓冲区。 |
| 9    | [`file.seek(offset[, whence])`](http://www.runoob.com/python/file-seek.html) 设置文件当前位置 |
| 10   | [`file.tell()`](http://www.runoob.com/python/file-tell.html) 返回文件当前位置。 |
| 11   | [`file.truncate([size])`](http://www.runoob.com/python/file-truncate.html) 截取文件，截取的字节通过size指定，默认为当前文件位置。 |
| 12   | [`file.write(str)`](http://www.runoob.com/python/python-file-write.html) 将字符串写入文件，没有返回值。 |
| 13   | [`file.writelines(sequence)`](http://www.runoob.com/python/file-writelines.html) 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。 |



### file.read()

**read()** 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。

```
fileObject.read([size]); 
```

**size** -- 从文件中读取的字节数。

返回从字符串中读取的字节。













### Opening Files

built-in `open()` function:

```
afile = open(filename, mode) 
afile.method()
```

> The first argument to open, the external filename, may include a platform-specific and absolute or relative directory path prefix. Without a directory path, the file is assumed to exist in the current working directory (i.e., where the script runs). the filename may also contain non-ASCII Unicode characters that Python automatically translates to and from the underlying platform’s encoding, or be provided as a pre-encoded byte string.
>
> The second argument to open, processing mode, is typically the string 'r' to open for text input (the default), 'w' to create and open for text output, or 'a' to open for appending text to the end (e.g., for adding to logfiles). The processing mode argument can specify additional options:
>
> - Adding a b to the mode string allows for binary data (end-of-line translations and 3.X Unicode encodings are turned off).
>
>
> - Adding a + opens the file for both input and output (i.e., you can both read and write to the same file object, often in conjunction with seek operations to reposition in the file).
>
> Both of the first two arguments to open must be Python strings. An optional third argument can be used to control output buffering—passing a zero means that output is unbuffered (it is transferred to the external file immediately on a write method call), and additional arguments may be provided for special types of files (e.g., an encoding for Unicode text files in Python 3.X).



## Using Files

Once you make a file object with open, you can call its methods to read from or write to the associated external file. In all cases, file text takes the form of strings in Python programs; reading a file returns its content in strings, and content is passed to the write methods as strings.

- **File iterators are best for reading lines** 

  > Though the reading and writing methods in the table are common, keep in mind that probably the best way to read lines from a text file today is to not read the file at all


- **Content is strings, not objects**

  > Notice  that **data read from a file always comes back to your script as a string,**
  >
  > **Python does not add any formatting and does not convert objects to strings automatically when you write data to a file** (you must send an already formatted string)


- **Files are buffered and seekable** 

  > **By default, output files are always buffered**, which means that text you write may not be transferred from memory to disk immediately—closing a file, or running its flush method, forces the buffered data to disk. You can avoid buffering with extra open arguments, but it may impede performance. Python files are also random-access on a byte offset basis—their seek method allows your scripts to jump around to read and write at specific locations.


- **close is often optional: auto-close on collection** 

  > Calling the file close method terminates your connection to the external file, releases its system resources, and flushes its buffered output to disk if any is still in memory.
  >
  > in Python an object’s memory space is automatically reclaimed as soon as the object is no longer referenced anywhere in the program. When file objects are reclaimed, Python also automatically closes the files if they are still open (this also happens when a program shuts down).

## Files in Action

```
>>> myfile = open('myfile.txt', 'w')			# Open for text output: create/empty
>>> myfile.write('hello text file\n') 			# Write a line of text: string
16
>>> myfile.write('goodbye text file\n') 
18
>>> myfile.close()								# Flush output buffers to disk
>>> myfile = open('myfile.txt')					# Open for text input: 'r' is default
>>> myfile.readline() 							# Read the lines back one at a time
'hello text file\n'
>>> myfile.readline() 
'goodbye text file\n'
>>> myfile.readline() 
''												# Empty string: end-of-file


# reached the end of the file (empty lines in the file come back as strings containing just a newline character, not as empty strings) 

>>> open('myfile.txt').read() 					# Read all at once into string
'hello text file\ngoodbye text file\n'
>>> print(open('myfile.txt').read()) 			# User-friendly display
hello text file 
goodbye text file

>>> for line in open('myfile.txt'): 			# Use file iterators, not reads
...     print(line, end='') 
...
hello text file 
goodbye text file
```

**Windows users:** any of the following forms work for directory paths—raw strings, forward slashes, or doubled-up backslashes:

```
>>> open(r'C:\Python33\Lib\pdb.py').readline() 
'#! /usr/bin/env python3\n'
>>> open('C:/Python33/Lib/pdb.py').readline() 
'#! /usr/bin/env python3\n'
>>> open('C:\\Python33\\Lib\\pdb.py').readline() 
'#! /usr/bin/env python3\n'
```

### Text and Binary Files: The Short Story

In both Python 3.X and 2.X, file type is determined by the second argument to open, the mode string—an included “b” means binary. Python has always supported both text and binary files.

but in Python 3.X there is a sharper distinction between the two:

- Text files represent content as normal str strings, perform Unicode encoding and decoding automatically, and perform end-of-line translation by default.


- Binary files represent content as a special bytes string type and allow programs to access file content unaltered.

Python 2.X text files handle both 8-bit text and binary data, and a special string type and file interface (unicode strings and codecs.open) handles Unicode text.

The differences in Python 3.X stem from the fact that simple and Unicode text have been merged in the normal string type—which makes sense, given that all text is Uni-code, including ASCII and other 8-bit encodings.

All strings are technically Unicode in 3.X

If you need to handle internationalized applications or byte-oriented data, you must use bytes strings for binary files, and normal str strings for text files. Moreover, because text files implement Unicode encodings, you should not open a binary data file in text mode—decoding its content to Unicode text will likely fail.

```
>>> data = open('data.bin', 'rb').read()	# Open binary file: rb=read binary
>>> data b'\x00\x00\x00\x07spam\x00\x08'	# bytes string holds binary data 
>>> data[4:8] 								# Act like strings 
b'spam'
>>> data[4:8][0] 							# But really are small 8-bit integers
115
>>> bin(data[4:8][0]) 						# Python 3.X/2.6+ bin() function
'0b1110011'
```

### Storing Python Objects in Files: Conversions

```
>>> X, Y, Z = 43, 44, 45						# Native Python objects
>>> S = 'Spam'									# Must be strings to store in file
>>> D = {'a': 1, 'b': 2}
>>> L = [1, 2, 3]
>>>
>>> F = open('datafile.txt', 'w')				# Create output text file
>>> F.write(S + '\n')							# Terminate lines with \n
>>> F.write('%s,%s,%s\n' % (X, Y, Z))			# Convert numbers to strings
>>> F.write(str(L) + '$' + str(D) + '\n')		# Convert and separate with $
>>> F.close()

>>> chars = open('datafile.txt').read()			# Raw string display
>>> chars 
"Spam\n43,44,45\n[1, 2, 3]${'a': 1, 'b': 2}\n"
>>> print(chars) 								# User-friendly display
Spam 
43,44,45 
[1, 2, 3]${'a': 1, 'b': 2}

>>> F = open('datafile.txt')					# Open again
>>> line = F.readline()							# Read one line
>>> line 
'Spam\n'
>>> line.rstrip() 								# Remove end-of-line
'Spam'

>>> line = F.readline()							# Next line from file
>>> line 										# It's a string here
'43,44,45\n'
>>> parts = line.split(',')						# Split (parse) on commas
>>> parts 
['43', '44', '45\n']

>>> int(parts[1]) 								# Convert from string to int
44
>>> numbers = [int(P) for P in parts]			# Convert all in list at once
>>> numbers 
[43, 44, 45]

>>> line = F.readline()
>>> line 
"[1, 2, 3]${'a': 1, 'b': 2}\n"
>>> parts = line.split('$')						# Split (parse) on $
>>> parts 
['[1, 2, 3]', "{'a': 1, 'b': 2}\n"]
>>> eval(parts[0]) 								# Convert to any object type
[1, 2, 3]
>>> objects = [eval(P) for P in parts]			# Do same for all in list
>>> objects 
[[1, 2, 3], {'a': 1, 'b': 2}]
```

### Storing Native Python Objects: pickle

The pickle module is a more advanced tool that allows us to store almost any Python object in a file directly, with no to- or from-string conversion requirement on our part. It’s like a super-general data formatting and parsing utility. To store a dictionary in a file, for instance, we pickle it directly:

```
>>> D = {'a': 1, 'b': 2}
>>> F = open('datafile.pkl', 'wb')
>>> import pickle
>>> pickle.dump(D, F)						# Pickle any object to file
>>> F.close()

>>> F = open('datafile.pkl', 'rb')
>>> E = pickle.load(F)						# Load any object from file
>>> E 
{'a': 1, 'b': 2}
```

The pickle module performs what is known as object serialization—convert-ing objects to and from strings of bytes—but requires very little work on our part. pickle internally translates our dictionary to a string form

```
>>> open('datafile.pkl', 'rb').read() 					# Format is prone to change! b'\x80\x03}q\x00(X\x01\x00\x00\x00bq\x01K\x02X\x01\x00\x00\x00aq\x02K\x01u.'
```

### Storing Python Objects in JSON Format

Python’s variables and expressions support richer structuring options (any part of the following can be an arbitrary expression in Python code):

```
>>> name = dict(first='Bob', last='Smith')
>>> rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
>>> rec
{'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}
```

the json module makes the translation official —here translating Python objects to and from a JSON serialized string representation in memory:

```
>>> import json
>>> json.dumps(rec) 
'{"job": ["dev", "mgr"], "name": {"last": "Smith", "first": "Bob"}, "age": 40.5}'

>>> S = json.dumps(rec)
>>> S
'{"job": ["dev", "mgr"], "name": {"last": "Smith", "first": "Bob"}, "age": 40.5}'

>>> O = json.loads(S)
>>> O 
{'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}
>>> O == rec 
True
```

Prior to being stored in a file, your data is simply Python objects; the JSON module recreates them from the JSON textual representation when it loads it from the file:

```
>>> json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
>>> print(open('testjson.txt').read()) 
{ 
	"job": [ 
		"dev", 
		"mgr" 
	], 
	"name": { 
		"last": "Smith", 
		"first": "Bob" 
	}, 
	"age": 40.5
}
>>> P = json.load(open('testjson.txt'))
>>> P 
{'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}
```

- Note that strings are all Unicode in JSON to support text drawn from international character sets, so you’ll see a leading u on strings after translating from JSON data in Python 2.X (but not in 3.X);


- Because Unicode text strings support all the usual string operations, the difference is negligible to your code while text resides in memory; the distinction matters most when transferring text to and from files, and then usually only for non-ASCII types of text where encodings come into play.

There is also support in the Python world for translating objects to and from XML. .For another semirelated tool that deals with formatted data files, see the standard library’s csv module. It parses and creates CSV (comma-sep-arated value) data in files and strings. This doesn’t map as directly to Python objects, but is another common data exchange format:

```
>>> import csv
>>> rdr = csv.reader(open('csvdata.txt'))
>>> for row in rdr: print(row) 
...
['a', 'bbb', 'cc', 'dddd'] 
['11', '22', '33', '44']
```

### Storing Packed Binary Data: struct

the struct module knows how to both compose and parse packed binary data. In a sense, this is another data-conversion tool that interprets strings in files as binary data.

```
>>> F = open('data.bin', 'wb')					# Open binary output file
>>> import struct
>>> data = struct.pack('>i4sh', 7, b'spam', 8)	# Make packed binary data
>>> data 
b'\x00\x00\x00\x07spam\x00\x08'
>>> F.write(data)								# Write byte string
>>> F.close()
```



## File Scanners

1. To **load a file’s contents into a string all at once**, you simply call the file object’s `read` method:

   ```
   file = open('test.txt', 'r') 		# Read contents into a string
   print(file.read())
   ```


2. load a file in smaller pieces, To **read by characters**, either of the following codings will suffice:

   **a while loop with breaks on end-of-file**

   ```
   file = open('test.txt') 
   while True:
   	char = file.read(1) 	# Read by character
   	if not char: break 		# Empty string means end-of-file
   	print(char)
   ```

   **a for loop**

   ```
   file = open('test.txt') 
   for char in open('test.txt').read():
   	print(char)
   ```

   > The `for` loop here also processes each character, but it loads the file into memory all at once (and assumes it fits!).

3. To **read by lines** :

   ```
   file = open('test.txt') 
   while True:
   	line = file.readline() 		# Read line by line
   	if not line: break 
   	print(line.rstrip())		# Line already has a \n
   ```

4. **read binary data in blocks**:

   ```
   file = open('test.txt', 'rb') 
   while True:
   	chunk = file.read(10) 		# Read byte chunks: up to 10 bytes
   	if not chunk: break 
   	print(chunk)
   ```

5. To **read text files line by line**, though, the for loop tends to be easiest to code and the quickest to run:

   ```
   for line in open('test.txt').readlines():
   	print(line.rstrip())

   for line in open('test.txt'):		# Use iterators: best for text input
   	print(line.rstrip())
   ```

   > Both of these versions work in both Python 2.X and 3.X. The first uses the file read lines method to load a file all at once into a line-string list, and the last example here relies on file iterators to automatically read one line on each loop iteration.