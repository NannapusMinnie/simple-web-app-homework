import random
from mistral_api_demo import text_to_expression

from flask import Flask, render_template, request

from calcs import plot_expression

# Docs and examples for Flask: https://flask.palletsprojects.com/en/stable/
app = Flask(__name__)  # To run, use flask --app webapp run --debug

@app.route("/")
def index():
    return render_template("APIplot_func.html")

@app.route("/plot_graph_api")
def plot_graph_api():
    user_text = request.args.get("func_expr", "").strip()

    if not user_text:
        return {"error": "empty input"}
    
    python_expr, a, b, color = text_to_expression(user_text)

    rnd_suffix = random.randint(0, 1000000)

    plot_file = f"plot_{rnd_suffix}.png"
    plot_expression(python_expr, a, b, f"static/{plot_file}", color)

    return {
            "plot_image_url": f"static/{plot_file}",
            "expression": python_expr,
            "interval": [a, b],
            "color": color
            }
