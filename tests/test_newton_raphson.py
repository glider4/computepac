import sympy as sym
from computepac import newton_raphson
from computepac.utils.utilities import Utilities


class Test:
    def test_newton_raphson(self):
        f = sym.Function("f")
        x = sym.Symbol("x")
        f = (x ** 3) + 2 * (x ** 2) + 10 * x - 20
        ans = newton_raphson(f, 2, 0.5e-12)[0]
        assert Utilities.check_same_float(ans, 6.0, 1) is True
