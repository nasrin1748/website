def greet14():
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Calling Python from JS</title>
        <link rel="stylesheet" href="https://pyscript.net/releases/2024.10.1/core.css">
        <script type="module" src="https://pyscript.net/releases/2024.10.1/core.js"></script>
    </head>
    <body>
        <button onclick="handleJavaScript()">JavaScript</button>
        <button onclick="handlePython()">Python</button>

        <script>
            window.handleJavaScript = () => alert("JavaScript")
        </script>     

        <script type="py" terminal>
          import js
import pyscript

def showPythonMessage():
    js.window.alert("This message was shown in Python")


# Make our Python function visible to JavaScript by adding it to window
function = pyscript.ffi.create_proxy(showPythonMessage)
js.window.handlePython = function

        </script>
    </body>
</html>
    """
    return html_content
