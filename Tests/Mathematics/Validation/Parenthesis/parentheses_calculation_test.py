from Mathematics.Eval.Parentheses import Parentheses


def test_parentheses_addition1():
    equation = ['(', 2, '+', 2, ')']
    first_parenthesis = 0
    last_parenthesis = 4
    answer = Parentheses.parentheses_calculation(equation, first_parenthesis, last_parenthesis)
    assert answer[0] == 4.0


def test_parentheses_addition2():
    equation = ['(', 2, '+', 2, '+', 2, ')']
    first_parenthesis = 0
    last_parenthesis = 6
    answer = Parentheses.parentheses_calculation(equation, first_parenthesis, last_parenthesis)
    assert answer[0] == 6.0


def test_parentheses_subtraction1():
    equation = ['(', 2, '-', 2, ')']
    first_parenthesis = 0
    last_parenthesis = 4
    answer = Parentheses.parentheses_calculation(equation, first_parenthesis, last_parenthesis)
    assert answer[0] == 0.0


def test_parentheses_subtraction2():
    equation = ['(', 2, '-', 2, '-', 2, ')']
    first_parenthesis = 0
    last_parenthesis = 6
    answer = Parentheses.parentheses_calculation(equation, first_parenthesis, last_parenthesis)
    assert answer[0] == -2.0


def test_parentheses_multiplication1():
    equation = ['(', 2, '*', 2, ')']
    first_parenthesis = 0
    last_parenthesis = 4
    answer = Parentheses.parentheses_calculation(equation, first_parenthesis, last_parenthesis)
    assert answer[0] == 4.0


def test_parentheses_multiplication2():
    equation = ['(', 2, '*', 2, '*', 2, ')']
    first_parenthesis = 0
    last_parenthesis = 6
    answer = Parentheses.parentheses_calculation(equation, first_parenthesis, last_parenthesis)
    assert answer[0] == 8.0


def test_parentheses_division1():
    equation = ['(', 2, '/', 2, ')']
    first_parenthesis = 0
    last_parenthesis = 4
    answer = Parentheses.parentheses_calculation(equation, first_parenthesis, last_parenthesis)
    assert answer[0] == 1.0


def test_parentheses_division2():
    equation = ['(', 4, '/', 2, '/', 2, ')']
    first_parenthesis = 0
    last_parenthesis = 6
    answer = Parentheses.parentheses_calculation(equation, first_parenthesis, last_parenthesis)
    assert answer[0] == 1.0


def test_parentheses_exponent1():
    equation = ['(', 2, '^', 2, ')']
    first_parenthesis = 0
    last_parenthesis = 4
    answer = Parentheses.parentheses_calculation(equation, first_parenthesis, last_parenthesis)
    assert answer[0] == 4.0
