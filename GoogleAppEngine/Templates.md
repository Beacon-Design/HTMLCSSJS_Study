# Templates





## Jinja2 html template

delete comment to run

> ```
> "{{}}" means print ; "name" is a variable
>
>
> --- statement use python code ---
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
> ```

```html
<!--Jinja2 templates-->



<form>
    <h2>Add a food!!!!</h2>
    <input type="text" name="food">
    <input type="hidden" name="food" value="eggs">
    <button>Add</button>
    <h2>Hi!! {{name}}</h2>
    <!--    "{{}}" means print ; "name" is a variable-->
        
    
<!--    statement use python code    

{% statement %}
output
{% end statement %}

{% if name == "steve" %}
Hello, Steve!
{% else %}
Who are you?
{% endif %}

-->

{% if n == 1 %}
    n equals 1
{% else %}
    n does not equal 1
{% endif %}

</form>

```