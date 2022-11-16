from src.Mathematics.Calculations.Simplify import Simplify


def test_edit_values_dictionary1():
    variable = [5.0, '*', 'b']
    variables = {"b": 2.0, "c": 1.0}
    coefficients = [3.0]
    response = Simplify.edit_values_dictionary(variable, variables, coefficients)

    assert response == [[3.0, 5.0], {"b": 3.0, "c": 1.0}]


def test_edit_values_dictionary2():
    variable = [5.0, '*', 'b', '*', 'c', '^', 60.0]
    variables = {"b": 2.0, "c": 1.0}
    coefficients = [3.0]
    response = Simplify.edit_values_dictionary(variable, variables, coefficients)

    assert response == [[3.0, 5.0], {"b": 3.0, "c": 61.0}]
