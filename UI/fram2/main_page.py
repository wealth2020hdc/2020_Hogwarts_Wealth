# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import yaml
from selenium.webdriver.common.by import By

from UI.fram2.bass_page import BassPage
from UI.fram2.market_page import MarketPage


class MainPage(BassPage):
    def goto_market(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # # self.find((By.XPATH, "//*[@resource-id=‘com.xueqiu.android:id/iv_close’]")).click()
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        # with open("./main.yml", encoding="utf-8") as f:
        #     data = yaml.safe_load(f)
        # steps = data['goto_mark']
        # for step in steps:
        #     if 'click' == step['action']:
        #         self.find(step['by'], step['locator']).click()
        self.parse_yaml("./main.yml", "goto_mark")
        return MarketPage(self.driver)
