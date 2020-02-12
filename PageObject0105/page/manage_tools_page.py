# Author:Pegasus-Yang
# Time:2020/2/9 15:57
from selenium.webdriver.common.by import By

from PageObject0105.page.base_page import BasePage
from PageObject0105.page.material_page import MaterialPage


class ManageToolsPage(BasePage):
    """企业微信管理工具页(frame#manageTools)"""
    _url = 'https://work.weixin.qq.com/wework_admin/frame#manageTools'
    _material_page = (By.CSS_SELECTOR, '[href="#material/text"]')

    def goto_member_join_page(self):
        """跳转至成员加入页面"""
        pass

    def goto_contacts_sync_page(self):
        """跳转至通讯录同步页面"""
        pass

    def goto_create_message_page(self):
        """跳转至消息群发页面"""
        pass

    def goto_im_list_page(self):
        """跳转至用户消息页面"""
        pass

    def goto_material_page(self):
        """跳转至素材库页面"""
        self.clickable_wait(self._material_page)
        self.find_element(self._material_page).click()
        return MaterialPage(self._driver)

    def goto_interior_page(self):
        """跳转至员工服务页面"""
        pass

    def goto_log_page(self):
        """跳转至使用分析页面"""
        pass

    def goto_fuli_page(self):
        """跳转至奖励页面"""
        pass

    def goto_weekly_summary_page(self):
        """跳转至一周小结页面"""
        pass
