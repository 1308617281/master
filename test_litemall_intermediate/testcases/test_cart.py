
import pytest

from test_litemall_intermediate.apis.admin.goods import Goods
from test_litemall_intermediate.apis.wx.cart import Cart
from test_litemall_intermediate.utils.log_utils import logger


class TestCart():
    """
    框架优化：
    1. 先把接口和用例步骤写出来，接口的实现，暂时先设置为空
    2. 先初步的实现接口，保证可用
    """
    def setup_class(self):
        self.goods = Goods("http://litemall.hogwarts.ceshiren.com/", "admin")
        self.cart = Cart("http://litemall.hogwarts.ceshiren.com/", "client")

    # def teardown(self):
    #     self.goods.delete(self.goods_id)

    @pytest.mark.parametrize("goods_name", ['qw22','qw33'])
    def test_add_cart(self, goods_name):
        """
        1. 添加购物车的测试
            上架商品接口
            获取商品列表
            获取商品详情
            添加购物车
        :return:
        """
        goods_data = {
            "goods": {"picUrl": "", "gallery": [], "isHot": False, "isNew": True, "isOnSale": True, "goodsSn": "9001",
                      "name": goods_name}, "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price": "66", "number": "66", "url": ""}],
            "attributes": []}
        self.goods.create(goods_data)
        goods_list_r = self.goods.list(goods_name)
        self.goods_id = goods_list_r["data"]["list"][0]["id"]
        goods_detail_r = self.goods.detail(self.goods_id)
        product_id = goods_detail_r["data"]["products"][0]["id"]
        logger.info(f"获取到的goodsid为{self.goods_id}, 获取到的productid为{product_id}")
        res = self.cart.add(self.goods_id, product_id)
        self.goods.delete(self.goods_id)
        # self.goods.delete_by_name(goods_name)
        # 添加断言信息
        assert res["errmsg"] == "成功"
