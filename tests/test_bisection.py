import sympy as sym
from computepac import bisection
from computepac.utils.utilities import Utilities


class Test:
    def test_bisection(self):
        f = sym.Function("f")
        x = sym.Symbol("x")
        f = (x ** 3) + 2 * (x ** 2) + 10 * x - 20
        ans = bisection(f, 1.0, 2.0, 0.5e-12)[0]
        assert Utilities.check_same_float(ans, 41.0, 1) is True
