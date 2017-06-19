



# module turtle

https://docs.python.org/3.4/library/turtle.html



## dir(turtle)

```
>>> import turtle
>>> dir(turtle)
['Canvas', 'Pen', 'RawPen', 'RawTurtle', 'Screen', 'ScrolledCanvas', 'Shape', 'TK', 'TNavigator', 'TPen', 'Tbuffer', 'Terminator', 'Turtle', 'TurtleGraphicsError', 'TurtleScreen', 'TurtleScreenBase', 'Vec2D', '_CFG', '_LANGUAGE', '_Root', '_Screen', '_TurtleImage', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__forwardmethods', '__loader__', '__methodDict', '__methods', '__name__', '__package__', '__spec__', '__stringBody', '_alias_list', '_getpen', '_getscreen', '_screen_docrevise', '_tg_classes', '_tg_screen_functions', '_tg_turtle_functions', '_tg_utilities', '_turtle_docrevise', '_ver', 'addshape', 'back', 'backward', 'begin_fill', 'begin_poly', 'bgcolor', 'bgpic', 'bk', 'bye', 'circle', 'clear', 'clearscreen', 'clearstamp', 'clearstamps', 'clone', 'color', 'colormode', 'config_dict', 'deepcopy', 'defstr', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'end_fill', 'end_poly', 'exitonclick', 'fd', 'fillcolor', 'filling', 'forward', 'get_poly', 'get_shapepoly', 'getcanvas', 'getmethparlist', 'getpen', 'getscreen', 'getshapes', 'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'inspect', 'isdown', 'isfile', 'isvisible', 'join', 'left', 'listen', 'lt', 'mainloop', 'math', 'methodname', 'mode', 'numinput', 'onclick', 'ondrag', 'onkey', 'onkeypress', 'onkeyrelease', 'onrelease', 'onscreenclick', 'ontimer', 'pd', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pl1', 'pl2', 'pos', 'position', 'pu', 'radians', 'read_docstrings', 'readconfig', 'register_shape', 'reset', 'resetscreen', 'resizemode', 'right', 'rt', 'screensize', 'seth', 'setheading', 'setpos', 'setposition', 'settiltangle', 'setundobuffer', 'setup', 'setworldcoordinates', 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 'shearfactor', 'showturtle', 'simpledialog', 'speed', 'split', 'st', 'stamp', 'sys', 'textinput', 'tilt', 'tiltangle', 'time', 'title', 'towards', 'tracer', 'turtles', 'turtlesize', 'types', 'undo', 'undobufferentries', 'up', 'update', 'width', 'window_height', 'window_width', 'write', 'write_docstringdict', 'xcor', 'ycor']
```



### bgcolor()

> ```
> Help on function bgcolor in module turtle:
>
> bgcolor(*args)
>     Set or return backgroundcolor of the TurtleScreen.
>     
>     Arguments (if given): a color string or three numbers
>     in the range 0..colormode or a 3-tuple of such numbers.
>     
>     Example:
>     >>> bgcolor("orange")
>     >>> bgcolor()
>     'orange'
>     >>> bgcolor(0.5,0,0.5)
>     >>> bgcolor()
>     '#800080'
> ```



### color()

> ```
> Help on function color in module turtle:
>
> color(*args)
>     Return or set the pencolor and fillcolor.
>     
>     Arguments:
>     Several input formats are allowed.
>     They use 0, 1, 2, or 3 arguments as follows:
>     
>     color()
>         Return the current pencolor and the current fillcolor
>         as a pair of color specification strings as are returned
>         by pencolor and fillcolor.
>     color(colorstring), color((r,g,b)), color(r,g,b)
>         inputs as in pencolor, set both, fillcolor and pencolor,
>         to the given value.
>     color(colorstring1, colorstring2),
>     color((r1,g1,b1), (r2,g2,b2))
>         equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
>         and analogously, if the other input format is used.
>     
>     If turtleshape is a polygon, outline and interior of that polygon
>     is drawn with the newly set colors.
>     For mor info see: pencolor, fillcolor
>     
>     Example:
>     >>> color('red', 'green')
>     >>> color()
>     ('red', 'green')
>     >>> colormode(255)
>     >>> color((40, 80, 120), (160, 200, 240))
>     >>> color()
>     ('#285078', '#a0c8f0')
> ```





### exitonclick()

> ```
> Help on function exitonclick in module turtle:
>
> exitonclick()
>     Go into mainloop until the mouse is clicked.
>     
>     No arguments.
>     
>     Bind bye() method to mouseclick on TurtleScreen.
>     If "using_IDLE" - value in configuration dictionary is False
>     (default value), enter mainloop.
>     If IDLE with -n switch (no subprocess) is used, this value should be
>     set to True in turtle.cfg. In this case IDLE's mainloop
>     is active also for the client script.
>     
>     This is a method of the Screen-class and not available for
>     TurtleScreen instances.
>     
>     Example:
>     >>> exitonclick()
> ```







### forward()

> ```
> Help on function forward in module turtle:
>
> forward(distance)
>     Move the turtle forward by the specified distance.
>     
>     Aliases: forward | fd
>     
>     Argument:
>     distance -- a number (integer or float)
>     
>     Move the turtle forward by the specified distance, in the direction
>     the turtle is headed.
>     
>     Example:
>     >>> position()
>     (0.00, 0.00)
>     >>> forward(25)
>     >>> position()
>     (25.00,0.00)
>     >>> forward(-75)
>     >>> position()
>     (-50.00,0.00)
> ```





### left()

> ```
> Help on function left in module turtle:
>
> left(angle)
>     Turn turtle left by angle units.
>     
>     Aliases: left | lt
>     
>     Argument:
>     angle -- a number (integer or float)
>     
>     Turn turtle left by angle units. (Units are by default degrees,
>     but can be set via the degrees() and radians() functions.)
>     Angle orientation depends on mode. (See this.)
>     
>     Example:
>     >>> heading()
>     22.0
>     >>> left(45)
>     >>> heading()
>     67.0
> ```







### right()

> ```
> Help on function right in module turtle:
>
> right(angle)
>     Turn turtle right by angle units.
>     
>     Aliases: right | rt
>     
>     Argument:
>     angle -- a number (integer or float)
>     
>     Turn turtle right by angle units. (Units are by default degrees,
>     but can be set via the degrees() and radians() functions.)
>     Angle orientation depends on mode. (See this.)
>     
>     Example:
>     >>> heading()
>     22.0
>     >>> right(45)
>     >>> heading()
>     337.0
> ```







### Screen()

> ```
> Help on function Screen in module turtle:
>
> Screen()
>     Return the singleton screen object.
>     If none exists at the moment, create a new one and return it,
>     else return the existing one.
> ```





### shape()

> ```
> Help on function shape in module turtle:
>
> shape(name=None)
>     Set turtle shape to shape with given name / return current shapename.
>     
>     Optional argument:
>     name -- a string, which is a valid shapename
>     
>     Set turtle shape to shape with given name or, if name is not given,
>     return name of current shape.
>     Shape with name must exist in the TurtleScreen's shape dictionary.
>     Initially there are the following polygon shapes:
>     'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
>     To learn about how to deal with shapes see Screen-method register_shape.
>     
>     Example:
>     >>> shape()
>     'arrow'
>     >>> shape("turtle")
>     >>> shape()
>     'turtle'
> ```



### speed()

> ```
> Help on function speed in module turtle:
>
> speed(speed=None)
>     Return or set the turtle's speed.
>     
>     Optional argument:
>     speed -- an integer in the range 0..10 or a speedstring (see below)
>     
>     Set the turtle's speed to an integer value in the range 0 .. 10.
>     If no argument is given: return current speed.
>     
>     If input is a number greater than 10 or smaller than 0.5,
>     speed is set to 0.
>     Speedstrings  are mapped to speedvalues in the following way:
>         'fastest' :  0
>         'fast'    :  10
>         'normal'  :  6
>         'slow'    :  3
>         'slowest' :  1
>     speeds from 1 to 10 enforce increasingly faster animation of
>     line drawing and turtle turning.
>     
>     Attention:
>     speed = 0 : *no* animation takes place. forward/back makes turtle jump
>     and likewise left/right make the turtle turn instantly.
>     
>     Example:
>     >>> speed(3)
> ```