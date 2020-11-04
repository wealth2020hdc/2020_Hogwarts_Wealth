# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.actual2.page.basspage import BassPage


class ContactEdit(BassPage):
    def click_delmember(self):
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='删除成员']"))
        # self.wait_for_find(MobileBy.XPATH, "//android.widget.TextView[@text='删除成员']")
        self.find(MobileBy.XPATH, "//android.widget.TextView[@text='删除成员']").click()
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='确定']"))
        # self.wait_for_find(MobileBy.XPATH, "//android.widget.TextView[@text='确定']")
        self.find(MobileBy.XPATH, "//android.widget.TextView[@text='确定']").click()
        return True
