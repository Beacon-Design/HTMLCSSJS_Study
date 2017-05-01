

# File

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

