
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from master.test_litemail.page_objects.base_page import BasePage
from master.test_litemail.utils.utils import logger
from master.test_litemail.utils.web_util import click_exception


class CategoryCreatePage(BasePage):
    """创建类目页面：创建类目"""
    __INPUT_PRODUCT_NAME = (By.CSS_SELECTOR, ".el-input__inner")
    __BTN_OK = (By.CSS_SELECTOR, ".dialog-footer .el-button--primary")

    def create_category(self, categroy_name):
        logger.info('创建类目页面：创建类目')
        # 输入“类目名称”
        self.do_send_keys(categroy_name, self.__INPUT_PRODUCT_NAME)
        # 点击“确定”按钮
        WebDriverWait(self.driver, 10).until(click_exception(*self.__BTN_OK))
        # ==》类目列表页面

        from master.test_litemail.page_objects.categroy_list_page import CategoryListPage
        return CategoryListPage(self.driver)
