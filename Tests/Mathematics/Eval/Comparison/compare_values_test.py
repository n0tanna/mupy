from src.Mathematics.Eval.Comparison import Comparison
from src.Mathematics.Enums.ComparisonOperator import ComparisonIdentifiers


def test_compare_values1():
    left_number = 1.2
    right_number = 3
    comparison_type = ComparisonIdentifiers.EQUAL
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is False


def test_compare_values2():
    left_number = 3
    right_number = 3
    comparison_type = ComparisonIdentifiers.EQUAL
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is True


def test_compare_values3():
    left_number = 3
    right_number = 0
    comparison_type = ComparisonIdentifiers.GREATER_THAN
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is True


def test_compare_values4():
    left_number = 3
    right_number = 5
    comparison_type = ComparisonIdentifiers.GREATER_THAN
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is False


def test_compare_values5():
    left_number = 2
    right_number = 5
    comparison_type = ComparisonIdentifiers.LESS_THAN
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is True


def test_compare_values6():
    left_number = 7
    right_number = 5
    comparison_type = ComparisonIdentifiers.LESS_THAN
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is False


def test_compare_values7():
    left_number = 7
    right_number = 5
    comparison_type = ComparisonIdentifiers.NOT_EQUAL
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is True


def test_compare_values8():
    left_number = 5
    right_number = 5
    comparison_type = ComparisonIdentifiers.NOT_EQUAL
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is False


def test_compare_values9():
    left_number = 7
    right_number = 5
    comparison_type = ComparisonIdentifiers.GREATER_THAN_OR_EQUAL
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is True


def test_compare_values10():
    left_number = 5
    right_number = 5
    comparison_type = ComparisonIdentifiers.GREATER_THAN_OR_EQUAL
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is True


def test_compare_values11():
    left_number = 5
    right_number = 5
    comparison_type = ComparisonIdentifiers.LESS_THAN_OR_EQUAL
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is True


def test_compare_values12():
    left_number = 1
    right_number = 5
    comparison_type = ComparisonIdentifiers.LESS_THAN_OR_EQUAL
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is True


def test_compare_values13():
    left_number = 1.3
    right_number = 1.3
    comparison_type = ComparisonIdentifiers.EQUAL
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is True


def test_compare_values14():
    left_number = 1.3
    right_number = 2
    comparison_type = ComparisonIdentifiers.EQUAL
    result = Comparison.compare_values(left_number, right_number, comparison_type)
    assert result is False
