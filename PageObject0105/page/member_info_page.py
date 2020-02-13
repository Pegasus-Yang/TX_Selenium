# Author:Pegasus-Yang
# Time:2020/2/13 13:44
from selenium.webdriver.common.by import By

from PageObject0105.page.base_page import BasePage
from PageObject0105.page.edit_member_page import EditMemberPage


class MemberInfo(BasePage):

    def goto_edit_member_page(self):
        edit_button = (By.CSS_SELECTOR, '.qui_btn.ww_btn.js_edit')
        self._click_element(edit_button)
        return EditMemberPage(self._driver)
