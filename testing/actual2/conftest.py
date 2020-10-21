# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import pytest


@pytest.fixture(scope='module', autouse=True)
def warn1():
    print("模块里的测试用例开始执行！")
    yield
    print("模块里的测试用例执行完毕！")


@pytest.fixture(autouse=True)
def warn2():
    print("当前测试用例开始执行！")
    yield
    print("当前测试用例执行完毕！")

# @pytest.fixture()
# def login():
#     # setup 操作
#     print("登录")
#     # return 操作
#     yield ['tom', 123456]
#     # teardown 操作
#     print("退出")
#
#
# @pytest.fixture(autouse=False, scope="module")
# def search():
#     print("搜索")
#     yield
#     print("搜索完毕")
