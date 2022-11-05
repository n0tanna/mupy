from Mathematics.Eval.Evaluate import Evaluate


def test_evaluate1():
    equation = "1+1"
    answer = Evaluate.evaluate(equation)
    assert answer == 2


def test_evaluate2():
    equation = "(2+1)"
    answer = Evaluate.evaluate(equation)
    assert answer == 3


def test_evaluate3():
    equation = "((2+1)+3)"
    answer = Evaluate.evaluate(equation)
    assert answer == 6


def test_evaluate4():
    equation = "((2+1)+(3+2))"
    answer = Evaluate.evaluate(equation)
    assert answer == 8


def test_evaluate5():
    equation = "(( 2 + 1 ) + ( 3 + 2 ))"
    answer = Evaluate.evaluate(equation)
    assert answer == 8


def test_evaluate6():
    equation = "2(4)"
    answer = Evaluate.evaluate(equation)
    assert answer == 8


def test_evaluate7():
    equation = "(2+1)+(3+2)"
    answer = Evaluate.evaluate(equation)
    assert answer == 8


def test_evaluate8():
    equation = "(2+1)^2"
    answer = Evaluate.evaluate(equation)
    assert answer == 9


def test_evaluate9():
    equation = "(2+1)^2"
    answer = Evaluate.evaluate(equation)
    assert answer == 9


def test_evaluate10():
    equation = "(2+2)/2"
    answer = Evaluate.evaluate(equation)
    assert answer == 2


def test_evaluate11():
    equation = "((-2))"
    answer = Evaluate.evaluate(equation)
    assert answer == -2.0


def test_evaluate_decimals1():
    equation = "(2+1.1)+(3+2.5)"
    answer = Evaluate.evaluate(equation)
    assert answer == 8.6


def test_evaluate_decimals2():
    equation = "(2 + 1.1) + (3 + 2.5)"
    answer = Evaluate.evaluate(equation)
    assert answer == 8.6


def test_evaluate_decimals3():
    equation = "1/3"
    answer = Evaluate.evaluate(equation)
    assert answer == 0.3333333333333333

