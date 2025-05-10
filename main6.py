def greet6():
    html_content = f"""
   <!DOCTYPE html>
<html lang="en">
<head>
    <title>Green Wildflower</title>

    <!-- Recommended meta tags -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">

    <!-- PyScript CSS -->
   <link rel="stylesheet" href="https://pyscript.net/releases/2024.10.1/core.css">
    <script defer src="https://pyscript.net/releases/2024.10.1/core.js"></script>
</head>
<body>
<h1>Example6</h1><p>Example for Adding two numbers using @when decorator.</p>
    <h5>index.html</h5>
    <pre style="background-color:#f1f1f1;">
    <code onmousedown="return false" onselectstart="return false">
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
&lt;title&gt;Yellow Cloud&lt;/title&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width,initial-scale=1.0"&gt;
    &lt;link rel="stylesheet" href="https://pyscript.net/releases/2024.8.1/core.css"&gt;
    &lt;script type="module" src="https://pyscript.net/releases/2024.8.1/core.js"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;Addition Calculator&lt;/h1&gt;
&lt;p&gt;input 1: &lt;input id="input1" size="5"/&gt;&lt;/p&gt;&lt;br&gt;
&lt;p&gt;input 2: &lt;input id="input2" size="5"/&gt;&lt;/p&gt;&lt;br&gt;
&lt;button id="add" onclick='myFunction'&gt;Submit&lt;/button&gt;           
&lt;script type="py" &gt;
from pyscript import display,when
@when("click", "#add")    
def myFunction(event): 
       from pyscript import document
       num1 = document.getElementById("input1").value
       num2 = document.getElementById("input2").value
       c = int(num1)+int(num2)
       display(num1)
       display(num2)
       display(c)
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt; 
</pre>
</code>
<p>The following example displays Addition of two numbers taken from input1 and input2.</p>
<div id="div-01">
<h6>Output</h6>
<p>input 1: <input id="input1" size="5"/></p><br>
<p>input 2: <input id="input2" size="5"/></p><br>
<button id="add">Submit</button>
<p></p></div>
<br/>     
    <script type="py">    
from pyscript import when,display 
from datetime import datetime
now = datetime.now()
@when("click", "#add")
def add(event):
    from pyscript import document
    num1 = document.getElementById("input1").value
    num2 = document.getElementById("input2").value
    c = int(num1)+int(num2)
    display(num1)
    display(num2)
    display(c)
    </script>
</body>
</html>
    """
    return html_content
