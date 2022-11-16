from mupy.Eval.Classification import Classification
from mupy.Enums.EquationIdentifers import EquationIdentifiers
from mupy.Exceptions.ValidationErrors.IncorrectCharacterError import IncorrectCharacterError
from mupy.Exceptions.ValidationErrors.VariableValidation.VariableNotFoundError import VariableNotFoundError
import pytest


def test_determine_variables1():
    equation = ['2', '>', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, [])
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables2():
    equation = ['2', '+', '4', '^', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.EQUATION, [])
    assert equation_type == EquationIdentifiers.EQUATION


def test_determine_variables3():
    equation = ['2', '-', '6', '.', '3', '=', '3', 'b']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.EQUATION, [])
    assert equation_type == EquationIdentifiers.VARIABLES


def test_determine_variables4():
    equation = ['2', '-', '6', '.', '3', '=', '3', '+', '1', '0']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.EQUATION, [])
    assert equation_type == EquationIdentifiers.EQUATION


def test_determine_variables5():
    equation = ['2', '<', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, [])
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables6():
    equation = ['2', '=', '=', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, [])
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables7():
    equation = ['2', '=', '=', '=', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, [])
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables8():
    equation = ['2', '!', '=', '=', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, [])
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables9():
    equation = ['2', '>', '=', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, [])
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables10():
    equation = ['2', 'c', '-', '6', '.', '3', '=', '3', 'b']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.EQUATION, [])
    assert equation_type == EquationIdentifiers.VARIABLES


def test_determine_variables11():
    equation = ['2', '>', 'a']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, ['n'])
    assert equation_type == EquationIdentifiers.COMPARISON_VARIABLES


def test_determine_variables_incorrect_character1():
    equation = ['2', '>', '=', '3', 'a']
    with pytest.raises(IncorrectCharacterError):
        Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, [])


def test_determine_variables_incorrect_character2():
    equation = ['2', '=', '=', '3', 'a']
    with pytest.raises(IncorrectCharacterError):
        Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, [])


def test_determine_variables_incorrect_character3():
    equation = ['2', '=', '=', '=', 'a']
    with pytest.raises(IncorrectCharacterError):
        Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, [])


def test_determine_variables_incorrect_character4():
    equation = ['2', '>', 'a']
    with pytest.raises(IncorrectCharacterError):
        Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, [])


def test_determine_variables_variable_not_found1():
    equation = ['2', '>', '2']
    with pytest.raises(VariableNotFoundError):
        Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, ['b'])


def test_determine_variables_variable_not_found2():
    equation = ['2', '=', '2', '+', '4']
    with pytest.raises(VariableNotFoundError):
        Classification.determine_variables(equation, EquationIdentifiers.COMPARISON, ['b'])

