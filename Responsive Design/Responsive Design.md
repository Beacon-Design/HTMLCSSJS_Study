# Responsive Design

## CSS

### Viewport 

viewport meta

```css
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

- width：控制 viewport 的大小，可以指定的一个值，如果 600，或者特殊的值，如 device-width 为设备的宽度（单位为缩放为 100% 时的 CSS 的像素）。
- height：和 width 相对应，指定高度。
- initial-scale：初始缩放比例，也即是当页面第一次 load 的时候缩放比例。
- maximum-scale：允许用户缩放到的最大比例。
- minimum-scale：允许用户缩放到的最小比例。
- user-scalable：用户是否可以手动缩放。

### 网格视图

响应式网格视图通常是 12 列，宽度为100%，在浏览器窗口大小调整时会自动伸缩。

#### 创建响应式网格视图

首先确保所有的 HTML 元素都有 **box-sizing** 属性且设置为 **border-box**。[CSS3 Box-sizing](http://www.runoob.com/cssref/css3-pr-box-sizing.html)

确保边距和边框包含在元素的宽度和高度间。

```css
* {
    box-sizing: border-box;
}
```

12 列的网格系统可以更好的控制响应式网页。

首先我们可以计算每列的百分比: 100% / 12 列 = 8.33%。

在每列中指定 class， **class="col-"** 用于定义每列有几个 span 

```css
.col-1 {width: 8.33%;}
.col-2 {width: 16.66%;}
.col-3 {width: 25%;}
.col-4 {width: 33.33%;}
.col-5 {width: 41.66%;}
.col-6 {width: 50%;}
.col-7 {width: 58.33%;}
.col-8 {width: 66.66%;}
.col-9 {width: 75%;}
.col-10 {width: 83.33%;}
.col-11 {width: 91.66%;}
.col-12 {width: 100%;}
```

