from Mathematics.Calculations.Simplify import Simplify
from Mathematics.Calculations.Expand import Expand


def test_simplify_multiplication1():
    equation = [2.0, '*', 'b', '^', 3.0, '+', 3.0, '*', 'b', '*', 'c',
                '*', 2.0, '*', 'b', '+', 2.0, '*', 'b']
    variables = []
    index = 0

    while index < len(equation):
        variable = Expand.group_variables(equation, index)
        variables.append(variable)
        index += len(variable["variable"]) + 1

    simplified = Simplify.simplify_multiplication(variables)

    assert simplified == [[{'variable': [2.0, '*', 'b', '^', 3.0]}, {'operator': '+'}],
                          [{'variable': [6.0, '*', 'b', '^', 2, '*', 'c']}, {'operator': '+'}],
                          [{'variable': [2.0, '*', 'b']}, {'operator': ''}]]


def test_simplify_multiplication2():
    equation = [2.0, '*', 'b', '^', 3.0, '+', 3.0, '*', 'b', '*', 'c']
    variables = []
    index = 0

    while index < len(equation):
        variable = Expand.group_variables(equation, index)
        variables.append(variable)
        index += len(variable["variable"]) + 1

    simplified = Simplify.simplify_multiplication(variables)

    assert simplified == [[{'variable': [2.0, '*', 'b', '^', 3.0]}, {'operator': '+'}],
                          [{'variable': [3.0, '*', 'b', '*', 'c']}, {'operator': ''}]]


def test_simplify_multiplication3():
    equation = [2.0, '*', 'b', '^', 3.0, '*', 3.0, '*', 'b', '*', 'c', '*', 2.0, 'b', '^', 5.0]
    variables = []
    index = 0

    while index < len(equation):
        variable = Expand.group_variables(equation, index)
        variables.append(variable)
        index += len(variable["variable"]) + 1

    simplified = Simplify.simplify_multiplication(variables)

    assert simplified == [[{'variable': [12.0, '*', 'b', '^', 5.0, '*', 'c']}, {'operator': ''}]]


