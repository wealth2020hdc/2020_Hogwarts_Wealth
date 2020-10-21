# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import pytest


@pytest.mark.login
def test_login1():
    print("登录1")


@pytest.mark.login
def test_login2():
    print("登录2")


@pytest.mark.search
def test_search1():
    print("搜索1")


@pytest.mark.search
def test_search2():
    print("搜索2")
