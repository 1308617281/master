
import time

from appium.webdriver.webdriver import WebDriver

from xueqiuapp.base.black_handle import black_warpper


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @black_warpper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def find_and_gettext(self, by, locator):
        return self.find(by, locator).text

    def screenshot(self, name):
        self.driver.save_screenshot(name)

    def get_time(self):
        t = time.localtime(time.time())
        current_time = time.strftime("%Y-%m-%d-%H-%M-%S", t)
        return current_time
