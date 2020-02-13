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
        self.index.quit_driver()

    def test_from_member_info_edit_member(self):
        edit_member_page = self.contacts_page.goto_member_info('aa').goto_edit_member_page()
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
        edit_member_page.press_save_button()
