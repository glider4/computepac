import sympy as sym
from computepac import euler_forward
from computepac import euler_backward
from computepac.utils.utilities import Utilities


class Test:
    def test_euler_forward(self):
        f = sym.Function('f')
        x1 = sym.Symbol('x1')
        x2 = sym.Symbol('x2')
        f = 6 - 2*(x2 / x1)
        ans = euler_forward(f, 3, 1, 3, 6, 100)[0][99]
        assert Utilities.calc_relative_error(ans, 10.72684) < 0.0001


    def test_euler_backward(self):
        f = sym.Function('f')
        x1 = sym.Symbol('x1')
        x2 = sym.Symbol('x2')
        f = 6 - 2 * (x2 / x1)
        ans = euler_backward(f, 3, 1, 3, 6, 100)[0][99]
        assert Utilities.calc_relative_error(ans, 10.69012) < 0.0001
