# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.actual2.page.basspage import BassPage
from app.actual2.page.contactdetailsettingpage import ContactDetailSetting


class ContactDetail(BassPage):
    def click_seting(self):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.ID, "com.tencent.wework:id/hxm"))
        # locator = (MobileBy.ID, "com.tencent.wework:id/hxm")
        # self.wait_for_find(*locator)
        # result = self.wait_for_click(*locator)
        # result.click()
        self.find(MobileBy.ID, "com.tencent.wework:id/hxm").click()
        return ContactDetailSetting(self.driver)
