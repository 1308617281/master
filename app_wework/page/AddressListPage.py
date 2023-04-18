
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from app_wework.base.wework_app import WeWorkApp


class AddressListPage(WeWorkApp):
    # _ADD_MEMBER = AppiumBy.XPATH, "//*[@text='添加成员']"
    _ADD_MEMBER = '添加成员'

    def goto_add_member(self):
        self.swipe_find(self._ADD_MEMBER)
        # self.find_and_click(*self._ADD_MEMBER)
        from app_wework.page.AddMemberPage import AddMemberPage
        return AddMemberPage(self.driver)
