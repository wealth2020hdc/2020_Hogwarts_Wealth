# --*-HogWarts-HDC-*--
# --*-UTF-8-*--

# 通讯录界面
from appium.webdriver.common.mobileby import MobileBy

from app.actual2.page.basspage import BassPage
from app.actual2.page.contactdetailpage import ContactDetail
from app.actual2.page.memberInvitemenupage import MemberInviteMenuPage


class AddressListPage(BassPage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_addmember(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()\
        #                          .scrollable(true).instance(0))\
        #                          .scrollIntoView(new UiSelector()\
        #                          .text("添加成员").instance(0));').click()
        self.find_by_scroll("添加成员").click()
        return MemberInviteMenuPage(self.driver)

    def click_delmember(self, value):
        self.find_by_scroll(value).click()
        return ContactDetail(self.driver)
