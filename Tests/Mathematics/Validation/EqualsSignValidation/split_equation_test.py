from mupy.Validation.EqualsSignValidation import EqualsSignValidation


def test_split_equation1():
    equation = ['(', '2', '+', '2', ')', '=', 'a', '+', '4']
    returned_equations = EqualsSignValidation.split_equation(equation, 5)
    assert returned_equations == [['(', '2', '+', '2', ')'], ['a', '+', '4']]


def test_split_equation2():
    equation = ['2', '+', '2', '=', 'a', '+', '4']
    returned_equations = EqualsSignValidation.split_equation(equation, 3)
    assert returned_equations == [['2', '+', '2'], ['a', '+', '4']]
