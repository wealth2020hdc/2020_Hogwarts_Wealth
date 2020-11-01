# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.diver = driver

    def register(self):
        self.diver.find_element(By.ID, 'corp_name').send_keys("英皇传媒集团")
        self.diver.find_element(By.ID, 'manager_name').send_keys("刘德华")
        self.diver.find_element(By.ID, 'register_tel').send_keys(18888888888)
        self.diver.find_element(By.ID, 'submit_btn').click()
        assert True
