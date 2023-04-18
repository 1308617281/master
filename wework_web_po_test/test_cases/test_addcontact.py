
import pytest
from faker import Faker

from wework_web_po_test.page_object.login_page import LoginPage


class TestAddContact:
    def setup(self):
        """资源初始化"""
        fake: Faker = Faker("zh_CN")#如果要生成中文的随机数据，我们可以在实例化时给locale参数传入‘zh_CN’这个值：
        self.username = fake.name()
        self.accid = fake.ssn()   #随机生成身份证号
        self.mobile = fake.phone_number()
        self.browser = LoginPage()

    # def teardown(self):
    #     self.browser.quit()

    def test_addcontact(self):
        """添加成员"""
        contact_list = self.browser.login().click_add_member().\
            edit_contact(self.username, self.accid,self.mobile)

        tips = contact_list.get_tips()
        assert tips=='保存成功'
        # 删除联系人
        contact_list.del_contact(self.username)

    @pytest.mark.parametrize("username", ["联系人1","联系人2"])
    def test_addcontact1(self,username):
        """添加成员"""
        contact_list = self.browser.login().click_add_member().\
            edit_contact(username, self.accid,self.mobile)

        tips = contact_list.get_tips()
        assert tips=='保存成功'
        # 删除联系人
        contact_list.del_contact(username)



