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

    def get_member_info(self):
        class Member:
            name = ''
            nickname = ''
            userid = ''
            sex = ''
            mobile = ''
            phone = ''
            email = ''
            address = ''
            duty = ''
            public_duty = ''

        result = Member()
        name_locator = (By.CSS_SELECTOR, '.member_display_cover_detail_name')
        nickname_locator = (By.CSS_SELECTOR, '.member_display_cover_detail_bottom')
        mobile_locator = (By.CSS_SELECTOR, '.member_display_item_Phone .member_display_item_right')
        woman_locator = (By.CSS_SELECTOR, '.member_display_cover_detail_genderIcon.ww_commonImg.ww_commonImg_Woman')
        phone_locator = (By.CSS_SELECTOR, '.member_display_item_Tel .member_display_item_right')
        email_locator = (By.CSS_SELECTOR, '.member_display_item_Email .member_display_item_right')
        address_locator = (By.CSS_SELECTOR, '.member_display_item_WxNickName .member_display_item_right')
        duty_locator = (By.CSS_SELECTOR, '.member_display_sec .member_display_item_right')
        public_duty_locator = (By.CSS_SELECTOR,'.member_display_external_cnt .member_display_item_right')

        result.sex = '男' if len(self._find_elements(woman_locator)) == 0 else '女'
        result.name = self._find_element(name_locator).text
        result.nickname = self._find_elements(nickname_locator)[0].text[3:]
        result.userid = self._find_elements(nickname_locator)[1].text[3:]
        result.mobile = self._find_element(mobile_locator).text
        result.phone = self._find_element(phone_locator).text
        result.email = self._find_element(email_locator).text
        result.address = self._find_elements(address_locator)[1].text
        result.duty = self._find_elements(duty_locator)[7].text
        result.public_duty = self._find_elements(public_duty_locator)[1].text
        return result
