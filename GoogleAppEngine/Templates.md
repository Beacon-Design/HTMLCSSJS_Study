# Templates

## Helpful Tips

- always automatically escape variables when possibale
- minimize caode in templates
- minimazr html in code



## Jinja2 html template

#### app.yaml

```
application: templates
version: 1
runtime: python27
api_version: 1
threadsafe: yes

handlers:
- url: /favicon\.ico
  static_files: favicon.ico
  upload: favicon\.ico

- url: .*
  script: main.app

libraries:
- name: webapp2
  version: "2.5.2"
- name: jinja2
  version: latest
```



delete comment to run

> ```
> "{{}}" means print ; "name" is a variable
>
> === Note that the bracket and the percent sign needs to be next to each other such as: ===
>
> {% keyword %}
> AND NOT
> { % keyword % }
>
>
> === statement use python code ===
>
> {% statement %}
> output
> {% end statement %}
>
> --- example ---
>
> {% if name == "steve" %}
> Hello, Steve!
> {% else %}
> Who are you?
> {% endif %}
>
> === for loop syntax ===
>
> {% for statement %}
> body
> {% endfor %}
>
> === character escape and safe ===
>     <ul>
>         {% for item in items %}
>             <li>{{ item | safe }}</li>
>             <li>{{ item | escape }}</li>
>         {% endfor %}
>     </ul>
>     
>
> ```

### input n

html file:

```html
<!--Jinja2 templates-->

<form>
    <h2>Add a food!!!!</h2>
    <input type="text" name="food">
    <input type="hidden" name="food" value="eggs">
    <button>Add</button>
    <h2>Hi!! {{name}}</h2>

     <ol>
        {% for x in range(1,n+1) %}
            <li>{{x ** 2}}</li>
        {% endfor %}
    </ol>
  
{% if n == 1 %}
    n equals 1
{% else %}
    n does not equal 1
{% endif %}

</form>
```
python file :

```python
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        # self.write(form_html)
        n = self.request.get("n")
        if n:
            n = int(n)
        # self.render("shopping_list.html", n=n)
        self.render("shopping_list.html", name="Jim", n=n)

app = webapp2.WSGIApplication([('/', MainPage),
                               ],
                              debug = True)
```


### shopping list

html file :

```html
<!--Jinja2 templates-->

<form>
    <h2>Add a food!!!!</h2>
    <input type="text" name="food">
    {% if items %}
        {% for item in items %}
            <input type="hidden" name="food" value="{{item}}">
        {% endfor %}
    {% endif %}
    <button>Add</button>
    <h2>Hi!! {{name}}</h2>
    
    {% if items %}
    <br>
    <br>
    <h2>Shopping List</h2>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
    {% endif %}
</form>
```

python file :

```python
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)
# automatically escape variables


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("shopping_list.html", name="Jim", items = items)

class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        self.render('fizzbuzz.html', n = n)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/fizzbuzz.html', FizzBuzzHandler),
                               ],
                              debug = True)
```



### template inheritance

python file:

```python
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("shopping_list.html", name="Jim", items = items)

class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        self.render('fizzbuzz.html', n = n)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/fizzbuzz', FizzBuzzHandler),
                               ],
                              debug = True)
```

base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Templates</title>
    
</head>
<body>
   <h1 style="background-color: blue; color: gray">
       This is a Template!!!
   </h1>
   
    {% block content %}
    {% endblock %}
</body>
</html>
```

shopping_list.html

```html
<!--Jinja2 templates-->
{% extends "base.html" %}

{% block content %}
<form>
    <h2>Add a food!!!!</h2>
    <input type="text" name="food">
    {% if items %}
        {% for item in items %}
            <input type="hidden" name="food" value="{{item}}">
        {% endfor %}
    {% endif %}
    <button>Add</button>
    <h2>Hi!! {{name}}</h2>
    
    {% if items %}
    <br>
    <br>
    <h2>Shopping List</h2>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
    {% endif %}
</form>
{% endblock %}
```

fizzbuzz.html

```html
{% extends "base.html" %}
   
{% block content %}
<h2>FizzBuzz</h2>
<ol>
    {% for x in range(1, n+1) %}
    <li>
        {% if x % 15 ==0 %}
        FizzBuzz
        {% elif x % 5 ==0 %}
        Fizz
        {% elif x % 3 ==0 %}
        Buzz
        {% else %}
        {{ x }}
        {% endif %}
        </li>
    {% endfor %}
</ol>
{% endblock %}
```