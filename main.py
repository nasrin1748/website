def greet():
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
<h1>Introduction</h1><p>PyScript allows you to create rich Python applications in the browser using HTML and Python code.<br/>The easiest way to get a PyScript development environment and hosting, is to use <a href="https://pyscript.com">pyscript.com</a>
in your browser.</p>
All PyScript applications need three things:
<li>An index.html file that is served to your browser.</li>
<li>pyscript.toml file where you specify your packages and files(default name is pyscript.toml but can be .toml file with any name)</li>
<li>Python code (usually in a file called something like main.py) that defines how your application works.</li>
<p>Alternately just use index.html where inside py-config tag specify your packages and files,write your Python code inside script tag.</p>
<p>Inside script tag if you specify your src="./main.py" config="./pyscript.toml" means you are going to write your python code in main.py and mention packages,files in pyscript.toml alternately just remove the src="./main.py" and write your code within script tags or just remove config="./pyscript.toml" when you don't need any packages for your code.</p>
<p>Always follow the following order for ./pyscript.toml</p>
<pre style="background-color:#f1f1f1;">
<code>
"packages" = ["package-name"]
[files]
"example.txt" = "example.txt"
</code>
</pre>
<p>"In pyscript prints goto terminal and display goto DOM"</p>
<h5>Simple example showing index.html,main.py,pyscript.toml specifying packages and files</h5>
<h6>index.html</h6>
<pre style="background-color:#f1f1f1;">
<code>
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
&lt;title&gt;Yellow Cloud&lt;/title&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width,initial-scale=1.0"&gt;
    &lt;link rel="stylesheet" href="https://pyscript.net/releases/2024.7.1/core.css"&gt;
    &lt;script type="module" src="https://pyscript.net/releases/2024.7.1/core.js"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;script type="py" src="./main.py" config="./pyscript.toml" terminal&gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code>
</pre>
<h6>main.py</h6>
<pre style="background-color:#f1f1f1;">
<code>
import numpy as np
from pyscript import display
from pyodide.ffi import to_js, create_once_callable
x = np.arange(15, dtype=np.int64).reshape(3, 5)
x[1:, ::2] = -99
print(x)
display(x)
</code>
</pre>
<h6>pyscript.toml</h6>
<pre style="background-color:#f1f1f1;">
<code>
name = "Yellow Cloud"
packages=["numpy"]
</code>
</pre>
<h5>Simple example showing index.html specifying packages and files</h5>
<h6>index.html</h6>
<pre style="background-color:#f1f1f1;">
<code>
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
&lt;title&gt;Yellow Cloud&lt;/title&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width,initial-scale=1.0"&gt;
    &lt;link rel="stylesheet" href="https://pyscript.net/releases/2024.7.1/core.css"&gt;
    &lt;script type="module" src="https://pyscript.net/releases/2024.7.1/core.js"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;py-config&gt;
        "packages" = ["numpy"]
    &lt;/py-config&gt;
&lt;script type="py" terminal&gt;
     import numpy as np
     from pyscript import display
     x = np.arange(15, dtype=np.int64).reshape(3, 5)
     x[1:, ::2] = -99
     print(x)
     display(x)
&lt;/script&gt;  
&lt;/body&gt;
&lt;/html&gt;
</code>
</pre>
    """
    return html_content
