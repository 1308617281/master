import os
import time

import allure

from wework_web_po_test.utils.log_util import logger


def ui_exception_record(func):
    def run(*args, **kwargs):
        self = args[0]
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # 这里添加所有的异常情况处理
            # 日志
            logger.warning("执行过程中发生异常")
            # 截图
            timestamp = int(time.time())
            image_path = f"./images/"
            image_file = image_path + f"image_{timestamp}.PNG"
            page_source_path = f"./page_source/"
            page_source_file =page_source_path + f"{timestamp}_page_source.html"
            # page_source
            if not os.path.exists(page_source_path):
                os.makedirs(page_source_path)
            with open(page_source_file, "w", encoding="u8") as f:
                f.write(self.driver.page_source)
            if not os.path.exists(image_path):
                os.makedirs(image_path)
            self.driver.save_screenshot(image_file)
            allure.attach.file(image_file, name="image", attachment_type=allure.attachment_type.PNG)
            # allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.HTML)
            allure.attach.file(page_source_file, name="page_source", attachment_type=allure.attachment_type.TEXT)
            raise e
    return run