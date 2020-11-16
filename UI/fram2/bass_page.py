# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from UI.fram2.hand_black import handle_black


class BassPage:
    black_list01 = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        """
        初始化应用
        获取包名和页面名字：先执行如下命令，再启动相应的APP
        Mac/Linux:
        adb logcat |grep -i activitymanager
        Windows:
        adb logcat |findstr /i activitymanager
        启动元素定位工具：Uiautomatorviewer
        """
        if driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "True"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        """
        查找元素
        :return:
        """
        if locator is None:
            # 如果传的是一个元组
            result = self.driver.find_element(*by)
        else:
            # 如果传的是两个参数
            result = self.driver.find_element(by, locator)
        return result

        # try:
        #     if locator is None:
        #         # 如果传的是一个元组
        #         result = self.driver.find_element(*by)
        #     else:
        #         # 如果传的是两个参数
        #         result = self.driver.find_element(by, locator)
        #     self._error_num = 0
        #     return result
        # except Exception as e:
        #     if self._error_num > self._max_num:
        #         raise e
        #     self._error_num += 1
        #     for black_ele in self._black_list:
        #         print(black_ele)
        #         print("查找黑名单元素")
        #         print(*black_ele)
        #         ele = self.driver.find_elements(*black_ele)
        #         if len(ele) > 0:
        #             ele[0].click()
        #             print("点击操作")
        #             return self.find(by, locator)
        #     raise e
        # if locator is None:
        #     # 如果传的是一个元组
        #     result = self.driver.find_element(*by)
        # else:
        #     # 如果传的是两个参数
        #     result = self.driver.find_element(by, locator)
        # return result

    def parse_yaml(self, path, func_name):
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        self.parse(data[func_name])

    def parse(self, steps):
        for step in steps:
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()
            elif 'send' == step['action']:
                self.find(step['by'], step['locator']).send_keys(step['content'])
