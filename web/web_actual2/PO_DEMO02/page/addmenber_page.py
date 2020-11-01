# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from web.web_actual2.PO_DEMO02.page.bass_page import BassPage


class AddMenberPage(BassPage):

    def addmenber(self, username, acctid, phonenumber):
        self.find(By.ID, 'username').send_keys(username)
        self.find(By.ID, 'memberAdd_acctid').send_keys(acctid)
        self.find(By.XPATH, '//*/input[@id="memberAdd_phone"]').send_keys(phonenumber)
        self.find(By.XPATH, '//*/form[@class="js_member_editor_form"]/div[1]/a[2]').click()
        checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(checkbox)
        return True

    def getnumber(self, value):
        # 验证添加联系人成功
        totallist = []
        while True:
            contaclist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = []
            for element in contaclist:
                titlelist.append(element.get_attribute("title"))
            totallist = totallist + titlelist
            result: str = self.find(By.XPATH, '//*[@class="ww_pageNav_info_text"]').text
            num, total = result.split('/', 1)
            # if int(num) != int(total):
            #     self.find(By.XPATH, '//*[@class="ww_commonImg ww_commonImg_PageNavArrowRightNormal"]').click()
            # else:
            #     break

            if value in totallist:
                return True
            self.find(By.XPATH, '//*[@class="ww_commonImg ww_commonImg_PageNavArrowRightNormal"]').click()

            if int(num) == int(total):
                return False

        # return totallist
