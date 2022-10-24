import pytest
from Mathematics.Validation.VariableEquationValidation import VariableEquationValidation
from Exceptions.ValidationErrors.VariableValidation.NoVariablesToSolveError import NoVariablesToSolveError
from Exceptions.ValidationErrors.VariableValidation.VariableNotFoundError import VariableNotFoundError


def test_find_variable_values1():
    equation = ['(', '2', '+', '2', ')', '=', 'a', '+', '4']
    variables = ['a']
    returned_equations = VariableEquationValidation.find_variable_values(equation, variables)
    assert returned_equations == True


def test_find_variable_values2():
    equation = ['(', 'a', '+', 'b', ')', '=', 'a', '+', '4']
    variables = ['a', 'b']
    returned_equations = VariableEquationValidation.find_variable_values(equation, variables)
    assert returned_equations == True


def test_find_variable_values3():
    equation = ['(', 'a', '+', 'b', ')', '=', 'a', '+', 'c']
    variables = ['a', 'b']
    returned_equations = VariableEquationValidation.find_variable_values(equation, variables)
    assert returned_equations == True


def test_find_variable_values_no_variables1():
    equation = ['(', 'a', '+', 'b', ')', '=', 'a', '+', 'c']
    variables = []
    with pytest.raises(NoVariablesToSolveError):
        assert VariableEquationValidation.find_variable_values(equation, variables)


def test_find_variable_values_variable_not_found():
    equation = ['(', 'a', '+', 'b', ')', '=', 'a', '+', 'c']
    variables = ['d']
    with pytest.raises(VariableNotFoundError):
        assert VariableEquationValidation.find_variable_values(equation, variables)
