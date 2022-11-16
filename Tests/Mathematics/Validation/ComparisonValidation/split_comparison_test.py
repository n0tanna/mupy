import pytest

from src.Mathematics.Validation.ComparisonValidation import ComparisonValidation
from src.Mathematics.Enums.ComparisonOperator import ComparisonIdentifiers
from src.Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError


def test_split_comparison1():
    comparison = ['2', '^', '3', '>', '4', '3']
    validated_comparison = ComparisonValidation.split_comparison(comparison)
    assert validated_comparison == {'left_equation': ['2', '^', '3'], 'right_equation': ['4', '3'], 'comparison_type':
        ComparisonIdentifiers.GREATER_THAN}


def test_split_comparison2():
    comparison = ['2', '^', '3', '<', '4', '3']
    validated_comparison = ComparisonValidation.split_comparison(comparison)
    assert validated_comparison == {'left_equation': ['2', '^', '3'], 'right_equation': ['4', '3'], 'comparison_type':
        ComparisonIdentifiers.LESS_THAN}


def test_split_comparison3():
    comparison = ['2', '^', '3', '=', '=', '4', '3']
    validated_comparison = ComparisonValidation.split_comparison(comparison)
    assert validated_comparison == {'left_equation': ['2', '^', '3'], 'right_equation': ['4', '3'], 'comparison_type':
        ComparisonIdentifiers.EQUAL}


# def test_split_comparison4():
#     comparison = ['2', '^', '3', '=', '=', '=', '4', '3']
#     validated_comparison = ComparisonValidation.split_comparison(comparison)
#     assert validated_comparison == {'left_equation': ['2', '^', '3'], 'right_equation': ['4', '3'], 'comparison_type':
#         ComparisonIdentifiers.IDENTICAL}


def test_split_comparison5():
    comparison = ['2', '^', '3', '!', '=', '4', '3']
    validated_comparison = ComparisonValidation.split_comparison(comparison)
    assert validated_comparison == {'left_equation': ['2', '^', '3'], 'right_equation': ['4', '3'], 'comparison_type':
        ComparisonIdentifiers.NOT_EQUAL}


# def test_split_comparison6():
#     comparison = ['2', '^', '3', '!', '=', '=', '4', '3']
#     validated_comparison = ComparisonValidation.split_comparison(comparison)
#     assert validated_comparison == {'left_equation': ['2', '^', '3'], 'right_equation': ['4', '3'], 'comparison_type':
#         ComparisonIdentifiers.NOT_IDENTICAL}


def test_split_comparison7():
    comparison = ['2', '^', '3', '<', '=', '4', '3']
    validated_comparison = ComparisonValidation.split_comparison(comparison)
    assert validated_comparison == {'left_equation': ['2', '^', '3'], 'right_equation': ['4', '3'], 'comparison_type':
        ComparisonIdentifiers.LESS_THAN_OR_EQUAL}


def test_split_comparison8():
    comparison = ['2', '^', '3', '>', '=', '4', '3']
    validated_comparison = ComparisonValidation.split_comparison(comparison)
    assert validated_comparison == {'left_equation': ['2', '^', '3'], 'right_equation': ['4', '3'], 'comparison_type':
        ComparisonIdentifiers.GREATER_THAN_OR_EQUAL}


def test_split_comparison9():
    comparison = ['2', '^', '3', '>', '=', '4', 'b']
    validated_comparison = ComparisonValidation.split_comparison(comparison)
    assert validated_comparison == {'left_equation': ['2', '^', '3'], 'right_equation': ['4', 'b'], 'comparison_type':
        ComparisonIdentifiers.GREATER_THAN_OR_EQUAL}


def test_split_comparison_incorrect_equal_sign_usage1():
    comparison = ['2', '^', '3', '=', '=', '=', '=', '4', '3']
    with pytest.raises(IncorrectEqualsSignUsageError):
        assert ComparisonValidation.split_comparison(comparison)


def test_split_comparison_incorrect_equal_sign_usage2():
    comparison = ['=', '^', '3', '=', '=', '4', '3']
    with pytest.raises(IncorrectEqualsSignUsageError):
        assert ComparisonValidation.split_comparison(comparison)