"""
This is a simple program to plot and compute the derivative of a function
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x)

def tangent(x, x0, y0,m0):
    return m0*(x - x0) + y0

def save_derivative_plot(N):
    x = np.linspace(-2, 2, N)
    y = f(x)

    fig, ax = plt.subplots(figsize=(10, 5))

    # Do a plot of the function
    ax.plot(x, y, 'lightblue')
    if N<=31:
        ms = 5 - N/15
        ax.plot(x, y, 'lightblue', marker='s', markersize=3)

    # Do a plot of the derivative at x = 0
    n = N//2
    xl = x[n-1]
    xc = x[n]
    xr = x[n+1]
    yl = y[n-1]
    yc = y[n]
    yr = y[n+1]
    # Compute the derivative
    m = (yr - yl) / (xr - xl)

    # Plot the tangent line at xc
    xline = np.linspace(xl, xr, 101)
    yline = tangent(xline, xc, yc, m)
    ax.plot(xline, yline, color='red', )

    # Annotate the plot
    ax.text(0.5, 0.5, f'$f\'(0)={m:.2f}$', transform=ax.transAxes, fontsize=14, ha='right', va='top')

    ax.set_xlabel('$x$')
    ax.set_ylabel('$e^x$')
    ax.set_title(f'Cálculo numérico de la derivada de $e^x$ en $x={xc:.2f}$ usando $\Delta x={xr-xl:.2f}$')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 7)
    fig.savefig(f'derivada_{N}.png', dpi=300)
    #plt.show()

save_derivative_plot(5)
save_derivative_plot(7)
save_derivative_plot(9)
save_derivative_plot(11)
save_derivative_plot(21)
save_derivative_plot(31)
