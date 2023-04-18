
import json

import requests

from test_litemall_intermediate.utils.log_utils import logger


class BaseApi:

    def __init__(self, base_url, role=None):
        self.base_url = base_url
        # 获取对应的角色信息
        if role:
            self.role = role

    def __set_token(self, request_infos):
        admin_url = "admin/auth/login"
        admin_data = {"username": "admin123", "password": "admin123", "code": ""}
        admin_r = requests.request("post", self.base_url + admin_url, json=admin_data)
        self.token = {"X-Litemall-Admin-Token": admin_r.json()["data"]["token"]}
        client_url = "wx/auth/login"
        client_data = {"username": "user123", "password": "user123"}
        client_r = requests.request("post", self.base_url + client_url, json=client_data)
        self.client_token = {"X-Litemall-Token": client_r.json()["data"]["token"]}

        # 如果是admin，那么就塞入admin的token
        # 如果是其他，那么就塞入 其他的token
        if self.role == "admin":
            self.final_token = self.token
        else:
            self.final_token = self.client_token
        # 获取headers， 如果请求本身有头信息，那么就把token信息更新进去
        if request_infos.get("headers"):
            request_infos["headers"].update(self.final_token)
        else:
            request_infos["headers"] = self.final_token
        return request_infos

    def send(self, method, url, **kwargs):
        kwargs = self.__set_token(kwargs)
        r = requests.request(method, self.base_url + url, **kwargs)
        logger.debug(f"{url}接口的响应为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r.json()
