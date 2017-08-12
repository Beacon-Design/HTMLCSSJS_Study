# Transition

## Properties

> [transition](https://developer.mozilla.org/en-US/docs/Web/CSS/transition)
>
> [transition-delay](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-delay)
>
> [transition-duration](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-duration)
>
> [transition-property](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property)
>
> [transition-timing-function](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function)

## CSS animated properties

[*Examples of Each Property Animated*](http://leaverou.github.io/animatable/)	

[CSS Animated Properties Reference Page](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animated_properties)

> Some Basic List of Animatable Properties:
>
> 











## transition

> **Initial value**
>
> [transition-delay](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-delay): 0s
>
> [transition-duration](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-duration): 0s
>
> [transition-property](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property): all
>
> [transition-timing-function](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function): ease



#### Syntax

[reference page](https://developer.mozilla.org/en-US/docs/Web/CSS/transition)

```css
/* Apply to 1 property */
/* property name | duration */
transition: margin-left 4s;

/* property name | duration | delay */
transition: margin-left 4s 1s;

/* property name | duration | timing function | delay */
transition: margin-left 4s ease-in-out 1s;

/* Apply to 2 properties */
transition: margin-left 4s, color 1s;

/* Apply to all changed properties */
transition: all 0.5s ease-out;

/* Global values */
transition: inherit;
transition: initial;
transition: unset;
```

------



#### Property value lists are of different lengths

> If any property's list of values is shorter than the others, its values are repeated to make them match. For example:
>
> ```css
> div {
>   transition-property: opacity, left, top, height;
>   transition-duration: 3s, 5s;
> }
> ```
>
> This is treated as if it were:
>
> ```css
> div {
>   transition-property: opacity, left, top, height;
>   transition-duration: 3s, 5s, 3s, 5s;
> }
> ```

> if any property's value list is longer than that for [transition-property](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property) , it's truncated, so if you have the following CSS:
>
> ```css
> div {
>   transition-property: opacity, left;
>   transition-duration: 3s, 5s, 2s, 1s;
> }
> ```
>
> This gets interpreted as:
>
> ```css
> div {
>   transition-property: opacity, left;
>   transition-duration: 3s, 5s;
> }
> ```



#### A simple example

> This example performs a four-second font size transition with a two-second delay between the time the user mouses over the element and the beginning of the animation effect:
>
> ```css
> #delay1 {
>   position: relative;
>   transition-property: font-size;
>   transition-duration: 4s;
>   transition-delay: 2s;
>   font-size: 14px;
> }
>
> #delay1:hover {
>   transition-property: font-size;
>   transition-duration: 4s;
>   transition-delay: 2s;
>   font-size: 36px;
> }
> ```



#### Using transitions when highlighting menus

> First we set up the menu using HTML:
>
> ```css
> <div class="sidebar">
>   <p><a class="menuButton" href="home">Home</a></p>
>   <p><a class="menuButton" href="about">About</a></p>
>   <p><a class="menuButton" href="contact">Contact Us</a></p>
>   <p><a class="menuButton" href="links">Links</a></p>
> </div>
> ```
>
> Then we build the CSS to implement the look and feel of our menu. The relevant portions are shown here:
>
> ```css
> .menuButton {
>   position: relative;
>   transition-property: background-color, color;
>   transition-duration: 1s;
>   transition-timing-function: ease-out;
>   text-align: left;
>   background-color: grey;
>   left: 5px;
>   top: 5px;
>   height: 26px;
>   color: white;
>   border-color: black;
>   font-family: sans-serif;
>   font-size: 20px;
>   text-decoration: none;
>   box-shadow: 2px 2px 1px black;
>   padding: 2px 4px;
>   border: solid 1px black;
> }
>
> .menuButton:hover {
>   position: relative;
>   transition-property: background-color, color;
>   transition-duration: 1s;
>   transition-timing-function: ease-out;
>   background-color:white;
>   color:black;
>   box-shadow: 2px 2px 1px black;
> }
> ```
>
> This CSS establishes the look of the menu, with the background and text colors both changing when the element is in its [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/:hover) state.



#### Using transitions to make JavaScript functionality smooth

> Transitions are a great tool to make things look much smoother without having to do anything to your JavaScript functionality. Take the following example.
>
> ```css
> <p>Click anywhere to move the ball</p>
> <div id="foo"></div>
> ```
>
> Using JavaScript you can make the effect of moving the ball to a certain position happen:
>
> ```css
> var f = document.getElementById('foo');
> document.addEventListener('click', function(ev){
>     f.style.transform = 'translateY('+(ev.clientY-25)+'px)';
>     f.style.transform += 'translateX('+(ev.clientX-25)+'px)';
> },false);
> ```
>
> With CSS you can make it smooth without any extra effort. Simply add a transition to the element and any change will happen smoothly:
>
> ```css
> p {
>   padding-left: 60px;
> }
>
> #foo {
>   border-radius: 50px;
>   width: 50px;
>   height: 50px;
>   background: #c00;
>   position: absolute;
>   top: 0;
>   left: 0;
>   transition: transform 1s;
> }
> ```
>
> You can play with this here: [http://jsfiddle.net/9h261pzo/291/](http://jsfiddle.net/9h261pzo/291/)



## transition-delay

The **transition-delay** CSS property specifies the amount of time to wait between a change being requested to a property that is to be transitioned and the start of the [transition effect](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions).

A value of `0s`, or `0ms`, indicates that the property will begin to animate its transition immediately when the value changes; positive values will delay the start of the transition effect for the corresponding number of seconds. Negative values cause the transition to begin immediately, but to cause the transition to seem to begin partway through the animation effect.

You may specify multiple delays; each delay will be applied to the corresponding property as specified by the [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property) property, which acts as a master list. If there are fewer delays specified than in the master list, missing values are set to the initial value (0s). If there are more delays, the list is simply truncated to the right size. In both case the CSS declaration stays valid.

**Syntax**	[reference page](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-delay)

```css
/* <time> values */
transition-delay: 3s;
transition-delay: 2s, 4ms;

/* Global values */
transition-delay: inherit;
transition-delay: initial;
transition-delay: unset;
```

Is a [`time`](https://developer.mozilla.org/en-US/docs/Web/CSS/time) denoting the amount of time to wait between a property's value changing and the start of the animation effect.



## transition-duration

The **transition-duration** [CSS](https://developer.mozilla.org/en/CSS) property specifies the number of seconds or milliseconds a transition animation should take to complete. By default, the value is `0s`, meaning that no animation will occur.

You may specify multiple durations; each duration will be applied to the corresponding property as specified by the [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property) property, which acts as a master list. If there are fewer durations specified than in the master list, the user agent repeat the list of durations. If there are more durations, the list is simply truncated to the right size. In both case the CSS declaration stays valid.

**Syntax**	[reference page](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-duration)

```css
/* <time> values */
transition-duration: 6s;
transition-duration: 120ms;
transition-duration: 1s, 15s;
transition-duration: 10s, 30s, 230ms;

/* Global values */
transition-duration: inherit;
transition-duration: initial;
transition-duration: unset;
```

Is a [`time`](https://developer.mozilla.org/en-US/docs/Web/CSS/time) denoting the amount of time the transition from the old value of a property to the new value should take. A time of `0s` indicates that no transition will happen, that is the switch between the two states will be instantaneous. A negative value for the time renders the declaration invalid.



## transition-property

If you specify a shorthand property (for example, [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/background)) all of its longhand sub-properties that can be animated will be.

**Syntax**	[reference page](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property)

```css
/* Keyword values */
transition-property: none;
transition-property: all;
transition-property: test_05;
transition-property: -specific;
transition-property: sliding-vertically;

transition-property: test1;
transition-property: test1, animation4;
transition-property: all, height, all;
transition-property: all, -moz-specific, sliding;

/* Global values */
transition-property: inherit;
transition-property: initial;
transition-property: unset;
```

**none**

No properties will transition.

**all**

All properties that can have an animated transition will do so.

**IDENT**

A string identifying the property to which a transition effect should be applied when its value changes. This identifier is composed by case-insensitive letters `a` to `z`, numbers `0` to `9`, an underscore (`_`) or a dash(`-`). The first non-dash character must be a letter (that is: no number at the beginning of it, even preceded by a dash). Also, two dashes are forbidden at the beginning of the identifier.



## transition-timing-function



**Syntax**	[reference page](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function)

```css
/* Keyword values */
transition-timing-function: ease;
transition-timing-function: ease-in;
transition-timing-function: ease-out;
transition-timing-function: ease-in-out;
transition-timing-function: linear;
transition-timing-function: step-start;
transition-timing-function: step-end;

/* Function values */
transition-timing-function: steps(4, end);
transition-timing-function: cubic-bezier(0.1, 0.7, 1.0, 0.1);

/* Multiple timing functions */
transition-timing-function: ease, step-start, cubic-bezier(0.1, 0.7, 1.0, 0.1);

/* Global values */
transition-timing-function: inherit;
transition-timing-function: initial;
transition-timing-function: unset;
```









## Reference

[High Performance Animations](https://www.html5rocks.com/en/tutorials/speed/high-performance-animations/)

[Making the transition from animating in After Effects to CSS](https://medium.com/@ryan_brownhill/after-effects-to-css-79225c1d767e#.jfx6hr5gr)

[Ant Design](https://ant.design/index-cn)

[Material Design](https://material.io/)