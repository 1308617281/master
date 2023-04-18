
from faker import Faker


class TestContact:

    def setup_class(self):
        # 准备测试数据
        self.faker = Faker("zh_CN")
        # 实例化app
        from app_wework.base.wework_app import WeWorkApp
        self.app = WeWorkApp()

    def setup(self):

        # 启动app并进入首页
        self.main = self.app.start().goto_mian()

    def teardown_class(self):
        # 关闭app
        self.app.stop()

    def test_add_contact(self):
        name = self.faker.name()
        phone = self.faker.phone_number()
        # 链式调用，拼接业务逻辑
        toast_tips = self.main.goto_address_list().goto_add_member(). \
            goto_input_member().input_contact(name,phone).get_tips()

        assert toast_tips == "添加成功"
