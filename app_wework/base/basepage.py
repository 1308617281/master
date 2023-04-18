
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException


class BasePage:
    IMPLICITLY_TIME = 10

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        # 查找元素
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        # 查找元素并点击
        self.find(by, locator).click()

    def find_and_sendkeys(self, text, by, locator):
        # 查找元素并输入
        self.find(by, locator).send_keys(text)

    def implicitly_wait(self, time=1):
        # 设置隐式等待的时间
        self.driver.implicitly_wait(time)

    def swipe_find(self, text, max_mum=5):
        # 滑动查找元素
        self.driver.implicitly_wait(1)
        for num in range(max_mum):
            try:
                self.find(AppiumBy.XPATH, f"//*[@text='{text}']").click()
                self.driver.implicitly_wait(self.IMPLICITLY_TIME)
                return True
            except Exception as e:
                print("未找到元素")
                size = self.driver.get_window_size()
                width = size.get("width")
                height = size.get("height")

                startx = width / 2
                starty = height / 2

                endx = startx
                endy = height * 0.2

                duration = 2000
                self.driver.swipe(startx, starty, endx, endy, duration)

            if num == max_mum - 1:
                self.driver.implicitly_wait(self.IMPLICITLY_TIME)
                raise NoSuchElementException(f"找了{num}次，未找到{text[1]}")

    def get_toast_tips(self):
        # 获取toast提示语
        return self.find(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text