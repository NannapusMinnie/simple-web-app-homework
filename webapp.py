import random
import time

from flask import Flask, render_template, request

from calcs import plot_expression

# Docs and examples for Flask: https://flask.palletsprojects.com/en/stable/
app = Flask(__name__)  # To run, use flask --app webapp run --debug

@app.route("/")  # http://127.0.0.1:5000/
def main_page():
    plot_file = ''
    user_input = request.args.get("func_expr", "")  # TODO: real input

    plot_ready = False

    if user_input.strip() != '':
        rnd_suffix = ''  # some random suffix to caching in browser
        plot_file = "test.png"
        plot_expression(user_input, 0, 4, "static/test.png")
        plot_ready = True

    return render_template('plot_func.html', plot_ready=plot_ready, func_expr=user_input)  # Add parameters for the template

@app.route("/test")  # http://127.0.0.1:5000/test
def test_route():
    x = random.randint(0, 10)

    return render_template('main_page.html', lucky_num=x)