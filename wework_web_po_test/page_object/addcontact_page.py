
from selenium.webdriver.common.by import By

from wework_web_po_test.utils.log_util import logger
from wework_web_po_test.page_object.base_page import BasePage
from wework_web_po_test.page_object.contactlist_page import ContactListPage


class AddContactPage(BasePage):
    _INPUT_USERNAME = By.ID, "username"
    _INPUT_ACCID = By.ID, "memberAdd_acctid"
    _INPUT_PHONE = By.ID, "memberAdd_phone"
    _BNT_SAVE = (By.CSS_SELECTOR, ".js_btn_save")

    def edit_contact(self,username, accid, mobile):
        """填写成员信息"""
        # 3. 填写成员信息
        logger.info("填写成员信息")
        # 3.1 输入用户名
        self.find_and_send(username, self._INPUT_USERNAME)
        # 3.2 输入acctid
        self.find_and_send(accid, self._INPUT_ACCID)
        # 3.3 输入手机号
        self.find_and_send(mobile, self._INPUT_PHONE)
        # 3.4 点击保存
        self.find_and_click(self._BNT_SAVE)
        return  ContactListPage(self.driver)