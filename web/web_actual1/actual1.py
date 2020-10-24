# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFileUpload:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_file_upload(self):
        self.driver.get(
            "https://work.weixin.qq.com/wework_admin/loginpage_wx?redirect_uri=https://work.weixin.qq.com/wework_admin/frame#index")
        db = shelve.open("cookies")
        cookies = db["cookie"]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@class="index_service_cnt js_service_list"]/a[2]').click()
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@class="ww_fileImporter_fileContainer_uploadInputMask"]').send_keys(
            "D:/tongxunlu.xlsx")
        sleep(3)
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        print(filename)
        assert filename == "tongxunlu.xlsx"
        sleep(3)
