# --*-HogWarts-HDC-*--
# --*-UTF-8-*--

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.web_actual2.PO_DEMO02.page.addmenber_page import AddMenberPage
from web.web_actual2.PO_DEMO02.page.bass_page import BassPage


class MainPage(BassPage):
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=options)

    def goto_addmenberpage(self):
        # 进入通讯录页面
        self.find(By.ID, 'menu_contacts').click()

        # 添加成员
        # self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')

        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, 'username')
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)

        return AddMenberPage(self.driver)
