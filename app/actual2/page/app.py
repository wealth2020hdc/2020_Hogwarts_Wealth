# --*-HogWarts-HDC-*--
# --*-UTF-8-*--

"""
    存放app相关的一些操作
    比如： 启动应用；重启应用；停止应用；进入首页
"""
import yaml
from appium import webdriver

from app.actual2.page.basspage import BassPage
from app.actual2.page.mainpage import MainPage

with open('../../datas/caps.yml') as f:
    myconfig = yaml.safe_load(f)
    caps = myconfig["desirecaps"]
    ip = myconfig["server"]["ip"]
    port = myconfig["server"]["port"]


class App(BassPage):
    def start(self):
        if self.driver == None:
            # 定义一个字典
            # caps = {}
            # caps["platformName"] = "Android"
            # caps["deviceName"] = "hogwarts"
            # caps["appPackage"] = "com.tencent.wework"
            # caps["appActivity"] = ".launch.LaunchSplashActivity"
            # noReset保留缓存信息， 登录
            # caps["noReset"] = "True"
            # 不停止应用，直接运行测试用例
            # caps["dontStopAppOnReset"] = "true"
            # caps["skipDeviceInitialization"] = "true"
            # caps["skipServerInstallation"] = "true"

            # caps["settings[waitForIdleTimeout]"] = 0

            # 关键 localhost:4723 本机ip:server端口
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def go_to_main(self) -> MainPage:
        return MainPage(self.driver)
