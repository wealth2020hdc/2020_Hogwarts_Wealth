# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from pythoncode.calculator import Calculator


def setup_module():
    print("setup_module在模块中第一个执行")


def teardown_module():
    print("setup_module在模块中最后一个执行")


def setup_function():
    print("setup_function在类外每个用例执行之前执行")


def teardown_function():
    print("teardown_function在类外每个用例执行执行")


def test_add():
    cal = Calculator()
    assert 6 == cal.add(3, 3)


class TestDemo:
    def setup_class(self):
        print("setup_class在类中第一个执行")

    def teardown_class(self):
        print("teardown_class在类中最后执行")

    def setup(self):
        print("setup在类中每个用例执行之前执行")

    def teardown(self):
        print("teardown在类中每个用例执行之后执行")

    def test_add(self):
        cal = Calculator()
        assert 5 == cal.add(2, 3)


class TestDemo1:
    def setup_class(self):
        print("setup_class1在类中第一个执行")

    def teardown_class(self):
        print("teardown_class1在类中最后执行")

    def setup(self):
        print("setup在类中每个用例执行之前执行")

    def teardown(self):
        print("teardown在类中每个用例执行之后执行")

    def test_add(self):
        cal = Calculator()
        assert 5 == cal.add(2, 3)


def test_add1():
    cal = Calculator()
    assert 6 == cal.add(3, 3)
