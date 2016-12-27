# Mac Terminal


## mac:在当前文件夹打开terminal终端

Version A  
1. System Preferences -> Keyboard -> Shortcuts -> Services -> New Terminal at Folders/New Terminal Tab at Folder 这二项都勾上
2. 然后在Finder中,在任何目录上右击->service就能看到进入terminal的选项

Version B  
* cd + 空格 + 拖曳要进入的文件夹




## 文件目录

首先要清楚几个文件目录：

" / "  ：根目录

" ~ " ：用户主目录的缩写。例如当前用户为hello，那么" ~ "展开来就是：/Users/hello

" . "  ：当前目录

".."   ：父目录



## 命令

###1. cd 跳转到某个目录

例如：

$ cd /Users/apple/Desktop/
在这里有个小技巧，就是在输入目录如Desktop时，只要输入Des并按tab键，该目录名便自动补全了。

$ cd / 
前往根目录（Macintosh HD） 
$ cd ~ 
前往用户主目录 
$ cd .. 
前往当前所在目录的上一级



###2. ls 列出当前目录下的子目录和文件
###3. pwd 显示当前目录的路径
###4. clear / cmd+k 清空当前输入
如果Terminal窗口中的内容太多了，可以用clear命令将其清空。
###5. history 查看输入历史记录
在Terminal输入命令时，可以使用上下方向键查看之前输入的命令（和windows的cmd相同）,可以用history查看输入的完整历史
###6. mkdir 创建目录 / rmdir 删除目录
$ mkdir name 
在当前目录下创建名为name的子目录 
$ rmdir name 
在当前目录下删除名为name的子目录(子目录为空则可删除，不会出现在垃圾桶中，不为空则不可删除) 
$ rm -r name
在当前目录下删除名为name的子目录（不会出现在垃圾桶中）  
###7. rm 删除（remove）

rm 的意义是 remove ，也就是用来杀掉一个档案的指令。在 UNIX 中一个被杀掉的档案除非是系统恰好有做备份，否则是无法像 DOS 里面一样还能够救回来的。所以在做 rm 动作的时候使用者应该要特别小心。

rm 的格式如下:

$ rm name
删除名为name的空目录（rm只能删 除文件或者空的文件夹）  

rm 的参数

-f : 将会使得系统在删除时，不提出任何警告讯息。 
-i : 在除去档案之前均会询问是否真要除去。 
-r : 递回式的删除。（删除文件夹内的子文件夹及内容）  


$ touch index.html 
创建index.html空文件 
$ open index.html 
打开index.html文件 
$ open index.html -a "Sublime Text" 
用Sublime Text打开index.html文件 
$ open . 
在finder中打开当前目录  

### mv
mv 的意义为 move , 主要是将一档案改名或换至另一个目录。如同 cp ，它也有三种格式:

mv f1 f2 : 将档名为 f1 的档案变更成档名为 f2 的档案。 
mv dir1 dir2 : 将档名为 dir1 的目录变更成档名为 dir2 的目录。 
mv f1 f2 f3 ... dir : 将档案 f1 f2 f3 ... 都移至目录 dir 里面。  

mv 的参数有两个，-f 和 -i , 其中 -i 的意义与 cp 中的相同，均是 interactive询问之意。而 -f 为强迫( force ) , 就是不管有没有同名的档案，反正我就是要搬过去，所有其他的参数遇到 -f 均会失效。

