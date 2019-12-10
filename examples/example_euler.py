# Example using Euler to estimate an ODE
# Equation:
#   dy/dx = 6 - 2 * (y/x)
#
#   We know the solution at y(3) is 1
#   I want to know the solution at y(12)
#
#   The exact solution is known y(12) = 23.6875
#

import sympy as sym
from computepac import euler


def example_euler(n):

    f = sym.Function('f')
    x1 = sym.Symbol('x1')
    x2 = sym.Symbol('x2')
    f = 6 - 2 * (x2 / x1)

    result = euler(f, 3, 1, 3, 12, n)

    print("\nResult of", n, "iterations of Euler's method to estimate f(12) =", result[0][n-1])
    print("Time for computation", round(result[1], 3), "seconds")
    print("\nExact solution known as 23.6875")
    print("Relative error:", round(((abs(23.6875 - result[0][n-1]) / 23.6875)*100), 5), "%\n")


if __name__ == '__main__':
    example_euler(1000)
