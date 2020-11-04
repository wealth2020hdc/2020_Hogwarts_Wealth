# --*-HogWarts-HDC-*--
# --*-UTF-8-*--


# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:

    def setup_class(self):
        # 定义一个字典
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # noReset保留缓存信息， 登录
        caps["noReset"] = "True"
        # 不停止应用，直接运行测试用例
        caps["dontStopAppOnReset"] = "true"
        caps["skipDeviceInitialization"] = "true"
        caps["skipServerInstallation"] = "true"

        # caps["settings[waitForIdleTimeout]"] = 0

        # 关键 localhost:4723 本机ip:server端口
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    # def test_case(self):
    #     el1 = self.driver.find_element_by_xpath(
    #         "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
    #     el1.click()
    #     el2 = self.driver.find_element_by_xpath(
    #         "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[11]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
    #     el2.click()
    def teardown(self):
        self.driver.back()

    def test_one(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()

    def test_two(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        self.driver.update_settings({"waitForIdleTimeout": 0})
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # sleep(2)
        # assert "外出打卡成功" in self.driver.page_source
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)

    def teardown_class(self):
        self.driver.quit()
