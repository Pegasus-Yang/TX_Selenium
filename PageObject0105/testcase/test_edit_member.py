# Author:Pegasus-Yang
# Time:2020/2/13 13:19
from PageObject0105.page.contacts_page import ContactsPage
from PageObject0105.tools.common_tools import get_abs_path

user_info = ['../data/5d7f51a0b0627.jpg', 'aaa', 'aaa', '男', '86', '10012340002', '12340002',
             'tianma0002@tianma.com', '天马公司工位0002', '测试开发工程师2', '同步公司内职务']


class TestEditMember:
    def setup(self):
        self.contacts_page = ContactsPage()

    def teardown(self):
        pass
        # self.contacts_page.quit_driver()

    def test_from_member_info_edit_member(self):
        edit_member_page = self.contacts_page.goto_member_info('aaa').goto_edit_member_page()
        edit_member_page.set_photo(get_abs_path(user_info[0]))
        edit_member_page.set_name(user_info[1])
        edit_member_page.set_nickname(user_info[2])
        edit_member_page.set_sex(user_info[3])
        edit_member_page.set_mobile(user_info[4], user_info[5])
        edit_member_page.set_phone(user_info[6])
        edit_member_page.set_email(user_info[7])
        edit_member_page.set_address(user_info[8])
        # edit_member_page.set_department()
        edit_member_page.set_duty(user_info[9])
        # edit_member_page.set_identity()
        edit_member_page.set_public_duty(user_info[10])
        member_info = edit_member_page.press_save_button().get_member_info()
        assert user_info[1] == member_info.name
        assert user_info[2] == member_info.nickname
        assert user_info[3] == member_info.sex
        assert user_info[5] == member_info.mobile
        assert user_info[6] == member_info.phone
        assert user_info[7] == member_info.email
        assert user_info[8] == member_info.address
        assert user_info[9] == member_info.duty
        assert user_info[10] == '同步公司内职务' if member_info.public_duty == member_info.duty else member_info.public_duty
