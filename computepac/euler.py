# Euler's method iterative scheme to estimate ODE - EXPLICIT (Forward)
# and IMPLICIT (Backwards).
#
# You have to know the DERIVATIVE of the function to utilize this method
# Ex. you know dy/dx and a certain point like y(3) = 1.
#
# To run, use:
#
#       import sympy as sym
#       f = sym.Function('f')
#       x1 = sym.Symbol('x1')
#       x2 = sym.Symbol('x2')
#       f = '''dy/dx equation with x1, x2 as x, y'''
#       euler_[ ](f, x0, y0, lower bound, upper bound, num steps)
#
# Note: do not use x or y as values.  Use x1, x2, etc.
#
# Output format: [y_values, total_time]
#

import sympy as sym
import time


def euler_forward(f, x, y, a, b, n) -> list:    # function, x0, y0, lower bound, upper bound, num steps
    x1 = sym.Symbol('x1')
    x2 = sym.Symbol('x2')
    start_time = time.time()

    p = 0                               # flag
    h = (b - a) / n                     # step size

    x_val = []
    y_val = []

    while p < n:
        x_val.append(x)
        y_val.append(y)

        x += h
        y = y + h * f.evalf(subs={x1: x, x2: y})

        p += 1

    end_time = time.time()
    total_time = end_time - start_time

    return [y_val, total_time]


def euler_backward(f, x, y, a, b, n) -> list:   # function, x0, y0, lower bound, upper bound, num steps
    x1 = sym.Symbol('x1')
    x2 = sym.Symbol('x2')
    start_time = time.time()

    p = 0                               # flag
    h = (b - a) / n                     # step size

    x_val = []
    y_val = []

    while p < n:
        x_val.append(x)
        y_val.append(y)

        x += h
        y_p = y + h * f.evalf(subs={x1: x, x2: y})
        y = y + h * f.evalf(subs={x1: x+h, x2: y_p})

        p += 1

    end_time = time.time()
    total_time = end_time - start_time

    return [y_val, total_time]
