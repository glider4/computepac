import pytest
import sympy as sym
from ..computepac import runge_kutta_four


class Test:
    def test_rkfour(self):
        f = sym.Function('f')
        x1 = sym.Symbol('x1')
        x2 = sym.Symbol('x2')
        f = (((5 * x1**2) - x2) / sym.exp(x1+x2))
        assert runge_kutta_four(f, 0, 1, 0, 1, 100)[0][99] == 1.06665177484571
