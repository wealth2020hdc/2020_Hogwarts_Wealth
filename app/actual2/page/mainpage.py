# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
"""
    获取页面的布局结构命令：
    adb shell "uiautomator dump && cat /sdcard/window_dump.xml"
    获取app当前页面的名字
    adb shell dumpsys window|grep mCurrentFocus
    adb shell dumpsys window|fndstr mCurrentFocus
"""
from appium.webdriver.common.mobileby import MobileBy

from app.actual2.page.addresslistpage import AddressListPage
from app.actual2.page.basspage import BassPage


class MainPage(BassPage):
    # def __init__(self, driver):
    #     self.driver = driver

    def go_message(self):
        """
        进入到消息也
        :return:
        """
        pass

    def goto_address(self):
        """
        进入到通讯录
        :return:
        """
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)
