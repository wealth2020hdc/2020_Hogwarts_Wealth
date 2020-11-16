# --*-HogWarts-HDC-*--
# --*-UTF-8-*--

# 1.动态导入
import importlib

import hello


def test_tmp():
    a = importlib.import_module("re")
    print(a.search(".*", "abcd"))


def test_tmp1():
    b = importlib.import_module('hello')
    print(b.a())


# 2.反射
def test_tmp2():
    c = importlib.import_module('hello')
    getattr(c, 'a')()


# 导入特定包
def test_tmp3():
    tmp = "a.b.c.d".split(".")
    print(tmp)


# save原理
def test_tmp4():
    globals()["a"] = 101
    print(globals()["a"])
    print(hasattr(hello, "a"))


# 把string当做命令执行
def test_tmp5():
    print(eval("1+1"))
