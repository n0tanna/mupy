from src.Mathematics.Calculations.Simplify import Simplify


def test_build_values_dictionary1():
    variable = [2.0, '*', 'b', '^', 2.0]
    response = Simplify.build_values_dictionary(variable)
    assert response == [[2.0], {"b": 2.0}]


def test_build_values_dictionary2():
    variable = [2.0, '*', 'b', '*', 'b', '^', 2.0]
    response = Simplify.build_values_dictionary(variable)
    assert response == [[2.0], {"b": 3.0}]


def test_build_values_dictionary3():
    variable = [2.0, '*', 'c', '*', 'b', '^', 2.0]
    response = Simplify.build_values_dictionary(variable)
    assert response == [[2.0], {"b": 2.0, "c": 1.0}]
