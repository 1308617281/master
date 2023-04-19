
from hamcrest import assert_that, close_to


class TestXueQiu:

    def setup_class(self):
        from xueqiuapp.base.xueqiu_app import XueQiuApp
        self.xueqiuapp = XueQiuApp()
        self.main = self.xueqiuapp.start().goto_main()

    def setup(self):
        self.main = self.xueqiuapp.start().goto_main()
        # self.main = self.xueqiuapp.start()

    def teardown_class(self):
        self.xueqiuapp.stop()

    def test_search(self):
        """
        打开【雪球】应用首页
        点击搜索框，进入搜索页面
        向搜索输入框中输入【alibaba】
        点击搜索结果中的【阿里巴巴】
        切换到 tab 的【股票】
        找到 股票【阿里巴巴】的股票价格 price
        判断 price 在 90 上下 10%浮动
        :return:
        """
        search_key = 'alibaba'
        search_result = "BABA"
        stock_price = self.main.click_search() \
            .input_searchcontent(search_key) \
            .click_searchresult(search_result) \
            .goto_stock_tab() \
            .get_price()
        assert_that(stock_price, close_to(90, 90 * 0.1))


    def test_search2(self):
        """
        打开【雪球】应用首页
        点击搜索框，进入搜索页面
        向搜索输入框中输入【alibaba】
        点击搜索结果中的【阿里巴巴】
        切换到 tab 的【股票】
        找到 股票【阿里巴巴】的股票价格 price
        判断 price 在 90 上下 10%浮动
        :return:
        """
        search_key = 'alibaba'
        search_result = "BABA"
        stock_price = self.main.click_search() \
            .input_searchcontent(search_key) \
            .click_searchresult(search_result) \
            .goto_stock_tab() \
            .get_price()
        assert_that(stock_price, close_to(90, 90 * 0.1))