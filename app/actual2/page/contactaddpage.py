# --*-HogWarts-HDC-*--
# --*-UTF-8-*--

"""
    编辑联系人页面
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

# from app.actual2.page.memberInvitemenupage import MemberInviteMenuPage
from app.actual2.page.basspage import BassPage


class ContactAddPage(BassPage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_contact(self, name, gender, phonenumber):
        self.find(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(
            name)
        self.find(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[contains(@text, '男')]").click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
        if gender == "男":
            self.find(MobileBy.XPATH, "//*[contains(@text, '男')]").click()
        else:
            self.find(MobileBy.XPATH, "//*[contains(@text, '女')]").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机') and @class='android.widget.TextView']/..//android.widget.EditText").send_keys(
            phonenumber)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from app.actual2.page.memberInvitemenupage import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
