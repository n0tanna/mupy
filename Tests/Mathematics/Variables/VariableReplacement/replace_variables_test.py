import pytest
from Exceptions.ValidationErrors.VariableValidation.VariableNotFoundError import VariableNotFoundError
from Mathematics.Variables.VariableReplacement import VariableReplacement
from Mathematics.Enums.EquationIdentifers import EquationIdentifiers
from Exceptions.ValidationErrors.VariableValidation.NoVariableValueError import NoVariableValueError
from Exceptions.ValidationErrors.IncorrectCharacterError import IncorrectCharacterError


def test_replace_variables1():
    variables = {'a': ['2', '+', '3'], 'b': ['3', '.', '0']}
    equation = ['a', '=', 'b']
    replaced_variables = VariableReplacement.replace_variables(equation, variables,
                                                               EquationIdentifiers.COMPARISON_VARIABLES)
    assert replaced_variables == ['(', '2', '+', '3', ')', '=', '(', '3', '.', '0', ')']


def test_replace_variables2():
    variables = {'a': ['2', '*', '3'], 'b': ['3', '.', '0']}
    equation = ['2', 'a', '=', '3', '+', 'b']
    replaced_variables = VariableReplacement.replace_variables(equation, variables,
                                                               EquationIdentifiers.COMPARISON_VARIABLES)
    assert replaced_variables == ['2', '(', '2', '*', '3', ')', '=', '3', '+', '(', '3', '.', '0', ')']


def test_replace_variables3():
    variables = {'a': '', 'b': ['3', '.', '0']}
    equation = ['2', 'a', '=', '3', '+', 'b']
    replaced_variables = VariableReplacement.replace_variables(equation, variables,
                                                               EquationIdentifiers.VARIABLES)
    assert replaced_variables == ['2', 'a', '=', '3', '+', '(', '3', '.', '0', ')']


def test_replace_variables4():
    variables = {'a': '', 'b': ['3', '.', '0']}
    equation = ['2', 'a', 'b', '=', '3', '+', 'b']
    replaced_variables = VariableReplacement.replace_variables(equation, variables,
                                                               EquationIdentifiers.VARIABLES)
    assert replaced_variables == ['2', 'a', '(', '3', '.', '0', ')', '=', '3', '+', '(', '3', '.', '0', ')']


def test_replace_variables5():
    variables = {'a': '', 'b': ['3', '.', '0']}
    equation = ['2', 'a', 'b', '=', '3', '+', 'b', '+', 'c']
    replaced_variables = VariableReplacement.replace_variables(equation, variables,
                                                               EquationIdentifiers.VARIABLES)
    assert replaced_variables == [['2', 'a', '(', '3', '.', '0', ')', '=', '3', '+', '(', '3', '.', '0', ')', '+', 'c'],
                                  {'a': '', 'b': ['3', '.', '0'], 'c': ''}]


def test_replace_variables6():
    variables = {'a': '3', 'b': ''}
    equation = ['2', 'a', 'b', '=', '3', '+', 'b', '+', 'c']
    replaced_variables = VariableReplacement.replace_variables(equation, variables,
                                                               EquationIdentifiers.VARIABLES)
    assert replaced_variables == [['2', '(', '3', ')', '*', 'b', '=', '3', '+', 'b', '+', 'c'],
                                  {'a': '3', 'b': '', 'c': ''}]


def test_replace_variables_variable_not_found1():
    variables = {'b': ['2', '+', '4'], 'a': '', 'c': ''}
    equation = [2.0, '+', 'd']
    with pytest.raises(VariableNotFoundError):
        assert VariableReplacement.replace_variables(equation, variables, EquationIdentifiers.COMPARISON_VARIABLES)


def test_replace_variables_variable_not_found2():
    variables = {'a': ''}
    equation = [2.0, '+', 'b']
    with pytest.raises(VariableNotFoundError):
        assert VariableReplacement.replace_variables(equation, variables, EquationIdentifiers.COMPARISON_VARIABLES)


def test_replace_variables_variable_not_found3():
    variables = {'a': ''}
    equation = [2.0, '+', '=', 'b']
    with pytest.raises(VariableNotFoundError):
        assert VariableReplacement.replace_variables(equation, variables, EquationIdentifiers.COMPARISON_VARIABLES)


def test_replace_variables_variable_not_found4():
    variables = {'a': '2', 'c': '3'}
    equation = [2.0, '+', '=', 'a']
    with pytest.raises(VariableNotFoundError):
        assert VariableReplacement.replace_variables(equation, variables, EquationIdentifiers.COMPARISON_VARIABLES)


def test_replace_variables_no_variable_value1():
    variables = {'a': ['2', '+', '4'], 'b': ''}
    equation = ['b', '=', 'a']
    with pytest.raises(NoVariableValueError):
        assert VariableReplacement.replace_variables(equation, variables, EquationIdentifiers.COMPARISON_VARIABLES)


def test_replace_variables_no_variable_value2():
    variables = {'a': '', 'b': ['3', '.', '0']}
    equation = ['a', '=', 'b']
    with pytest.raises(NoVariableValueError):
        assert VariableReplacement.replace_variables(equation, variables, EquationIdentifiers.COMPARISON_VARIABLES)
