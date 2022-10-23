from Mathematics.Calculations.Reciprocal import Reciprocal


def test_get_reciprocal1():
    answer = Reciprocal.get_reciprocal(2)
    assert answer == 0.5
