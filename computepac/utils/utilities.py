class Utilities:
    def __init__(self):
        """Calculate relative error for testing purposes"""

    @staticmethod
    def calc_relative_error(calculated_val, correct_val):
        error = ((correct_val - calculated_val)/correct_val)*100
        return error

    @staticmethod
    def check_same_float(float_1, float_2, digits):
        if round(float_1) == round(float_2):
            return True
