class Utilities:
    def __init__(self):
        """Calculate relative error for testing purposes"""

    @staticmethod
    def calc_relative_error(calculated_val: float, correct_val: float) -> float:
        error = ((correct_val - calculated_val)/correct_val)*100
        return error

    @staticmethod
    def check_same_float(float_1: float, float_2: float, digits: int) -> bool:
        if round(float_1, digits) == round(float_2, digits):
            return True
        else:
            return False
