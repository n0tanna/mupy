import pytest

from src.Mathematics.Validation.VariableInputParser import VariableInputParser
from src.Exceptions.ValidationErrors.VariableValidation.IncorrectVariableFormat import IncorrectVariableFormat
from src.Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError


def test_variable_input_parser1():
    variables = "a=2,b=5+3"
    validated_variables = VariableInputParser.variable_input_parser(variables)
    assert validated_variables == {'a': '2', 'b': '5+3'}


def test_variable_input_parser2():
    variables = "a,b=5+3"
    validated_variables = VariableInputParser.variable_input_parser(variables)
    assert validated_variables == {'a': '', 'b': '5+3'}


def test_variable_input_parser3():
    variables = "a,b,c,d=(4+5)^2"
    validated_variables = VariableInputParser.variable_input_parser(variables)
    assert validated_variables == {'a': '', 'b': '', 'c': '', 'd': '(4+5)^2'}


def test_variable_input_parser_incorrect_equals_sign_usage1():
    variables = "a==,b=3"
    with pytest.raises(IncorrectEqualsSignUsageError):
        VariableInputParser.variable_input_parser(variables)


def test_variable_input_parser_incorrect_equals_sign_usage2():
    variables = "a=3,b=3,c=="
    with pytest.raises(IncorrectEqualsSignUsageError):
        VariableInputParser.variable_input_parser(variables)


def test_variable_input_parser_incorrect_variable_format1():
    variables = "aa,b=3"
    with pytest.raises(IncorrectVariableFormat):
        VariableInputParser.variable_input_parser(variables)


def test_variable_input_parser_incorrect_variable_format2():
    variables = "a,b=3,cc"
    with pytest.raises(IncorrectVariableFormat):
        VariableInputParser.variable_input_parser(variables)


def test_variable_input_parser_incorrect_variable_format3():
    variables = "a,=3,c=3"
    with pytest.raises(IncorrectVariableFormat):
        VariableInputParser.variable_input_parser(variables)


