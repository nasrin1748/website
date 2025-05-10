def greet4():
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
<h1>Example4</h1><p>Example for Calling function on button click.</p>
    <h5>index.html</h5>
    <pre style="background-color:#f1f1f1;">
    <code>
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
&lt;button py-click="fun" id="get-time"&gt;Date&Time&lt;/button&gt;
    &lt;script type="py"&gt;
        from pyscript import display
        from datetime import datetime
        now = datetime.now()
        def fun(event):
            print(now.strftime("%m/%d/%Y, %H:%M:%S"))
            display(now.strftime("%m/%d/%Y, %H:%M:%S"))
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>
</code>
<p>The following example displays date and time on terminal and DOM on button click.</p>
<div id="div-01">
<h6>Output</h6>
<p></p></div>
     <button id="greet-button">Get Greeting</button>   
<br/>     
    <script type="py" terminal>
from pyscript import when,display 
from datetime import datetime
now = datetime.now()
@when("click", "#greet-button") 
def click_handler(event):
    print('\033[H', end = "")
    print(now.strftime("%m/%d/%Y, %H:%M:%S"))
    display(now.strftime("%m/%d/%Y, %H:%M:%S"),append=False)
    </script>
</body>
</html>
    """
    return html_content
