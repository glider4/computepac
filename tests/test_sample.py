# Sample unit test that will always pass


def mult_zero(x):
    return x*0


class Test:
    def test_mult_zero(self):
        assert mult_zero(600) == 0
