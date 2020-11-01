# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from selenium import webdriver
from selenium.webdriver.common.by import By

from web.web_actual2.PO_DEMO1.login_page import LoginPage
from web.web_actual2.PO_DEMO1.register_page import RegisterPage


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    # 进入登录页
    def goto_login(self):
        #  点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        #  返回LoginPage
        return LoginPage(self.driver)

    # 进入注册页
    def goto_register(self):
        #  点击注册
        self.driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        # 返回 Register
        return RegisterPage(self.driver)
