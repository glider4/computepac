import pytest
import sympy as sym
from computepac import euler_forward


class Test:
    def test_euler(self):
        f = sym.Function('f')
        x1 = sym.Symbol('x1')
        x2 = sym.Symbol('x2')
        f = 6 - 2*(x2 / x1)
        assert round(euler_forward(f, 3, 1, 3, 6, 100)[0][99], 5) == 10.72864
