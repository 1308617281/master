
from selenium.webdriver.common.by import By

from wework_web_po_test.utils.log_util import logger
from wework_web_po_test.page_object.base_page import BasePage


class ContactListPage(BasePage):
    """通讯录页面"""
    _TIPS_LOC = (By.ID, "js_tips")
    _TEXT_USERNAME = By.XPATH, "//span[text()='{name}']/../..//input"
    _BNT_DELETE = By.XPATH, "//*[text()='删除']"
    _BNT_CONFIRM_DELETE = By.XPATH, "//*[@d_ck='submit_hr_helper']"
    def get_tips(self):
        """获取提示文本"""
        # 4. 断言结果
        # 等到可见，再去获取结果文字
        self.wait_for_visible(self._TIPS_LOC)
        tips_value = self.driver.find_element(*self._TIPS_LOC).text
        return tips_value

    def del_contact(self,username):
        """删除成员"""
        logger.info(f"===>> {self._TEXT_USERNAME[0],self._TEXT_USERNAME[1].format(name=username)}")
        self.find_and_click(self._TEXT_USERNAME[0],self._TEXT_USERNAME[1].format(name=username))
        self.find_and_click(self._BNT_DELETE)
        self.find_and_click(self._BNT_CONFIRM_DELETE)
