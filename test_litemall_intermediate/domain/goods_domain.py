
class GoodsDomain:
    """
    抽象的概念，不做具体的实现
    代表是某一种业务模型
    """
    def create(self):
        pass

    def delete(self):
        pass

    def list(self):
        pass

    def delete_by_name(self, name):
        goods_list_r = self.list(name)
        goods_id = goods_list_r["data"]["list"][0]["id"]
        self.delete(goods_id)