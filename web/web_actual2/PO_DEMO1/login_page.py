# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.web_actual2.PO_DEMO1.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 扫码
    def scsn(self):
        pass

    # 进入到注册也
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return RegisterPage(self.driver)
