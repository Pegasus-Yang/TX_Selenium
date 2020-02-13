# Author:Pegasus-Yang
# Time:2020/2/13 10:21
from selenium.webdriver.common.by import By

from PageObject0105.page.base_page import BasePage
from PageObject0105.page.member_info_page import MemberInfo


class ContactsPage(BasePage):
    """通讯录页面(frame#contacts)"""
    _url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
    _user_list_locator = (By.CSS_SELECTOR, '.js_list')

    def _get_user_list_text(self, element):
        """获取元素下span标签中的值"""
        return element.find_element(By.TAG_NAME, 'span').text

    def get_user_list(self) -> list:
        """获取当前页面用户列表中的信息，并以数组方式返回"""

        class User:
            name = ''
            duty = ''
            department = ''
            mobile = ''
            email = ''

        result = []
        self._clickable_wait(self._user_list_locator)
        user_list = self._find_element(self._user_list_locator).find_elements(By.TAG_NAME, 'tr')
        for user_line in user_list:
            info = user_line.find_elements(By.TAG_NAME, 'td')
            user = User()
            user.name = self._get_user_list_text(info[1])
            user.duty = self._get_user_list_text(info[2])
            user.department = self._get_user_list_text(info[3])
            user.mobile = self._get_user_list_text(info[4])
            user.email = self._get_user_list_text(info[5])
            result.append(user)
        return result

    def goto_member_info(self, name):
        """根据姓名在列表中选择对应行进入用户信息详情页"""
        self._clickable_wait(self._user_list_locator)
        user_list = self._find_element(self._user_list_locator).find_elements(By.TAG_NAME, 'tr')
        for user_line in user_list:
            name_element = user_line.find_elements(By.TAG_NAME, 'td')[1]
            if self._get_user_list_text(name_element) == name:
                name_element.click()
                return MemberInfo(self._driver)
        return False
