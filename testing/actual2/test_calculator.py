# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
"""
    测试计算器（加、减、乘、除）
"""
import pytest
import yaml

from pythoncode.calculator import Calculator
from testing.actual2.get_datas import get_datas


@pytest.fixture(scope="class")
def get_cal():
    print("开始执行类中的用例！")
    calculator = Calculator()
    yield calculator
    print("类中所有用例都执行完毕!")


class TestCalculator:
    # def setup(self):
    #     print("开始计算")
    #
    # def teardown(self):
    #     print("计算结束")

    @pytest.mark.run(order=1)
    @pytest.mark.dependency()
    @pytest.mark.parametrize('a, b, c', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_cal, a, b, c):
        assert c == get_cal.add(a, b)
        print("add")

    @pytest.mark.run(order=3)
    @pytest.mark.dependency()
    @pytest.mark.parametrize('a, b, c', get_datas()[2],
                             ids=get_datas()[3])
    def test_sub(self, get_cal, a, b, c):
        assert c == get_cal.sub(a, b)
        print("sub")

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depens=["test_add"])
    @pytest.mark.parametrize('a, b, c', get_datas()[4],
                             ids=get_datas()[5])
    def test_mul(self, get_cal, a, b, c):
        assert c == round(get_cal.mul(a, b), 2)
        print("mul")

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["test_sub"])
    @pytest.mark.parametrize('a, b, c', get_datas()[6],
                             ids=get_datas()[7])
    def test_div(self, get_cal, a, b, c):
        try:
            assert c == round(get_cal.div(a, b), 2)
            print("div")
        except ZeroDivisionError as f:
            print("除数为0")
