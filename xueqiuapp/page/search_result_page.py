
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from xueqiuapp.base.xueqiu_app import XueQiuApp


class SearchResultPage(XueQiuApp):
    __TAB = AppiumBy.XPATH, "//*[@text='股票']"
    __GETTEXT = AppiumBy.XPATH, '//*[@text="BABA"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]'

    # def __init__(self, driver: WebDriver = None):
    #     self.driver = driver

    def goto_stock_tab(self):
        self.find_and_click(*self.__TAB)
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='股票']").click()
        return self

    def get_price(self):
        current_price = self.find_and_gettext(*self.__GETTEXT)
        # current_price = self.driver.find_element(AppiumBy.XPATH,
        #                                          '//*[@text="BABA"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        return float(current_price)
