def greet13():
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Rapid Field</title>

    <!-- Recommended meta tags -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">

    <!-- PyScript CSS -->
    <link rel="stylesheet" href="https://pyscript.net/releases/2024.4.1/core.css">

    <!-- This script tag bootstraps PyScript -->
    <script type="module" src="https://pyscript.net/releases/2024.4.1/core.js"></script>
</head>
<body>
    <textarea id="input1" name="html" rows="20" cols="200"></textarea>
    <button id="run">Run</button>
<button id="clearTerm">Click to Clear</button>  

<script type="py" terminal>
from pyscript import when, display,document   

@when("click","#clearTerm")    
def clearTerm(evt):
    terminal_element = document.querySelector("script[type='py'][terminal]")
    terminal_element.terminal.clear() 

@when("click", "#run")
def click_handler(event):
    f = document.getElementById("input1").value
    exec(f)
    import js
    x = js.input()
    print(x)   
</script>    
</body>
    <script src='main.js'></script>    
</html>
    """
    return html_content
