import pytest

from master.test_litemail.page_objects.login_page import LoginPage


class TestLitemall:
    # 前置动作
    def setup_class(self):
        self.home = LoginPage().login()

    # 后置动作
    def teardown_class(self):
        self.home.do_quit()

    # 新增功能
    @pytest.mark.parametrize('category_name', ['x', 'y', 'z'])
    def test_add_type(self, category_name):
        lists = self.home \
            .go_to_category() \
            .click_add() \
            .create_category(category_name)
        res = lists.get_oprate_result()
        assert "创建成功" == res
        lists.delete_category(category_name)

    # 删除功能
    @pytest.mark.parametrize('category', ['delX', "delY", "delZ"])
    def test_delete_type(self, category):
        res = self.home \
            .go_to_category() \
            .click_add() \
            .create_category(category) \
            .delete_category(category) \
            .get_delete_result()
        assert "删除成功" == res
