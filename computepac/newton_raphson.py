# Numerical Analysis
# Newton-Raphson Method to find roots of an equation
# Uses derivative of equation in iterative scheme
#
# To run, use:
#
#       import sympy as sym
#       f = sym.Function('f')
#       x = sym.Symbol('x')
#       f = '''YOUR EQUATION'''
#       newton_raphson(f, guess of root, accuracy desired)
#
# Output format: [num_itr, root, total_time]
#

import sympy as sym
import time


def newton_raphson(f, g, acc):
    x = sym.Symbol('x')             # set up x as symbol for functions below
    start_time = time.time()
    f_prime = sym.diff(f)           # derivative of inputted function
    err = []                        # to store errors
    made_accuracy = 0               # (flag) program has not achieved proper accuracy yet

    while made_accuracy == 0:       # if desired accuracy not reached yet

        g_1 = g - (f.evalf(subs={x: g}) / f_prime.evalf(subs={x: g}))

        error = abs(g_1 - g)
        err.append(error)

        if error < acc:
            made_accuracy = 1       # signal flag to end computation if accuracy has been reached
        else:
            g = g_1                 # otherwise, continue iterating

    end_time = time.time()
    total_time = end_time-start_time
    num_itr = len(err)
    root = g

    return [num_itr, root, total_time]
