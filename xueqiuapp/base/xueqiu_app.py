from appium import webdriver

from xueqiuapp.base.base_page import BasePage


class XueQiuApp(BasePage):

    def start(self):

        if self.driver == None:
            print('driver=None')
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['deviceName'] = 'qw'
            # mac: adb logcat ActivityManager:I | grep "cmp"
            # win: adb logcat ActivityManager:I | findstr "cmp"
            desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
            desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['noReset'] = 'true'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            # 直接启用app
            print('复用driver')
            self.driver.launch_app()  # 即将被弃用

        return self  # 调用当前同类里的方法（即想调用MainPage的方法）
        from xueqiuapp.page.main_page import MainPage
        return MainPage(self.driver)

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        from xueqiuapp.page.main_page import MainPage
        return MainPage(self.driver)
