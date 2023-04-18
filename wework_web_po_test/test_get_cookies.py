import os
import time
import yaml
from selenium import webdriver

#  企业微信的cookie 有互踢机制。
#  获取cookies
class TestCookieLogin:

    def setup_class(self):
        """前置动作"""
        self.driver = webdriver.Chrome()

    def teardown_class(self):
        """后置处理"""
        pass
        # self.driver.quit()

    def test_save_cookies(self):
        """获取cookie"""
        # 1、访问企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 2、直接等待，手工扫码
        time.sleep(15)
        # 3、登录成功后，获取cookie
        cookies = self.driver.get_cookies()
        path = os.path.dirname(os.path.abspath(__file__))
        print(path)
        # 4、保存cookie
        with open('./cookies.yaml', 'w') as f:
            yaml.dump(data=cookies, stream=f)

    def test_add_cookie(self):
        """植入cookie"""

        # 1、访问企业微信首页 CookieDomain
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 2、获取本地 cookies
        with open('./cookies.yaml', 'r') as f:
            cookies = yaml.safe_load(f)
            time.sleep(4)

        # 3、植入cookies
        for ck in cookies:
            self.driver.add_cookie(ck)

        # 4、访问企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")



