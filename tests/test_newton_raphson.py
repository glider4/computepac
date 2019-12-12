import sympy as sym
from computepac import newton_raphson


class Test:
    def test_newton_raphson(self):
        f = sym.Function('f')
        x = sym.Symbol('x')
        f = (x ** 3) + 2 * (x ** 2) + 10 * x - 20
        assert newton_raphson(f, 2, 0.5e-12)[0] == 6
