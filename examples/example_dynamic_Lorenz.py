# Example of the Lorenz Attractor solved by Adams-Bashforth-Moulton
# in the dynamic_triple module
#

from computepac.dynamic_triple import ABM


# Lorenz Attractor equations
def f1(x, y, z):
    return 10 * (y - x)


def f2(x, y, z):
    return x * (28 - z) - y


def f3(x, y, z):
    return (x * y) - (8 / 3) * z


res = ABM(f1, f2, f3, 0, 15, 15, 36, 0, 20, 1000)
print(res.adams()[2][100])
