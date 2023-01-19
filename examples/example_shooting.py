# Example of the Shooting Method

import numpy as np
import sympy as sym
from computepac.shooting_method import shooting

f = sym.Function("f")
x1 = sym.Symbol("x1")
c1 = (8 * (np.pi ** 2))
c2 = 0
f = sym.log(c1) - 2 * sym.log(sym.cos(0.9939931166 * x1) + c2)

# alpha and beta are the same
alpha = np.log(8 * (np.pi ** 2))
beta = np.log(8 * (np.pi ** 2))

# num iterations
n = 10

# initial Z1 and Z2 given
Z1 = (-23 / 2)
Z2 = (-25 / 2)

res = shooting(f, Z1, Z2, alpha, beta, n)

print("\nShooting Method Results")
print("====================================================\n")
print("     Solution Convergence Demonstration:\n ")
print("   Z Value                 Solution")

for i in range(0, 2):  # need extra tab spacing for first 2 lines
    print(" ", res[0][i], " \t\t\t\t", res[1][i])

for i in range(2, 11):
    print(" ", res[0][i], " \t", res[1][i])

print("\nCompare to actual solution:", alpha)
print("\nTotal time for computation:", res[2])
print("====================================================\n")
