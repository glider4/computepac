import sympy as sym
from computepac import bisection
from computepac.utils.utilities import Utilities
from computepac.dynamic_triple import ABM


class Test:
    def test_abm(self):
        # Lorenz Attractor equations
        def f1(x, y, z):
            return 10 * (y - x)

        def f2(x, y, z):
            return x * (28 - z) - y

        def f3(x, y, z):
            return (x * y) - (8 / 3) * z

        compute_test = ABM(f1, f2, f3, 0, 15, 15, 36, 0, 20, 1000)
        ans = compute_test.adams()[2][100]
        assert Utilities.calc_relative_error(ans, 29.386854067862377) < 0.000001
