from Mathematics.Calculations.ExpandSimplify import ExpandSimplify


def test_group_values1():
    equation = [2.0, '*', 'b', '^', 3.0, '+', 3.0, '*', 'b']
    variables = []
    index = 0
    equation_holder = equation

    while index < len(equation):
        variable = ExpandSimplify.group_variables(equation_holder, index)
        variables.append(variable)
        index += len(variable["variable"]) + 1

    assert variables == [{'variable': [2.0, '*', 'b', '^', 3.0], 'operator': '+'},
                         {'variable': [3.0, '*', 'b'], 'operator': ''}]


def test_group_values2():
    equation = [2.0, '*', 'b', '^', 3.0, '+', 3.0, '*', 'b', '-', 'a']
    variables = []
    index = 0
    equation_holder = equation

    while index < len(equation):
        variable = ExpandSimplify.group_variables(equation_holder, index)
        variables.append(variable)
        index += len(variable["variable"]) + 1

    assert variables == [{'variable': [2.0, '*', 'b', '^', 3.0], 'operator': '+'},
                         {'variable': [3.0, '*', 'b'], 'operator': '-'},
                         {'variable': ['a'], 'operator': ''}]


def test_group_values3():
    equation = [2.0, '*', 'b', '^', 3.0, '+', 3.0, '*', 'b', '*', 2.0, '*', 'a']
    variables = []
    index = 0
    equation_holder = equation

    while index < len(equation):
        variable = ExpandSimplify.group_variables(equation_holder, index)
        variables.append(variable)
        index += len(variable["variable"]) + 1

    assert variables == [{'variable': [2.0, '*', 'b', '^', 3.0], 'operator': '+'},
                         {'variable': [3.0, '*', 'b'], 'operator': '*'},
                         {'variable': [2.0, '*', 'a'], 'operator': ''}]


def test_group_values4():
    equation = [2.0, '+', 3.0, '+', 3.0]
    variables = []
    index = 0
    equation_holder = equation

    while index < len(equation):
        variable = ExpandSimplify.group_variables(equation_holder, index)
        variables.append(variable)
        index += len(variable["variable"]) + 1

    assert variables == [{'variable': [2.0], 'operator': '+'},
                         {'variable': [3.0], 'operator': '+'},
                         {'variable': [3.0], 'operator': ''}]


