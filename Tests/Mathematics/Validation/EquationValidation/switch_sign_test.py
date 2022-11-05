from Mathematics.Validation.EquationValidation import EquationValidation


def test_switch_sign1():
    equation = ['(', '(', '(', '-', 2.0, '*', 'c', '-', 1.0, ')', '/', 5.0, '*', 'a', ')', '+', 4.0, ')']
    switched_equation = EquationValidation.switch_sign(equation)
    assert switched_equation == ['(', '(', '(', -2.0, '*', 'c', '-', 1.0, ')', '/', 5.0, '*', 'a', ')', '+', 4.0, ')']


def test_switch_sign2():
    equation = ['(', '(', '(', '-', 2.0, '*', 'c', '-', 1.0, ')', '/', '-', 5.0, '*', 'a', ')', '+', 4.0, ')', '-', 3.0]
    switched_equation = EquationValidation.switch_sign(equation)
    assert switched_equation == ['(', '(', '(', -2.0, '*', 'c', '-', 1.0, ')', '/', '-', 5.0, '*', 'a', ')', '+', 4.0, ')', '-', 3.0]


def test_switch_sign3():
    equation = ['(', '(', '(', '-', 2.0, '*', 'c', '-', '(', '-', 1.0, ')', ')', '/', '-', 5.0, '*', 'a', ')', '+', 4.0, ')']
    switched_equation = EquationValidation.switch_sign(equation)
    assert switched_equation == ['(', '(', '(', -2.0, '*', 'c', '-', '(', -1.0, ')', ')', '/', '-', 5.0, '*', 'a', ')', '+', 4.0, ')']
