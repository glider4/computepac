# Runge-Kutta Four (RK4) iterative method to estimate ODE
# Knowing initial conditions x0 and y0
#
# To run, use:
#
#       import sympy as sym
#       f = sym.Function('f')
#       x1 = sym.Symbol('x1')
#       x2 = sym.Symbol('x2')
#       f = '''YOUR EQUATION with x1, x2 as x, y'''
#       rkfour(f, x0, y0, lower bound, upper bound, num steps)
#
# Note: do not use x or y as values.  Use x1, x2, etc.
# Output format: [y_values, total_time]
#

import sympy as sym
import time


def rkfour(
    f, x, y, a, b, n
) -> list:  # function, x0, y0, lower bound, upper bound, num steps
    x1 = sym.Symbol("x1")
    x2 = sym.Symbol("x2")
    start_time = time.time()

    p = 0  # flag
    h = (b - a) / n  # step size

    x_val = []
    y_val = []

    while p < n:

        k0 = h * f.evalf(subs={x1: x, x2: y})
        k1 = h * f.evalf(subs={x1: (x + (0.5 * h)), x2: (y + (0.5 * k0))})
        k2 = h * f.evalf(subs={x1: (x + (0.5 * h)), x2: (y + (0.5 * k1))})
        k3 = h * f.evalf(subs={x1: (x + h), x2: (y + k2)})

        x_val.append(x)
        y_val.append(y)

        x += h
        y = y + ((1 / 6) * (k0 + (2 * k1) + (2 * k2) + k3))

        p += 1

    end_time = time.time()
    total_time = end_time - start_time

    return [y_val, total_time]
