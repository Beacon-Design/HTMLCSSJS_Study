# Web Server

## Version 1.
### python -m SimpleHTTPServer
(python version 2.7.1;)

1.mac(要建立服务器设备的机器)上，创建需要共享的文件夹
2.mac 打开 Terminal
3.输入：文件夹路径（或cd到文件夹路径位置）
4.输入：python -m SimpleHTTPServer 8080（如果不填写端口号，默认为8000）
5.查看 mac 的 ip 地址（如：192.168.1.1）
6.在其他设备上的浏览器中输入 http://192.168.1.1:8000 （ip地址：端口号）
（其他设备应与mac在同一网络中）

关闭该Terminal窗口，则端口关闭。
如果你的目录下有一个叫 index.html 的文件名的文件，那么这个文件就会成为一个默认页，如果没有这个文件，那么，目录列表就会显示出来。

python -m SimpleHTTPServer 8000 &
在上述命令的最后加一个 & ，则该命令产生的进程在后台运行，不会影响当前终端的使用（我们在只有一个bash的环境下）。
生成的新的进程为当前bash的子进程，所以，当我们关闭当前bash时，相应的子进程也会被kill掉，这也不是我们想要的结果。

nohup python -m SimpleHTTPServer 8000 &
在命令的开头加一个nohup，忽略所有的挂断信号，如果当前bash关闭，则当前进程会挂载到init进程下，成为其子进程，这样即使退出当前用户，其8000端口也可以使用。


## Version 2.
### live-server

1.安装
npm install -g live-server
(sudo npm install -g live-server)
2.在文件夹name中创建index.html
3.在name文件夹上右键> Services> New Terminal at Folder
(Terminal 中 cd 到name文件夹位置)
4.Terminal 中输入 live-server
5.mac默认浏览器自动打开index.html
(保存对index.html的修改，所有连接服务器的设备中浏览器会自动刷新)
6.查看 mac 的 ip 地址（如：192.168.1.1）
7.在其他设备上的浏览器中输入 http://192.168.1.1:8000 （ip地址：端口号）
（其他设备应与mac在同一网络中）


## Version 3.
### Apache Web Server

1.打开终端，输入 httpd -v 可以查看 Apache 版本信息。
2.启动 Apache
在终端输入 sudo apachectl start 即可启动 Apache。
启动后，在浏览器中输入 http://127.0.0.1 或 http://localhost 如果看到 It Works! 页面：
那么 Apache 就启动成功了，站点的根目录为系统级根目录 /Library/WebServer/Documents。
(在终端输入ps aux | grep httpd可查看打开是否成功)
启动后，你可以通过编辑 /etc/apache2/httpd.conf 文件来修改 Apache 配置。



**web资源位置**
apache下部署web资源位置Macintosh HD/Library/WebServer/Documents

**修改资源位置**
3.在终端输入 open /etc 命令即可打开mac os 系统存放系统配置信息(apache安装目录)
(Finder> Go to Folder> /etc)
资源位置在etc> apache2文件夹下 httpd.conf文件可配置
DocumentRoot "/Library/WebServer/Documents"

找到：
/Library/WebServer/Documents
替换成
/Users/{username}/Sites
其中{username}是你登陆用户名,如:
/Users/rk/Sites

运行“sudo apachectl restart”
重启成功后，无需再加上用户名，便可以使用http://localhost/直接访问自己Sites目录下的内容。




### Apache

1.打开终端，输入 httpd -v 可以查看 Apache 版本信息。
2.启动 Apache
在终端输入 sudo apachectl start 即可启动 Apache。
启动后，在浏览器中输入 http://127.0.0.1 或 http://localhost 如果看到 It Works! 页面：
那么 Apache 就启动成功了，站点的根目录为系统级根目录 /Library/WebServer/Documents。
启动后，你可以通过编辑 /etc/apache2/httpd.conf 文件来修改 Apache 配置。
(在终端输入ps aux | grep httpd可查看打开是否成功)

3.停止 Apache：sudo apachectl stop

4.重启 Apache：sudo apachectl restart

check config syntax
在终端输入 apachectl configtest
configtest执行一次配置文件语法检查。它解析配置文件，并报告 Syntax Ok 或者是特定的语法错误详细信息。它等价于 apachectl -t 

apachectl test
打开help文档

**修改Apache的默认端口号**
httpd.conf
Listen 80

1.Listen 80”字符串中（仅此一处），将80改为8000或8080,或任意数字（端口号知识待补充）
在“Listen 80”的上方还有“#Listen 12.34.56.78:80”这样一串字符，这儿的80不是一定要随“Listen 80”中的80而变化，可改可不改，这只是一个样例。
2.完成端口号的修改后，要停止（STOP）一次Apache服务然后再启动（START），使修改生效。
3.打开位于Apache服务器上的网页，必须在地址后面加上冒号+端口号，如http://localhost:8080或者是http://127.0.0.1:8080

