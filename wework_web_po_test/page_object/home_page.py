
from selenium.webdriver.common.by import By

from wework_web_po_test.utils.log_util import logger
from wework_web_po_test.page_object.addcontact_page import AddContactPage
from wework_web_po_test.page_object.base_page import BasePage


class HomePage(BasePage):
    _TEXT_ADDMEMBER = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")
    def click_add_member(self):
        """点击添加成员"""
        logger.info("点击添加成员按钮")
        self.find_and_click(*self._TEXT_ADDMEMBER)
        return AddContactPage(self.driver)