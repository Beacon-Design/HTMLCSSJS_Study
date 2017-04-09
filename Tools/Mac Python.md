# Mac下配置Python开发环境



## VSCode配置Python开发环境

### 配置环境

1. command + shift + p

2. ```
   >Tasks:Configure Task Runner
   ```

3. tasks.json文件

   ```
   {
       // See https://go.microsoft.com/fwlink/?LinkId=733558
       // for the documentation about the tasks.json format
       "version": "0.1.0",
       "command": "python",
       "isShellCommand": true,
       "args": ["${file}"],
       "showOutput": "always"
   }
   ```

### 运行文件

1. 创建测试文件test.py

2. 打开文件后输入

   ```
   print("go")
   ```

3. 保存文件

4. Cmd + Shift + B





## Atom配置python

1. install atom-runner
2. run a python file Ctrol + R





## Sublime Text 运行 python file

run a python file

Cmd + B (Tools > Build) 



## Brackets 运行python file

1. install plugin "Brackets Builder Extended"(Hornets / Kmashint)
2. run a python file: Cmd + Alt + B




------





# Python Terminal



## Terminal 退出 python

> Ctrl + D 

或

```python
exit()
```



## Terminal切换不同版本python

> python2
>
> ```python
> python 
> ```

> python3
>
> ```python
> python3
> ```