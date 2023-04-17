# _*_ coding: utf-8 _*_
# @time     : 2023/3/7 8:33
# @Auther   : xiao

from selenium.webdriver.common.by import By

from master.test_litemail.page_objects.base_page import BasePage
from master.test_litemail.utils.utils import logger


class LoginPage(BasePage):
    """登录页面：用户登录"""
    _BASE_URL = "http://litemall.hogwarts.ceshiren.com/"
    __INPUT_USERNAME = (By.NAME, "username")
    __INPUT_PASSWORD = (By.NAME, "password")
    __BTN = (By.CSS_SELECTOR, ".el-button--primary")

    def login(self):
        logger.info("登录页面：用户登录")
        # 输入“用户名”
        self.do_send_keys("manage", self.__INPUT_USERNAME)
        # 输入“密码”
        self.do_send_keys("manage123", self.__INPUT_PASSWORD)
        # 点击“登录”按钮
        self.do_find(self.__BTN).click()
        # ==》首页

        from master.test_litemail.page_objects.home_page import HomePage
        return HomePage(self.driver)
