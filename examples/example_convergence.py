# Testing convergence of bisection and newton-raphson schemes
#   Both schemes be optimized further by setting the
#   bounds [a,b] for Bisection, and setting the initial
#   guess for Newton-Raphson.  Right now I used [-10,10]
#   for bisection and a guess of 0 for newton-raphson,
#   because these seemed reasonable for a variety of equations.
#
# For this test I used an accuracy of 0.5e-12.

from sympy import Function, Symbol
from sympy.plotting import plot
from computepac import *


def convergence(f, acc):

    print("\nFunction to find roots of:", f)
    print("======================================================\n")

    print("Bisection results:")
    bisec_res = bisection(f, -10, 10, acc)
    print("\nNum iterations needed:", bisec_res[0])
    print("Estimated root:", bisec_res[1])
    print("Execution time:", bisec_res[2], "seconds")

    print("\n======================================================\n")

    print("Newton-Raphson results:")
    newt_res = newton_raphson(f, 0, acc)
    print("\nNum iterations needed:", newt_res[0])
    print("Estimated root:", newt_res[1])
    print("Execution time:", newt_res[2], "seconds")

    print("\n======================================================")

    plot(f)


if __name__ == '__main__':
    x = Symbol('x')
    f = Function('f')

    f = 6 * x ** 3 + 4 * x ** 2 + x + 1  # Enter function to find roots of

    convergence(f, 0.5e-12)
