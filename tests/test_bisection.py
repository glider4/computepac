import pytest
import sympy as sym
from ..computepac import bisection

class Test:
    def test_bisection(self):
        f = sym.Function('f')
        x = sym.Symbol('x')
        f = (x ** 3) + 2 * (x ** 2) + 10 * x - 20
        assert bisection(f, 1.0, 2.0, 0.5e-12) == []
