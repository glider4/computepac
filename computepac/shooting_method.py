# Shooting method
#
# Explanation
#
#
# To run, use:
#
#       import sympy as sym
#       f = sym.Function('f')
#       x1 = sym.Symbol('x1')
#       f = '''Equation with t variable as x1'''
#       shooting()
#
# Note: do not use x as a variable in the function.  Use x1.
#
# Output format: [values, solution, total_time]
#

import sympy as sym
import time


def shooting(f, Z1, Z2, alpha, beta, n) -> list: # n is for number of iterations

    start_time = time.time()
    x1 = sym.Symbol("x1")
    i = 0
    solution = []
    valset = []

    # formula to solve for Z3 - using a, A, b, B for ease
    def newZ(a, A, b, B):
        VAL = a + (beta - A) * ((a - b) / (A - B))
        return VAL

    valset.append(Z2)
    valset.append(Z1)

    while i < (n+1):
        VAL = newZ(Z1, f.evalf(subs={x1: Z1}), Z2, f.evalf(subs={x1: Z2}))

        # redefine values for next iteration
        Z2 = Z1
        Z1 = VAL

        # move onto next iteration
        i += 1

        valset.append(VAL)

        # append equation result of new Z into solution set
        solution.append(f.evalf(subs={x1: Z1}))

    end_time = time.time()
    total_time = end_time - start_time

    return [valset, solution, total_time]
