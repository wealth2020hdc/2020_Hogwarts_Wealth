# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from appium.webdriver.common.mobileby import MobileBy

# from app.actual2.page.contactaddpage import ContactAddPage
from app.actual2.page.basspage import BassPage


class MemberInviteMenuPage(BassPage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_member_menual(self):
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from app.actual2.page.contactaddpage import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.get_toast_text()
        return result
