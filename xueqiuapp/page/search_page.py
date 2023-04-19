
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from xueqiuapp.base.xueqiu_app import XueQiuApp


class SearchPage(XueQiuApp):
    __SEARCH_CONTENT = AppiumBy.ID, 'com.xueqiu.android:id/search_input_text'
    __SEARCH_RESULT = AppiumBy.XPATH, '//*[@text="{text}"]'

    # def __init__(self, driver: WebDriver = None):
    #     self.driver = driver

    def input_searchcontent(self,searchkey):
        self.find_and_send(*self.__SEARCH_CONTENT,searchkey)
        # self.driver.find_element(AppiumBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(searchkey)
        return self

    def click_searchresult(self, text):
        self.find_and_click(self.__SEARCH_RESULT[0], self.__SEARCH_RESULT[1].format(text=text))
        # self.driver.find_element(AppiumBy.XPATH,f'//*[@text="{text}"]').click()
        from xueqiuapp.page.search_result_page import SearchResultPage
        return SearchResultPage(self.driver)
