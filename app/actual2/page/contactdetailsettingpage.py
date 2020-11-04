# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.actual2.page.basspage import BassPage
from app.actual2.page.contacteditpage import ContactEdit


class ContactDetailSetting(BassPage):
    def click_edit(self):
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='编辑成员']"))
        # self.wait_for_find(MobileBy.XPATH, "//android.widget.TextView[@text='编辑成员']")
        self.find(MobileBy.XPATH, "//android.widget.TextView[@text='编辑成员']").click()
        return ContactEdit(self.driver)
