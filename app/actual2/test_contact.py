# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
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
        # caps["dontStopAppOnReset"] = "true"
        caps["skipDeviceInitialization"] = "true"
        caps["skipServerInstallation"] = "true"

        # caps["settings[waitForIdleTimeout]"] = 0

        # 关键 localhost:4723 本机ip:server端口
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()

    def test_contact(self):
        name = "周杰伦103"
        gender = "男"
        phonenumber = "16600000103"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(
            name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[contains(@text, '男')]").click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '男')]").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '女')]").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机') and @class='android.widget.TextView']/..//android.widget.EditText").send_keys(
            phonenumber)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # sleep(2)
        # print(self.driver.page_source)
        result = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        print(result)
        assert "添加成功" == result

    def teardown_class(self):
        self.driver.quit()
