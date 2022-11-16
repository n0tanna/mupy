from Mathematics.Calculations.ParenthesesCalculation import ParenthesesCalculation


def test_calculate_while_parentheses_exist_one_set1():
    equation = ['(', 2, '+', 2, ')']
    answer = ParenthesesCalculation.calculate_while_parentheses_exist(equation)
    assert answer == 4.0


def test_calculate_while_parentheses_exist_two_sets1():
    equation = ['(', '(', 2, '+', 2, ')', '-', 4, ')']
    answer = ParenthesesCalculation.calculate_while_parentheses_exist(equation)
    assert answer == 0.0


def test_calculate_while_parentheses_exist_three_sets1():
    equation = ['(', '(', 2, '+', 2, ')', '+', '(', 8, '-', 4, ')', ')']
    answer = ParenthesesCalculation.calculate_while_parentheses_exist(equation)
    assert answer == 8.0


def test_calculate_while_parentheses_exist_three_sets2():
    equation = ['(', '(', '(', 2, '+', 2, ')', '-', 4, ')', '+', 10, ')']
    answer = ParenthesesCalculation.calculate_while_parentheses_exist(equation)
    assert answer == 10.0


def test_calculate_while_parentheses_exist_three_sets3():
    equation = ['(', 2, '+', '(', 2, '+', '(', 2, '-', 4, ')', ')', ')']
    answer = ParenthesesCalculation.calculate_while_parentheses_exist(equation)
    assert answer == 2.0


def test_calculate_while_parentheses_exist_two_different_sets1():
    equation = ['(', 2, '+', 2, ')', '+', '(', 8, '-', 4, ')']
    answer = ParenthesesCalculation.calculate_while_parentheses_exist(equation)
    assert answer == 8.0

