# Example using Euler to estimate an ODE
# Comparing euler_foward and euler_backward
#
# Equation to estimate:s
#
#   dy/dx = 6 - 2 * (y/x)
#
#   We know the solution at y(3) is 1
#   We want to know the solution at y(12)
#
#   The exact solution is known y(12) = 23.6875
#
# How to run this example:
#
#   Use example_euler(n), where n = number of iterations
#   Note that this example is hard coded for one ODE
#

import sympy as sym
from computepac import euler_forward, euler_backward


def example_euler(n):

    f = sym.Function('f')
    x1 = sym.Symbol('x1')
    x2 = sym.Symbol('x2')
    f = 6 - 2 * (x2 / x1)

    resultf = euler_forward(f, 3, 1, 3, 12, n)
    resultb = euler_backward(f, 3, 1, 3, 12, n)

    print("\nResult of", n, "iterations FORWARD method to estimate f(12) =", resultf[0][n-1])
    print("Result of", n, "iterations BACKWARD method to estimate f(12) =", resultb[0][n - 1])
    print("\nTime for FORWARD computation", round(resultf[1], 3), "seconds")
    print("Time for BACKWARD computation", round(resultb[1], 3), "seconds")
    print("\nExact solution known as 23.6875")
    print("\nFORWARD Relative error:", round(((abs(23.6875 - resultf[0][n-1]) / 23.6875)*100), 5), "%")
    print("BACKWARD Relative error:", round(((abs(23.6875 - resultb[0][n - 1]) / 23.6875) * 100), 5), "%\n")


if __name__ == '__main__':
    example_euler(10000)
