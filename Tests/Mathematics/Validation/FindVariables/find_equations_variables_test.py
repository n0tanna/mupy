import pytest
from Exceptions.ValidationErrors.VariableValidation.NoVariablesToSolveError import NoVariablesToSolveError
from Mathematics.Validation.FindVariables import FindVariables


def test_find_equations_variables1():
    equation = ['2', 'b', '+', '3', '+', 'd', '=', '2', '+', '4', 'a']
    answer = FindVariables.find_equations_variables(equation)
    assert answer == ['a', 'b', 'd']


def test_find_equations_variables_no_variables_to_solve1():
    equation = ['2', '+', '3', '=', '2', '+', '4']
    with pytest.raises(NoVariablesToSolveError):
        assert FindVariables.find_equations_variables(equation)