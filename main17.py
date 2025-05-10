def greet17():
    import pandas as pd
    import numpy as np
    from pyscript import display, HTML

    custom_styling = [
        {
            "selector": "th",
            "props": [
                ("background", "#00abe7"),
                ("color", "white"),
                ("font-family", "tahoma"),
                ("text-align", "center"),
                ("font-size", "15px"),
            ],
        },
        {
            "selector": "td",
            "props": [
                ("font-family", "tahoma"),
                ("color", "black"),
                ("text-align", "left"),
                ("font-size", "15px"),
            ],
        },
        {
            "selector": "tr:nth-of-type(odd)",
            "props": [
                ("background", "white"),
            ],
        },
        {"selector": "tr:nth-of-type(even)", "props": [("background", "#e8e6e6")]},
        {"selector": "tr:hover", "props": [("background-color", "#bfeaf9")]},
        {"selector": "td:hover", "props": [("background-color", "#7fd5f3")]},
    ]

    df = pd.DataFrame(np.random.randint(0, 100, (2, 200)))
    s1 = df.style
    s1.set_table_styles(custom_styling)
    return "<div style='width: 700px; overflow: auto;'>" + s1.to_html() + "</div>"




