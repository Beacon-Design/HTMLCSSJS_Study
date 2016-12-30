# Easing 

### Adobe After effects

##### 1. Graphic Editor

> Graphic Editor
>
> AE 内置图形编辑器，通过手动调节图形曲线来调整动画速率及缓动。
>
> 不可通过数值调整。仅软件内使用。不能直接输出对应数值应用到 CSS3 Animation 或其他前端编程动画中。
>
> Free

##### 2. Keyframe Velocity

> Keyframe Velocity
>
> AE 内置关键帧设置选项，可通过数值（需逐一输入数值）调整关键帧缓动效果。
>
> 仅软件内使用。不能直接输出对应数值应用到 CSS3 Animation 或其他前端编程动画中。数值需转换（对应关系待研究）
>
> Free

##### 2. Motion 2

> Motion v2 
>
> AE plugin, 可通过直观的界面数值输入调整 keyframe velocity(关键帧速率)设置缓动效果，并可直观的同时编辑多个帧。
>
> 不能直接输出对应数值应用到 CSS3 Animation 或其他前端编程动画中。数值需转换（对应关系待研究）
>
> $35
>
> 网址：http://www.mtmograph.com/motion/

##### 3. Easy

> aesweets Easy v1.0
>
> AE plugin, 通过图形界面的缓动预设，设置关键帧缓动。预设丰富，不可自定义。
>
> 不能输出数值应用到 CSS3 Animation 或其他前端编程动画中。
>
> $29.99
>
> 网址：http://aesweets.com/easy/

##### 4. After Ease

> After Ease v1.1.2
>
> AE plugin, 内置 Bounce, Elastic 表达式并可设置相应部分参数，并可通过Expression; Bake 方式应用到已制作的动画帧上, 或 animating mask and shape paths.
>
> 不能直接输出对应数值应用到 CSS3 Animation 或其他前端编程动画中。
>
> $25
>
> 网址：http://aescripts.com/after-ease/

##### 5. Flow

> Flow v1.1.2
>
> AE plugin, 可通过界面的图形编辑或数值输入设置关键帧缓动效果。可自定义缓动预设(自定义设置Bezier point数值)，并将Bezier Values, Apply to keys or Apply to expression。可保存预设，同时可导入他人预设。可直接输出对应数值到 CSS3 Animation 或其他前端编程动画中。
>
> $30
>
> 网址：http://aescripts.com/flow/
>
> ```javascript
> //	Apply to Expression 
>
> n = 0;
> if (numKeys > 0) {
>     n = nearestKey(time).index;
>     if (key(n).time > time) n--;
>     if (n == 0 || n == numKeys) value;
>     else customBezier(time, key(n).time, key(n + 1).time, key(n).value, key(n + 1).value, [0.11, 0, 0.58, 1]);
> } else {
>     value;
> }
>
>
> //--------- Flow Expression Code ---------//
> function customBezier(t, tMin, tMax, value1, value2, bezierPoints) {
>     z = arguments;
>     if (z.length !== 6) return value;
>     a = z[4] - z[3];
>     b = z[2] - z[1];
>     c = clamp((z[0] - z[1]) / b, 0, 1);
>     if (!(z[5] instanceof Array) || z[5].length !== 4) z[5] = [0.11, 0, 0.58, 1];
>     return a * h(c, z[5]) + z[3];
>
>     function h(f, g) {
>         y = arguments;
>         h = 3 * y[1][0];
>         j = 3 * (y[1][2] - y[1][0]) - h;
>         k = 1 - h - j;
>         l = 3 * y[1][1];
>         m = 3 * (y[1][3] - y[1][1]) - l;
>         n = 1 - l - m;
>         d = y[0];
>         for (var i = 0; i < 5; i++) {
>             var z = d * (h + d * (j + d * k)) - y[0];
>             if (Math.abs(z) < 1e-3) break;
>             d -= z / (h + d * (2 * j + 3 * k * d));
>         }
>         return d * (l + d * (m + d * n));
>     }
> }
> //--------- Flow Expression Code ---------//
>
> ```



### Easing Reference

[easing.net](http://easings.net/)

[cubic-bezier.com](http://cubic-bezier.com/#0,.5,1,.5)

[Ceaser css easing animation tool](https://matthewlein.com/ceaser/)