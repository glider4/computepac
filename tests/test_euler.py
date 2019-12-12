import sympy as sym
from computepac import euler_forward
from computepac import euler_backward


class Test:
    def test_euler_forward(self):
        f = sym.Function('f')
        x1 = sym.Symbol('x1')
        x2 = sym.Symbol('x2')
        f = 6 - 2*(x2 / x1)
        assert round(euler_forward(f, 3, 1, 3, 6, 100)[0][99], 5) == 10.72864


    def test_euler_backward(self):
        f = sym.Function('f')
        x1 = sym.Symbol('x1')
        x2 = sym.Symbol('x2')
        f = 6 - 2 * (x2 / x1)
        assert round(euler_backward(f, 3, 1, 3, 6, 100)[0][99], 5) == 10.69012