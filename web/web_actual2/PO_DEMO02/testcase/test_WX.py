# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from web.web_actual2.PO_DEMO02.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmenber(self):
        # username = "周杰伦4"
        # acctid = "singer100"
        # phonenumber = 16666666663
        # admenber = self.main.goto_addmenberpage()
        # admenber.addmenber(username, acctid, phonenumber)
        # assert username in admenber.getnumber()

        username = "刘欢10"
        acctid = "singger101"
        phonenumber = 16666666668
        admenber = self.main.goto_addmenberpage()
        admenber.addmenber(username, acctid, phonenumber)
        assert admenber.getnumber(username)
