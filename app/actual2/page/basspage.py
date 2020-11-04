# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
"""
    基类模块：主要用于初始化driver
"""
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BassPage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

    def get_toast_text(self):
        return self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text

    # def wait_for_find(self, locator, timeout=10):
    #     return  WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(locator))
    #
    # def wait_for_click(self, locator, timeout=10):
    #     element: WebElement = WebDriverWait(self.driver, timeout).until(
    #         expected_conditions.element_to_be_clickable(locator))
    #     return element
