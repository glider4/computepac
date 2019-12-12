import sympy as sym
from computepac import rktwo


class Test:
    def test_rktwo(self):
        f = sym.Function('f')
        x1 = sym.Symbol('x1')
        x2 = sym.Symbol('x2')
        f = (((5 * x1**2) - x2) / sym.exp(x1+x2))
        assert round(rktwo(f, 0, 1, 0, 1, 100)[0][99], 5) == 1.00058
