# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import yaml

from pythoncode.calculator import Calculator

cal = Calculator()


def test_add_steps():
    addstepsfile = "./steps/add_step.yml"
    calculator = cal
    a = 1
    b = 2
    c = 3
    get_steps(addstepsfile, calculator, a, b, c)
    # assert 2 == calculator.add(1, 1)
    # assert 3 == calculator.add1(1, 2)


def get_steps(addstepsfile, calculator, a, b, c):
    with open(addstepsfile) as f:
        steps = yaml.safe_load(f)

    for step in steps:
        if "add" == step:
            print("add")
            result = calculator.add(a, b)
        elif "add1" == step:
            print("add1")
            result = calculator.add1(a, b)

        assert c == result
