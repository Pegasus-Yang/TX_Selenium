# Author:Pegasus-Yang
# Time:2020/1/5 22:03
from PageObject0105.page.index_page import IndexPage
import pytest

from PageObject0105.tools.common_tools import get_abs_path

user_info = ['../data/天马.jpg', 'aa', 'aa', 'tianma0002', '女', '86', '10012340001', '12340001',
             'tianma0001@tianma.com', '天马公司工位0001', '测试开发工程师', '自定义', '否']


class TestIndexAddMember:
    """从首页进入添加成员页面进行成员添加的用例"""
    def setup(self):
        self.index_page = IndexPage()

    def teardown(self):
        pass
        self.index.quit_driver()

    def test_from_index_add_member(self):
        add_member_page = self.index_page.goto_add_member_page()
        add_member_page.set_photo(get_abs_path(user_info[0]))
        add_member_page.set_name(user_info[1])
        add_member_page.set_nickname(user_info[2])
        add_member_page.set_userid(user_info[3])
        add_member_page.set_sex(user_info[4])
        add_member_page.set_mobile(user_info[5], user_info[6])
        add_member_page.set_phone(user_info[7])
        add_member_page.set_email(user_info[8])
        add_member_page.set_address(user_info[9])
        # add_member_page.set_department()
        add_member_page.set_duty(user_info[10])
        # add_member_page.set_identity()
        add_member_page.set_public_duty(user_info[11])
        add_member_page.set_is_sendinvite(user_info[12])
        user_list = add_member_page.press_save_button().get_user_list()
        assert user_info[1] == user_list[0].name
        assert user_info[10] == user_list[0].duty
        assert user_info[6] == user_list[0].mobile
        assert user_info[8] == user_list[0].email
