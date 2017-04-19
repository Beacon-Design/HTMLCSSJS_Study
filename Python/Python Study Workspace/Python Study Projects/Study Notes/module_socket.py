# encoding=utf-8
print(u'''

http://python.org/doc/lib/module-socket.html
http://docs.python.org/dev/howto/sockets.html

http://blog.sina.com.cn/s/blog_523491650100hikg.html
http://www.cnblogs.com/vamei/archive/2012/10/30/2744955.html



套接字是为特定网络协议（例如TCP/IP，ICMP/IP，UDP/IP等）套件对上的网络应用程序提供者提供当前可移植标准的对象。
它们允许程序接受并进行连接，如发送和接受数据。为了建立通信通道，网络通信的每个端点拥有一个套接字对象极为重要。
套接字为BSD UNIX系统核心的一部分，而且他们也被许多其他类似UNIX的操作系统包括Linux所采纳。
许多非BSD UNIX系统（如ms-dos，windows，os/2，mac os及大部分主机环境）都以库形式提供对套接字的支持。


三种最流行的套接字类型是:stream,datagram和raw。stream和datagram套接字可以直接与TCP协议进行接口，
而raw套接字则接口到IP协议。但套接字并不限于TCP/IP。


### 建立服务器连接需要六个步骤: ###
第1步是创建socket对象。调用socket构造函数。

socket=socket.socket(familly,type)

family的值可以是AF_UNIX(Unix域，用于同一台机器上的进程间通讯)，也可以是AF_INET（对于IPV4协议的TCP和 UDP），
至于type参数，SOCK_STREAM（流套接字）或者 SOCK_DGRAM（数据报文套接字）,SOCK_RAW（raw套接字）。

第2步则是将socket绑定（指派）到指定地址上，socket.bind(address)

address必须是一个双元素元组,((host,port)),主机名或者ip地址+端口号。如果端口号正在被使用或者保留，
或者主机名或ip地址错误，则引发socke.error异常。

第3步，绑定后，必须准备好套接字，以便接受连接请求。

socket.listen(backlog)

backlog指定了最多连接数，至少为1，接到连接请求后，这些请求必须排队，如果队列已满，则拒绝请求。

第4步，服务器套接字通过socket的accept方法等待客户请求一个连接：

connection,address=socket.accept()

调用accept方法时，socket会进入'waiting'（或阻塞）状态。客户请求连接时，方法建立连接并返回服务器。
accept方法返回一个含有俩个元素的元组，形如(connection,address)。
第一个元素（connection）是新的socket对象，服务器通过它与客户通信；第二个元素（address）是客户的internet地址。

第5步是处理阶段，服务器和客户通过send和recv方法通信（传输数据）。服务器调用send，并采用字符串形式向客户发送信息。
send方法返回已发送的字符个数。服务器使用recv方法从客户接受信息。调用recv时，必须指定一个整数来控制本次调用所接受的最大数据量。
recv方法在接受数据时会进入'blocket'状态，最后返回一个字符串，用它来表示收到的数据。如果发送的量超过recv所允许，数据会被截断。
多余的数据将缓冲于接受端。以后调用recv时，多余的数据会从缓冲区删除。

第6步，传输结束，服务器调用socket的close方法以关闭连接。

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

### 编写server的步骤： ###

第一步是创建socket对象。调用socket构造函数。如：

socket = socket.socket( family, type )

family参数代表地址家族，可为AF_INET或AF_UNIX。AF_INET家族包括Internet地址，AF_UNIX家族用于同一台机器上的进程间通信。
type参数代表套接字类型，可为SOCK_STREAM(流套接字)和SOCK_DGRAM(数据报套接字)。

第二步是将socket绑定到指定地址。这是通过socket对象的bind方法来实现的：

socket.bind( address )

由AF_INET所创建的套接字，address地址必须是一个双元素元组，格式是(host,port)。host代表主机，port代表端口号。
如果端口号正在使用、主机名不正确或端口已被保留，bind方法将引发socket.error异常。

第三步是使用socket套接字的listen方法接收连接请求。

socket.listen( backlog )

backlog指定最多允许多少个客户连接到服务器。它的值至少为1。收到连接请求后，这些请求需要排队，如果队列满，就拒绝请求。

第四步是服务器套接字通过socket的accept方法等待客户请求一个连接。

connection, address = socket.accept()

调用accept方法时，socket会时入“waiting”状态。客户请求连接时，方法建立连接并返回服务器。
accept方法返回一个含有两个元素的元组(connection,address)。第一个元素connection是新的socket对象，
服务器必须通过它与客户通信；第二个元素 address是客户的Internet地址。

第五步是处理阶段，服务器和客户端通过send和recv方法通信(传输数据)。服务器调用send，并采用字符串形式向客户发送信息。
send方法返回已发送的字符个数。服务器使用recv方法从客户接收信息。调用recv 时，服务器必须指定一个整数，
它对应于可通过本次方法调用来接收的最大数据量。recv方法在接收数据时会进入“blocked”状态，最后返回一个字符串，用它表示收到的数据。
如果发送的数据量超过了recv所允许的，数据会被截短。多余的数据将缓冲于接收端。以后调用recv时，
多余的数据会从缓冲区删除(以及自上次调用recv以来，客户可能发送的其它任何数据)。
传输结束，服务器调用socket的close方法关闭连接。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### 编写client的步骤： ###
创建一个socket以连接服务器：socket = socket.socket( family, type )

使用socket的connect方法连接服务器。对于AF_INET家族,连接格式如下：

socket.connect( (host,port) )

host代表服务器主机名或IP，port代表服务器进程所绑定的端口号。如连接成功，客户就可通过套接字与服务器通信，
如果连接失败，会引发socket.error异常。
处理阶段，客户和服务器将通过send方法和recv方法通信。
传输结束，客户通过调用socket的close方法关闭连接。


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
通信类型和协议家族：
通信类型指明用什么协议来传输数据，协议的例子：
IPv4,IPv6,IPX/SPX(NetWare),AFP(Apple共享文件),(AF_INET表示IPv4)

协议家族：
SOCK_STREAM表示TCP通信，SOCK_DGRAM表示UDP通信

一个socket包含四个地址信息: 两台计算机的IP地址和两个进程所使用的端口(port)。IP地址用于定位计算机，
而port用于定位进程 (一台计算机上可以有多个进程分别使用不同的端口)。


''')



