
import yaml

from wework_web_po_test.test_cases import TESTCASE_PATH
from wework_web_po_test.utils.log_util import logger
from wework_web_po_test.page_object.base_page import BasePage
from wework_web_po_test.page_object.home_page import HomePage


class LoginPage(BasePage):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame"
    def login(self):
        """登录"""
        logger.info("登录")
        # 2、获取本地的cookie
        with open(TESTCASE_PATH+"/../data/cookies.yaml", "r") as f:
            cookies = yaml.safe_load(f)
        # 3、植入cookie
        for ck in cookies:
            self.driver.add_cookie(ck)
        # 4、访问企业微信首页
        self.driver.get(self._BASE_URL)
        return HomePage(self.driver)