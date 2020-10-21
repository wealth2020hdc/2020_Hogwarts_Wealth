# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
"""
    测试计算器（加、减、乘、除）
"""
import pytest

from pythoncode.calculator import Calculator


class TestCalculator:
    @classmethod
    def setup_class(cls):
        cls.calculator = Calculator()
        print("开始执行类中的用例！")

    @classmethod
    def teardown_class(cls):
        print("类中所有用例都执行完毕!")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a, b, c', [[1, 2, 3], [200, 300, 500], [0.1, 0.1, 0.2],
                                         [0, 2, 2], [-1, -2, -3]],
                             ids=['int_small', 'int_big', 'float_num', 'zero_int', 'int_minus'])
    def test_add(self, a, b, c):
        assert c == self.calculator.add(a, b)

    @pytest.mark.parametrize('a, b, c', [[1, 2, -1], [500, 300, 200], [0.1, 0.1, 0],
                                         [0, 2, -2], [-0.1, -0.1, 0]],
                             ids=['int_small', 'int_big', 'float_num', 'zero_int', 'float_minus'])
    def test_sub(self, a, b, c):
        assert c == self.calculator.sub(a, b)

    @pytest.mark.parametrize('a, b, c', [[1, 2, 2], [500, 300, 150000], [0.1, 0.1, 0.01],
                                         [0, 2, 0], [-0.1, -0.2, 0.02]],
                             ids=['int_small', 'int_big', 'float_num', 'zero_int', 'float_minus'])
    def test_mul(self, a, b, c):
        assert c == round(self.calculator.mul(a, b), 2)

    @pytest.mark.parametrize('a, b, c', [[4, 2, 2], [600, 300, 2], [0.4, 0.1, 4],
                                         [2, 0, 0], [-0.1, -2, 0.05]],
                             ids=['int_small', 'int_big', 'float_num', 'zero_int', 'float_minus'])
    def test_div(self, a, b, c):
        try:
            assert c == round(self.calculator.div(a, b), 2)
        except ZeroDivisionError as f:
            print("除数为0")
