from master.test_litemail.utils.utils import logger


def click_exception(by, element, max_attempts=5):
    def _inner(driver):
        # 多次点击按钮
        actul_attempts = 0  # 实际点击次数
        while actul_attempts < max_attempts:
            # 进行点击操作
            actul_attempts += 1
            try:
                # 如果点击过程报错，则直接执行 except 逻辑，并切继续循环
                # 没有报错，则直接return 循环结束
                driver.find_element(by, element).click()
                return True
            except Exception:
                logger.debug("点击的时候出现了一次异常")
        # 当实际点击次数大于最大点击次数时，结束循环并抛出异常
        raise Exception("超出了最大点击次数")

    # return _inner() 错误写法
    return _inner
