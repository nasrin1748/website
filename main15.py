def greet15():
    html_content = f"""
from pyscript import display,HTML
import os    
def click_handler(): 
    x = int(input("enter the value of a: "))
    y = int(input("enter the value of b: "))
    c = x+y
    print(c)
    """
    return html_content
