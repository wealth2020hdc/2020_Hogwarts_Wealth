# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from app.actual2.page.app import App
from app.actual2.page.memberInvitemenupage import MemberInviteMenuPage


class TestContact:

    def setup(self):
        self.app = App()
        self.main = self.app.start().go_to_main()

    def test_addcontact(self):
        name = "周杰伦100"
        gender = "男"
        phonenumber = "16600000100"
        result = self.main.goto_address(). \
            click_addmember(). \
            add_member_menual(). \
            add_contact(name, gender, phonenumber).get_toast()
        assert "添加成功" == result

    def test_delmemver(self):
        username = "周杰伦100"
        result = self.main.goto_address(). \
            click_delmember(username). \
            click_seting(). \
            click_edit(). \
            click_delmember()
        assert result
