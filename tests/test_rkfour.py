import sympy as sym
from computepac import rkfour
from computepac.utils.utilities import Utilities


class Test:
    def test_rkfour(self):
        f = sym.Function('f')
        x1 = sym.Symbol('x1')
        x2 = sym.Symbol('x2')
        f = (((5 * x1**2) - x2) / sym.exp(x1+x2))
        ans = round(rkfour(f, 0, 1, 0, 1, 100)[0][99], 5)
        assert Utilities.calc_relative_error(ans, 1.06665) < 0.0001
