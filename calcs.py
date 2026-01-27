import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_expression(expr_str, a, b, plot_file, color):
    n = 100

    x_vals = np.linspace(a, b, n + 1)

    y_vals = []
    for x in x_vals:
        y = eval(expr_str, {"x": x, "math": math})
        y_vals.append(y)

    plt.plot(x_vals, y_vals, color=color)
    plt.savefig(plot_file)
    plt.clf()