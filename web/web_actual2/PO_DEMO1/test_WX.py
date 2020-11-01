# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from web.web_actual2.PO_DEMO1.index_page import IndexPage


class Testwx:
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        self.index.goto_login().goto_register().register()

        # self.index.goto_register().register()
