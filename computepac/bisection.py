# Numerical Analysis
# Bisection Method to find roots of an equation
# With SymPy for function generalization
#
# To run, use:
#       f = function('f')
#       x = Symbol('x')
#       f = YOUR EQUATION
#
# Output format: [num_itr, root, total_time]
#

from sympy import *
import time


def bisection(f, a, b, acc):
    x = Symbol('x')
    start_time = time.time()                    # start timer
    error = 10                                  # before assignment in while loop
    err = []                                    # to store errors

    while error > acc:                          # if error still larger than desired accuracy

        m = (a + b) / 2                         # middle between bounds
        ans = f.evalf(subs={x: m})

        if ans > 0:
            error = abs(b - m)
            b = m

        elif ans < 0:
            error = abs(a - m)
            a = m

        err.append(error)

    end_time = time.time()
    total_time = end_time-start_time
    num_itr = len(err)
    root = m
    
    return [num_itr, root, total_time]
