# Author:Pegasus-Yang
# Time:2020/1/5 22:03
from PageObject0105.page.index_page import IndexPage
import pytest

userinfo = [
    ('天马0001', 'tianma0001', '0001', 1,
     '82', '10012340001', '12340001', 'tianma0001@tianma.com', '天马公司工位0001',
     None, '测试开发工程师', 1, None,
     1, '测试', 0)
]


class TestIndexAddMember:
    def setup(self):
        self.index = IndexPage()
        pass

    def teardown(self):
        self.index.quit()

    @pytest.mark.parametrize('username, userid, nickname, sex,'
                             'inter,mobil,phone, email, addr,'
                             'group, duty, identity,leadergroup,'
                             'out_duty,inv,sendinvite', userinfo)
    def test_index_add_member(self, username, userid, nickname, sex,
                              inter, mobil, phone, email, addr,
                              group, duty, identity, leadergroup,
                              out_duty, inv, sendinvite):
        print('\n==============================11111111111111===================================\n')
        print(self.index.get_title())
        print(self.index.get_url())
        print('\n===============================11111111111111==================================\n')
        self.add_member = self.index.go_add_member_page()
        print('\n==============================222222222222222===================================\n')
        print(self.add_member.get_url())
        print(self.add_member.get_title())
        print('\n==============================222222222222222===================================\n')
        self.add_member.add_member_info(
            username=username, userid=userid, nickname=nickname, sex=sex,
            inter=inter, mobil=mobil, phone=phone, email=email, addr=addr,
            group=group, duty=duty, identity=identity, leadergroup=leadergroup,
            out_duty=out_duty, inv=inv, sendinvite=sendinvite)
