import yaml
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from faker import Faker


from selenium.common import NoSuchElementException


class TestWeWork:
    IMPLICITLY_TIME = 10
    _ADD_MUM = AppiumBy.XPATH, "//*[@text='添加成员']"

    def swipe_find(self, *text, max_mum=5):
        self.driver.implicitly_wait(1)
        for num in range(max_mum):
            try:
                self.driver.find_element(*text).click()
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

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6"
        caps["deviceName"] = "qw"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(self.IMPLICITLY_TIME)
        # self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        #         # 设置隐式等待，动态等到元素出现
        #         self.driver.implicitly_wait(self.IMPLICITLY_WAIT)

    def setup_class(self):
        self.faker = Faker("zh_CN")

    def teardown(self):
        self.driver.quit()

    def test_addconnect(self):
        name = self.faker.name()
        phone_number = self.faker.phone_number()

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='添加成员']").click()
        self.swipe_find(*(self._ADD_MUM))
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动输入添加']").click()

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='姓名']/../*[@text='必填']").send_keys(name)
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手机']/..//*[@text='必填']").send_keys(phone_number)
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='保存']").click()

        with open('./page_source.yaml', "w", encoding="u8") as f:
            yaml.safe_dump(self.driver.page_source, f)
        print(self.driver.page_source)
        toast_tips = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text

        print(toast_tips)
        assert toast_tips == "添加成功"
