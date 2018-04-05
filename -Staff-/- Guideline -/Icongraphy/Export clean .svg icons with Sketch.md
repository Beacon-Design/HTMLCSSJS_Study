# Export clean .svg icons with Sketch



## 1. Create an artboard for each icon.

Rule 1 :  Make the artboard of the same size of the icon/illustration you want to export.

Rule 2 :  Make sure each artboard’s position has no half-pixels and is an even number.



## 2. Create your icon.

Rule 1 : Try to make shapes with fills. Fills are easily exported to vector drawables.

Rule 2 : If your shape has a border, use an centre border. SVGs exported with inner or outer borders don’t 		convert to vector drawables.

Rule 3 : Don’t use any masks. Masked layers are not identified in vector drawables.

Rule 4 : No groups. Creates a lot of unwanted code which creates a mess while converting to vector 		drawables.

Rule 5 : No rotation. No flip. No transformation.（Remove all）

Rule 6 :  Remove any bounding boxes so Sketch doesn’t export unneeded code. 



## 3. Install “SVGO Compressor.sketchplugin”

https://github.com/BohemianCoding/svgo-compressor



## 4. Edit SVGO Settings

Plugin > SVGO Compressor ( Edit svgo.json ) 



### delete fill-rule

```
{
"name": "sortAttrs"
},


{
"name": "removeAttrs",
"params": {
"attrs": "fill-rule"
}
```



### set removeTitle off

change

```
{
"name": "removeTitle"
},
```

to

```
{
"removeTitle": false
},
```

> #### removeTitle
>
> Removes `<title>`.
>
> On by default in SVGO Compressor





## 5. Export icon artcoard





## SVGO Parameters

https://github.com/svg/svgo



## Reference : Preparing and Exporting SVG Icons in Sketch

https://medium.com/sketch-app-sources/preparing-and-exporting-svg-icons-in-sketch-1a3d65b239bb





------





## 生成 16x16 适用前端 “symbol 引用” 方式的 svg 文件

1. 将图标上传至 https://icomoon.io/app/#/select


2. 导出的 svg 的 Preferences 设置, 将 Class Prefix 设置成 aui-icon-；取消所有其它选项.

3. 导出的 svg 文件夹中 symbol-defs.svg 文件交付前端使用

4. 打开 symbol-defs.svg 文件，示例代码如下：

   ```
   <svg aria-hidden="true" style="position: absolute; width: 0; height: 0; overflow: hidden;" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
   	<defs>
   		<symbol id="aui-icon-minus" viewBox="0 0 16 16">
   			<title>minus</title>
   			<path d="M14.125 7h-12.25c-0.525 0-0.875 0.35-0.875 0.875s0.35 0.875 0.875 0.875h12.25c0.525 0 0.875-0.35 0.875-0.875s-0.35-0.875-0.875-0.875z"></path>
   		</symbol>
   		<symbol id="aui-icon-plus" viewBox="0 0 16 16">
   			<title>plus</title>
   			<path d="M14.125 7.125h-5.25v-5.25c0-0.525-0.35-0.875-0.875-0.875s-0.875 0.35-0.875 0.875v5.25h-5.25c-0.525 0-0.875 0.35-0.875 0.875s0.35 0.875 0.875 0.875h5.25v5.25c0 0.525 0.35 0.875 0.875 0.875s0.875-0.35 0.875-0.875v-5.25h5.25c0.525 0 0.875-0.35 0.875-0.875s-0.35-0.875-0.875-0.875z"></path>
   		</symbol>
   	</defs>
   </svg>
   ```

5. ```
   <symbol></symbol> 标签内代码为实际使用图标。
   ```

   ​

