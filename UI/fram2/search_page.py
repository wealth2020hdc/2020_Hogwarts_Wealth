# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from selenium.webdriver.common.by import By

from UI.fram2.bass_page import BassPage


class SearchPage(BassPage):
    def search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("阿里巴巴")
        self.parse_yaml("./search.yml", "search")
