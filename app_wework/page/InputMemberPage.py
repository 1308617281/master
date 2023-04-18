
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from app_wework.base.wework_app import WeWorkApp


class InputMemberPage(WeWorkApp):
    _INPUT_NAME = AppiumBy.XPATH, "//*[@text='姓名']/../*[@text='必填']"
    _INPUT_PHONE = AppiumBy.XPATH, "//*[@text='手机']/..//*[@text='必填']"
    _SAVE = AppiumBy.XPATH, "//*[@text='保存']"

    def input_contact(self, name, phone):
        self.find_and_sendkeys(name, *self._INPUT_NAME)
        self.find_and_sendkeys(phone, *self._INPUT_PHONE)
        self.find_and_click(*self._SAVE)
        from app_wework.page.AddMemberPage import AddMemberPage
        return AddMemberPage(self.driver)
