# Author:Pegasus-Yang
# Time:2020/1/5 19:13
from selenium.webdriver.common.by import By

from PageObject0105.page.add_member_info_page import AddMemberInfoPage
from PageObject0105.page.base_page import BasePage


class IndexPage(BasePage):
    """企业微信首页(frame#index)"""
    _url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_add_member_page(self):
        """跳转至添加成员页面"""
        _add_member = (By.CSS_SELECTOR, '[node-type="addmember"]')
        self._click_element(_add_member)
        return AddMemberInfoPage(self._driver)
