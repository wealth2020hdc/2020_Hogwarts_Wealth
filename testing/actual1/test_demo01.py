# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from pythoncode.calculator import Calculator


class TestCalculator:
    def test_add(self):
        cal = Calculator()
        assert 5 == cal.add(2, 3)
