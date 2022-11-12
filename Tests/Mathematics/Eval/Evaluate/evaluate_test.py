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


def test_evaluate_variables1():
    equation = "((-2)+b)"
    answer = Evaluate.evaluate(equation, "b=5")
    assert answer == 3


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


def test_evaluate_comparison1():
    equation = "2==3"
    answer = Evaluate.evaluate(equation)
    assert answer is False


def test_evaluate_comparison2():
    equation = "2==2"
    answer = Evaluate.evaluate(equation)
    assert answer is True


def test_evaluate_comparison3():
    equation = "2.1==2"
    answer = Evaluate.evaluate(equation)
    assert answer is False


def test_evaluate_comparison4():
    equation = "2.1==2"
    answer = Evaluate.evaluate(equation)
    assert answer is False


def test_evaluate_comparison5():
    equation = "2+4==6"
    answer = Evaluate.evaluate(equation)
    assert answer is True


def test_evaluate_comparison6():
    equation = "2+4==6+4"
    answer = Evaluate.evaluate(equation)
    assert answer is False


def test_evaluate_comparison7():
    equation = "(2+4)^2==36"
    answer = Evaluate.evaluate(equation)
    assert answer is True


def test_evaluate_comparison8():
    equation = "1 != 2"
    answer = Evaluate.evaluate(equation)
    assert answer is True


def test_evaluate_comparison9():
    equation = "-1(-2) != 2"
    answer = Evaluate.evaluate(equation)
    assert answer is False


def test_evaluate_comparison10():
    equation = "(3+4)^(9*4) != 2"
    answer = Evaluate.evaluate(equation)
    assert answer is True


def test_evaluate_comparison11():
    equation = "10+4>(1+1)"
    answer = Evaluate.evaluate(equation)
    assert answer is True


def test_evaluate_comparison13():
    equation = "-(10+4)>2"
    answer = Evaluate.evaluate(equation)
    assert answer is False


def test_evaluate_comparison14():
    equation = "-(10+4)<2"
    answer = Evaluate.evaluate(equation)
    assert answer is True


def test_evaluate_comparison15():
    equation = "-(10+4)<-(2+50*4)"
    answer = Evaluate.evaluate(equation)
    assert answer is False


def test_evaluate_comparison16():
    equation = "-(10+4)<=10"
    answer = Evaluate.evaluate(equation)
    assert answer is True


def test_evaluate_comparison17():
    equation = "10<=10"
    answer = Evaluate.evaluate(equation)
    assert answer is True


def test_evaluate_comparison18():
    equation = "-(10+4)<=-100"
    answer = Evaluate.evaluate(equation)
    assert answer is False


def test_evaluate_comparison19():
    equation = "-(10+4)>=-100"
    answer = Evaluate.evaluate(equation)
    assert answer is True


def test_evaluate_comparison20():
    equation = "100>=100"
    answer = Evaluate.evaluate(equation)
    assert answer is True


def test_evaluate_comparison21():
    equation = "10>=100"
    answer = Evaluate.evaluate(equation)
    assert answer is False


def test_evaluate_variable_comparison1():
    equation = "10b==100"
    answer = Evaluate.evaluate(equation, "b=10")
    assert answer is True


def test_evaluate_variable_comparison2():
    equation = "10b==100"
    answer = Evaluate.evaluate(equation, "b=4")
    assert answer is False


def test_evaluate_variable_comparison3():
    equation = "10b!=100"
    answer = Evaluate.evaluate(equation, "b=4")
    assert answer is True


def test_evaluate_variable_comparison4():
    equation = "10b^a <= 100^a"
    answer = Evaluate.evaluate(equation, "a=10,b=4")
    assert answer is True


def test_evaluate_variable_comparison5():
    equation = "10b^a <= 100"
    answer = Evaluate.evaluate(equation, "a=10,b=4")
    assert answer is False


def test_evaluate_variable_comparison6():
    equation = "10b^a <= 100"
    answer = Evaluate.evaluate(equation, "a=10,b=4")
    assert answer is False


def test_evaluate_variable_comparison7():
    equation = "10 + 2(a + 2) < 100"
    answer = Evaluate.evaluate(equation, "a=10")
    assert answer is True


def test_evaluate_variable_comparison8():
    equation = "10 + 2(a + 2) > 100"
    answer = Evaluate.evaluate(equation, "a=10")
    assert answer is False


def test_evaluate_variable_comparison9():
    equation = "10 + 2(a + 2) > 100"
    answer = Evaluate.evaluate(equation, "a=100")
    assert answer is True
