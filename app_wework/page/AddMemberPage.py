
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from app_wework.base.wework_app import WeWorkApp


class AddMemberPage(WeWorkApp):
    _NOAUTO_INPUT= AppiumBy.XPATH, "//*[@text='手动输入添加']"

    def goto_input_member(self):
        self.find_and_click(*self._NOAUTO_INPUT)
        from app_wework.page.InputMemberPage import InputMemberPage
        return InputMemberPage(self.driver)

    def get_tips(self):
        return self.get_toast_tips()
