from selenium.webdriver.common.by import By

from master.test_litemail.page_objects.base_page import BasePage
from master.test_litemail.utils.utils import logger


class CategoryListPage(BasePage):
    """类目列表页面：点击添加"""
    __ADD = (By.XPATH, "//*[text()='添加']")
    __MSG_ADD = (By.XPATH, '//p[contains(text(),"创建成功")]')
    __MSG_DELETE = (By.XPATH, '//p[contains(text(),"删除成功")]')

    def click_add(self):
        logger.info('类目列表页面：点击添加')
        # 点击“添加”按钮
        self.do_find(self.__ADD).click()
        # ==》创建类目页面

        from master.test_litemail.page_objects.categroy_create_page import CategoryCreatePage
        return CategoryCreatePage(self.driver)

    """类目列表页面：获取添加操作结果"""

    def get_oprate_result(self):
        logger.info("类目列表页面：获取添加操作结果")
        # 获取冒泡消息文本
        # element = WebDriverWait(self.driver, 10).until(
        #     expected_conditions.visibility_of_element_located((By.XPATH, '//p[contains(text(),"创建成功")]')))
        element = self.wait_element(self.__MSG_ADD)
        msg = element.text
        logger.info(f'冒泡消息为{msg}')
        # ==》返回消息文本
        return msg

    """类目列表页面：进行删除操作"""

    def delete_category(self, category_name):
        logger.info('类目列表页面：进行删除操作')
        # self.driver.find_element(By.XPATH,
        #                                  "//*[text()='删除shop']/../..//*[text()='删除']").click()
        self.do_find(By.XPATH, f'//*[text()="{category_name}"]/../..//*[text()="删除"]').click()
        return CategoryListPage(self.driver)

    def get_delete_result(self):
        logger.info('类目列表页面：获取删除操作结果')
        # 获取冒泡消息文本
        element = self.wait_element(self.__MSG_DELETE)
        msg = element.text
        logger.info(f'冒泡消息为{msg}')
        # ==》返回消息文本
        return msg
