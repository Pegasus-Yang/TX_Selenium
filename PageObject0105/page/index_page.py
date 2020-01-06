# Author:Pegasus-Yang
# Time:2020/1/5 19:13
from selenium.webdriver.common.by import By

from PageObject0105.page.add_member_info_page import AddMemberInfoPage
from PageObject0105.page.base_page import BasePage


class IndexPage(BasePage):
    _url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    _add_member = (By.CSS_SELECTOR, '[node-type="addmember"]')

    def go_add_member_page(self):
        self._driver.find_element(*self._add_member).click()
        return AddMemberInfoPage(self._driver)