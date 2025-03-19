from calculations import *
import pytest
class TestCalculations:
    def test_add(self):
        c = Calculations(10,20)
        actual = c.add()
        expected = 30
        assert expected == actual, f"Expect result was {expected} but received {actual}"

    @pytest.mark.parametrize("a, b, expected", [
        (20, 10, 2),
        (10, 20, 0.5)
    ])
    def test_division(self, a, b, expected):
        c = Calculations(a, b)
        actual = c.divi()
        assert expected==actual

