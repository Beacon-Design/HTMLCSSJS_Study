# Keyboard_Key

## keycode()

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
    <meta charset="UTF-8">
    <title>Keyboard_Key</title>

    <script>
        // keycode()
        function kCode(event) {
            //alert(event.keyCode)
            var x = event.keyCode;
            document.getElementById("rtext").innerHTML = " Unicode 值为: " + x;
        }
    </script>
</head>

<body>
    <form name="rkCode">
        <input type="text" name="key" onKeyDown="kCode(event)">
    </form>
    <p id="rtext"></p>
</body>

</html>

```

