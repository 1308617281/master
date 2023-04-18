
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wework_web_po_test.utils.error_handle import ui_exception_record
from wework_web_po_test.utils.log_util import logger


class BasePage:
    _BASE_URL = ""

    def __init__(self, driver: WebDriver = None):
        if driver:
            # 复用driver
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL)

    @ui_exception_record
    def find(self, by, locator=None):
        """查找元素"""
        logger.info(f"查找元素：by>{by}, locator>{locator}")
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def find_and_click(self, by, locator=None):
        """查找到之后完成点击"""
        logger.info(f"查找到之后点击")
        self.find(by, locator).click()

    def find_and_send(self, text, by, locator=None):
        """查找到之后完成输入"""
        logger.info(f"查找到之后完成输入：{text}")
        self.find(by, locator).send_keys(text)

    def quit(self):
        logger.info("退出 quit()")
        self.driver.quit()

    def wait_for_visible(self, locator):
        logger.info("显式等待等到元素可见")
        WebDriverWait(self.driver, 10, 2). \
            until(expected_conditions.visibility_of_element_located(locator))

    def get_text(self, by, locator):
        logger.info("获取元素的文本信息")
        return self.find(by, locator).text
