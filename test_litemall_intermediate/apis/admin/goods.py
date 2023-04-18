
from test_litemall_intermediate.apis.base_api import BaseApi
from test_litemall_intermediate.domain.goods_domain import GoodsDomain


class Goods(BaseApi, GoodsDomain):

    def create(self, goods_data):
        url = "admin/goods/create"
        # 问题： token 是 手动复制进去的，一旦发生变化，还需要再次修改
        # 解决方案： token 需要自动完成获取，并且赋值
        # r = self.send("post", url, json=goods_data, headers={"X-Litemall-Admin-Token": self.token})
        # 没有添加头信息
        r = self.send("post", url, json=goods_data, headers={"teacher": "ad"})
        return r

    def list(self, goods_name, order="desc", sort="add_time"):
        # 自己编写的接口对应的方法，应该和接口本身的逻辑相关
        goods_list_url = "admin/goods/list"
        goods_data = {
            "name": goods_name,
            "order": order,
            "sort": sort
        }
        r = self.send("get", goods_list_url, params=goods_data,)

        return r

    def detail(self, goods_id):
        goods_detail_url = "admin/goods/detail"
        r = self.send("get", goods_detail_url,
                      params={"id": goods_id},)
        return r
        # product_id = r.json()["data"]["products"][0]["id"]

    def delete(self, goods_id):
        url = "admin/goods/delete"
        r = self.send("post", url, json={"id": goods_id})
        return r

