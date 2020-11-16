# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from selenium.webdriver.common.by import By

from UI.fram2.bass_page import BassPage
from UI.fram2.search_page import SearchPage


class MarketPage(BassPage):
    def goto_search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self.parse_yaml("./market.yaml", "goto_search")
        return SearchPage(self.driver)
