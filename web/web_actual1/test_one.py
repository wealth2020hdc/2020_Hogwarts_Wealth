# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import time

from selenium import webdriver


def test_one():
    driver = webdriver.Chrome()
    driver.get("https://baidu.com/")
    a = driver.find_element_by_xpath('//a[@href="http://map.baidu.com"]').text
    print(a)
