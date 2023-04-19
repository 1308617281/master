
import logging
import os
import traceback

import allure
from appium.webdriver.common.appiumby import AppiumBy

black_list = [(AppiumBy.ID, "com.xueqiu.android:id/iv_close")]


def black_warpper(fun):
    def inner(*args, **kwargs):
        from xueqiuapp.base.base_page import BasePage
        basepage: BasePage = args[0]
        try:
            logging.info(f"开始查找元素：{args[2]}")
            return fun(*args, **kwargs)
        except Exception as e:
            print("出现异常，进行异常处理")
            logging.warning('未找到元素，处理异常')
            time = basepage.get_time()
            tmp_name = time + ".png"
            logging.info("当前保存图片的路径>>>" + os.path.dirname(__file__))
            tmp_path = os.path.join(os.path.dirname(__file__), "..", "images", tmp_name)
            basepage.screenshot(tmp_path)
            allure.attach.file(tmp_path, name="查找截图", attachment_type=allure.attachment_type.PNG)
            for black in black_list:
                logging.info(f'点击黑名单弹框')
                eles = basepage.driver.find_elements(*black)
                if len(eles) > 0:
                    eles[0].click()
                    print(eles[0])
                    return fun(*args, **kwargs)
            logging.error(f"未找到元素,异常信息=========={e}")
            logging.error(f"命令行的错误输出trackback.format_exc()======{traceback.format_exc()}")
            raise e

    return inner
