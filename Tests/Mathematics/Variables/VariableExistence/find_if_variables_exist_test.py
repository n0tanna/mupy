from Mathematics.Variables.VariableExistence import VariableExistence


def test_find_if_variables_exist1():
    equation = ['2', 'a', '=', '3', '+', 'b']
    variables_exist = VariableExistence.find_if_variables_exist(equation)
    assert variables_exist is True


def test_find_if_variables_exist2():
    equation = ['2', '=', '3', '+', '4']
    variables_exist = VariableExistence.find_if_variables_exist(equation)
    assert variables_exist is False
