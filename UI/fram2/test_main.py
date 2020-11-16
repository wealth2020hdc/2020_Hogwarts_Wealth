# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from UI.fram2.main_page import MainPage


class TestMain:
    def test_main(self):
        main = MainPage()
        main.goto_market().goto_search().search()
