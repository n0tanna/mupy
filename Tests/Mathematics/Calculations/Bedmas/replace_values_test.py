from mupy.Calculations.Bedmas import Bedmas


def test_replace_values_test_valid1():
    equation = list('2+2')
    character = '+'
    answer = 4
    return_value = Bedmas.replace_values(equation, character, answer)
    assert return_value[0] == 4
