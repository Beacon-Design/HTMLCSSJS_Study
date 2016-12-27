var http = require("http");
//使用require载入http模块


//使用 http.createServer() 方法创建服务器，并使用 listen 方法绑定 8888 端口。 函数通过 request, response 参数来接收和响应数据
http.createServer(function (request, response) {
    
    // 发送 HTTP 头部 
	// HTTP 状态值: 200 : OK
	// 内容类型: text/plain
    response.writeHead(200, {
        "Content-Type": "text/plain"
    });
    
    // 发送响应数据 "Hello World"
    response.end("Hallo world\n");
}).listen(8888);

// 终端打印如下信息
console.log("Server running at http://127.0.0.1:8888/");


/*
使用 node 命令执行以代码:
node server.js

打开浏览器访问 http://127.0.0.1:8888/，你会看到一个写着 "Hello World"的网页。
*/