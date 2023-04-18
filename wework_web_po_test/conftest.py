import os.path

import allure
import pytest
import yaml
import sys

from test_cases import TESTCASE_PATH
from wework_web_po_test.utils.log_util import logger


# 解决用例描述中中文乱码的问题
def pytest_collection_modifyitems(
        session, config, items
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    fail_case_info = []
    # 错误类型
    error_type = None
    # 错误信息
    error_msg = None
    # 错误完整信息
    error_longrepr = None
    # 如果用例执行不通过
    if report.outcome != "passed":
        # 如果运行时有相应的错误日志则捕获日志，赋值到一个变量中
        if call.excinfo:
            error_type = call.excinfo.typename
            error_msg = call.excinfo.value.msg
            error_longrepr = str(out._result.longrepr)

        case_info = {
            "nodeid": report.nodeid,
            "result": report.outcome,
            "type": error_type,
            "msg": error_msg,
            "longrepr": error_longrepr
        }
        fail_case_info.append(case_info)
        # 用例信息写入 yaml 文件
        with open(TESTCASE_PATH+'./fail_record/fail_cases_info.yaml', 'a', encoding='utf-8') as f:
            yaml.dump(fail_case_info, f)

        logger.error(f'错误类型 =>> {error_type}，\n'
                     f'错误信息 =>> {error_msg}，\n'
                     f'错误详情 =>> {error_longrepr} \n')
