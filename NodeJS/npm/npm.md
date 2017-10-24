# NPM

## NPM 常用命令

[npm docs](https://docs.npmjs.com)

```
$ sudo npm install npm@latest -g
//To upgrade the latest version.

$ npm -v
2.3.0
//查看版本信息

$ sudo npm install npm -g
//npm 全局安装

$ npm ls -g
//查看所有全局安装的模块

$ npm help
//可查看所有命令

$ npm help <command>
//可查看某条命令的详细帮助，例如npm help install

$ npm update <package>
//可以把当前目录下node_modules子目录里边的对应模块更新至最新版本。
$ npm update <package> -g
//可以把全局安装的对应命令行程序更新至最新版

$ npm cache clear
//可以清空NPM本地缓存，用于对付使用相同版本号发布新版本代码的人

$ npm unpublish <package>@<version>
//可以撤销发布自己发布过的某个版本代码

//在package.json所在目录下使用npm install . -g可先在本地安装当前命令行程序，可用于发布前的本地测试。
```

## 使用 npm 命令安装模块

```
//npm 安装 Node.js 模块语法格式
$ npm install <Module Name>
```

```
//使用 npm 命令安装常用的 Node.js web框架模块 express
$ npm install express

//安装好之后，express 包就放在工程目录下的 node_modules 目录中.代码中只需要通过 require('express') 的方式就好，无需指定第三方包路径。
```



## 全局安装与本地安装

```
npm install express -g   
//全局安装

npm install express          
//本地安装
```

> ### 全局安装
>
> 1. 将安装包放在 /usr/local 下或者你 node 的安装目录。
> 2. 可以直接在命令行里使用。

> ### 本地安装
>
> 1. 将安装包放在 ./node_modules 下（运行 npm 命令时所在的目录），如果没有 node_modules 目录，会在当前执行 npm 命令的目录下生成 node_modules 目录。
>
>
> 2. 可以通过 require() 来引入本地安装的包。



如果出现以下错误

```
npm err! Error: connect ECONNREFUSED 127.0.0.1:8087 
```

解决办法为

```
$ npm config set proxy null
```



## 使用 package.json

package.json 位于模块的目录下，用于定义包的属性

>**Package.json 属性说明**
>
>- **name** - 包名。
>- **version** - 包的版本号。
>- **description** - 包的描述。
>- **homepage** - 包的官网 url 。
>- **author** - 包的作者姓名。
>- **contributors** - 包的其他贡献者姓名。
>- **dependencies** - 依赖包列表。如果依赖包没有安装，npm 会自动将依赖包安装在 node_module 目录下。
>- **repository** - 包代码存放的地方的类型，可以是 git 或 svn，git 可在 Github 上。
>- **main** - main 字段是一个模块ID，它是一个指向你程序的主要项目。就是说，如果你包的名字叫 express，然后用户安装它，然后require("express")。
>- **keywords** - 关键字



## 卸载, 更新, 搜索模块

```
$ npm uninstall express

$ npm ls
//卸载后，可以到 /node_modules/ 目录下查看包是否还存在，或者使用命令查看

$ npm update express
//更新模块

$ npm search express
//搜索模块
```



## 版本号

使用NPM下载和发布代码时都会接触到版本号。NPM使用语义版本号来管理代码，这里简单介绍一下。

语义版本号分为X.Y.Z三位，分别代表主版本号、次版本号和补丁版本号。当代码变更时，版本号按以下原则更新。

- 如果只是修复bug，需要更新Z位。
- 如果是新增了功能，但是向下兼容，需要更新Y位。
- 如果有大变动，向下不兼容，需要更新X位。

版本号有了这个保证后，在申明第三方包依赖时，除了可依赖于一个固定版本号外，还可依赖于某个范围的版本号。例如"argv": "0.0.x"表示依赖于0.0.x系列的最新版argv。

NPM支持的所有版本号范围指定方式可以查看[官方文档](https://npmjs.org/doc/files/package.json.html#dependencies)。



## 使用淘宝 NPM 镜像

大家都知道国内直接使用 npm 的官方镜像是非常慢的，这里推荐使用淘宝 NPM 镜像。

淘宝 NPM 镜像是一个完整 npmjs.org 镜像，你可以用此代替官方版本(只读)，同步频率目前为 10分钟 一次以保证尽量与官方服务同步。

你可以使用淘宝定制的 cnpm (gzip 压缩支持) 命令行工具代替默认的 npm:

```
$ npm install -g cnpm --registry=https://registry.npm.taobao.org
```

这样就可以使用 cnpm 命令来安装模块了：

```
$ cnpm install [name]
```

更多信息可以查阅：[http://npm.taobao.org/](http://npm.taobao.org/)。