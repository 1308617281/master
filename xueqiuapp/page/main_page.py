
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from xueqiuapp.base.xueqiu_app import XueQiuApp


class MainPage(XueQiuApp):
    __SEARCH_BOX = (AppiumBy.ID, 'com.xueqiu.android:id/tv_search')

    # def __init__(self, driver: WebDriver = None):
    #     self.driver = driver

    def click_search(self):
        #主动构造一个异常弹窗resource-id="com.xueqiu.android:id/post_status  //*[contains(@resource-id,"id/post_status")]
        self.find_and_click(AppiumBy.ID,"com.xueqiu.android:id/post_status")
        sleep(1)
        # self.find_and_click(AppiumBy.ID, "com.xueqiu.android:id/iv_close")
        # 点击搜索框
        self.find_and_click(*self.__SEARCH_BOX)
        # self.driver.find_element(AppiumBy.ID, 'com.xueqiu.android:id/tv_search').click()
        from xueqiuapp.page.search_page import SearchPage
        return SearchPage(self.driver)
