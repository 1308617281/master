
from appium import webdriver

from app_wework.base.basepage import BasePage


class WeWorkApp(BasePage):

    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6"
        caps["deviceName"] = "qw"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(self.IMPLICITLY_TIME)
        return self

    def restart(self):
        self.driver.close()
        # 已经起用launch_app方法
        # self.driver.launch_app()
        self.driver.activate_app("com.tencent.wework")
        return self

    def stop(self):
        self.driver.quit()

    def goto_mian(self):
        from app_wework.page.MainPage import MainPage
        return MainPage(self.driver)
