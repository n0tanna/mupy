import pytest
from Mathematics.Calculations.Bedmas import Bedmas
from Exceptions.ValidationErrors.MathematicsValidation.IncorrectExponentFormatError import IncorrectExponentFormatError
from Exceptions.MathematicErrors.DivisionByZeroError import DivisionByZeroError


def test_bedmas_calculation_addition1():
    equation = [1, '+', 2, '+', 3]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 6.0


def test_bedmas_calculation_addition2():
    equation = [1, '+', 2, '+', 3, '+', 1.5]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 7.5


def test_bedmas_calculation_addition3():
    equation = [1, '+', 2, '+', 3, '+', -1]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 5.0


def test_bedmas_calculation_subtraction1():
    equation = [1, '-', 2, '-', 3]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == -4.0


def test_bedmas_calculation_subtraction2():
    equation = [1, '-', 2, '-', 3, '-', 1.5]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == -5.5


def test_bedmas_calculation_subtraction3():
    equation = [1, '-', 2, '-', 3, '-', -1]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == -3.0


def test_bedmas_calculation_multiplication1():
    equation = [1, '*', 2, '*', 3]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 6.0


def test_bedmas_calculation_multiplication2():
    equation = [1, '*', 2, '*', 3, '*', 1.5]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 9.0


def test_bedmas_calculation_multiplication3():
    equation = [1, '*', 2, '*', 3, '*', -1]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == -6.0


def test_bedmas_calculation_division1():
    equation = [6, '/', 3]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 2.0


def test_bedmas_calculation_division2():
    equation = [5, '/', 2.5]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 2.0


def test_bedmas_calculation_division3():
    equation = [1, '/', 0.5]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 2.0


def test_bedmas_calculation_division4():
    equation = [10, '/', 2, '/', 5]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 1.0


def test_bedmas_calculation_exponent1():
    equation = [10, '^', 2]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 100.0


def test_bedmas_calculation_exponent2():
    equation = [2, '^', -2]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 0.25


def test_bedmas_calculation_exponent3():
    equation = [-2, '^', 2]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == -4.0


def test_bedmas_calculation_mixed_operators1():
    equation = [3, '+', -2, '^', 2]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == -1.0


def test_bedmas_calculation_mixed_operators2():
    equation = [2, '*', 3, '+', -2, '^', 2]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 2.0


def test_bedmas_calculation_mixed_operators3():
    equation = [2, '^', 3, '+', -2, '^', 2]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == 4.0


def test_bedmas_calculation_mixed_operators4():
    equation = [6, '/', 3, '+', -2, '-', 2]
    answer = Bedmas.bedmas_calculation(equation)
    assert answer == -2.0


def test_bedmas_calculation_division_by_zero1():
    equation = [6, '/', 0, '+', -2, '-', 2]
    with pytest.raises(DivisionByZeroError):
        assert Bedmas.bedmas_calculation(equation)


def test_bedmas_calculation_division_by_zero2():
    equation = [6, '/', 0]
    with pytest.raises(DivisionByZeroError):
        assert Bedmas.bedmas_calculation(equation)


def test_bedmas_calculation_incorrect_exponent_format1():
    equation = [6, '^', 1.3]
    with pytest.raises(IncorrectExponentFormatError):
        assert Bedmas.bedmas_calculation(equation)


def test_bedmas_calculation_incorrect_exponent_format2():
    equation = [6, '^', 0.2]
    with pytest.raises(IncorrectExponentFormatError):
        assert Bedmas.bedmas_calculation(equation)


def test_bedmas_calculation_incorrect_exponent_format3():
    equation = [3.0, '+', 4.0, '^', 0.453453]
    with pytest.raises(IncorrectExponentFormatError):
        assert Bedmas.bedmas_calculation(equation)
