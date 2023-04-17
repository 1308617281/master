
from selenium.webdriver.common.by import By

from master.test_litemail.page_objects.base_page import BasePage
from master.test_litemail.utils.utils import logger


class HomePage(BasePage):
    """系统首页：进入商品类目"""
    __SHOP_MANAGE = (By.XPATH, "//*[text()='商场管理']")
    __SHOP_PRODUCT = (By.XPATH, "//*[text()='商品类目']")

    def go_to_category(self):
        logger.info("系统首页：进入商品类目")
        # 点击菜单“商场管理”
        self.do_find(self.__SHOP_MANAGE).click()
        # 点击菜单“商品类目”
        self.do_find(self.__SHOP_PRODUCT).click()
        # ==》类目列表页面

        from master.test_litemail.page_objects.categroy_list_page import CategoryListPage
        return CategoryListPage(self.driver)
