# Example of the Lorenz Attractor solved by Adams-Bashforth-Moulton
# in the dynamic_triple module
#
# Should be run in an IDE like Anaconda.  May not work with PyCharm.

from computepac import *


# Lorenz Attractor equations
def f1(x, y, z):
    return 10 * (y - x)


def f2(x, y, z):
    return x * (28 - z) - y


def f3(x, y, z):
    return (x * y) - (8/3)*z


abm_comp(f1, f2, f3, 0, 15, 15, 36, 0, 20, 1000)

