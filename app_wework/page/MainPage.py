
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from app_wework.base.wework_app import WeWorkApp


class MainPage(WeWorkApp):

    _BTN_CONTACT = AppiumBy.XPATH, "//*[@text='通讯录']"

    def goto_address_list(self):
        self.find_and_click(*self._BTN_CONTACT)
        from app_wework.page.AddressListPage import AddressListPage
        return AddressListPage(self.driver)