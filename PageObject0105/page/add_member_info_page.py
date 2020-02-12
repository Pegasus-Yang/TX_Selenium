# Author:Pegasus-Yang
# Time:2020/1/5 20:01
from selenium.webdriver.common.by import By

from PageObject0105.page.base_page import BasePage


class AddMemberInfoPage(BasePage):
    """添加成员页面(frame#contacts)"""
    _url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'

    def _select_inter(self, inter):
        """从国际区号列表中选择输入的国际区号"""
        inter_list = (By.CSS_SELECTOR, '.ww_telInput_zipCode_input .qui_inputText.ww_inputText')
        inter_num = (By.CSS_SELECTOR, '[data-value="{}"]'.format(inter))
        self.clickable_wait(inter_list)
        self.find_element(inter_list).click()
        self.clickable_wait(inter_num)
        self.find_element(inter_num).click()

    def add_member_info(self, username=None, userid=None, nickname=None, sex=None,
                        inter=None, mobil=None, phone=None, email=None, addr=None,
                        group=None, duty=None, identity=None, leadergroup=None,
                        out_duty=None, inv=None, sendinvite=None):
        """添加成员页面详细数据填写"""
        """
        添加成员页面的填写成员信息
        测试用户数据完整格式(照片上传方式搞不定暂不考虑)：
        姓名,账号,别名,性别(0男 1女)
        国际区号,手机,座机,邮箱,地址
        部门,职务,身份(0普通成员 1上级),上级身份负责部门
        对外职务(0同步公司内职务 1自定义),自定义职务,是否通过邮件或短信发送企业邀请(0否 1是)
        """
        # todo 上传照片
        self.clear_send_keys(By.CSS_SELECTOR, '#username', username)  # 姓名
        self.clear_send_keys(By.CSS_SELECTOR, '#memberAdd_english_name', nickname)  # 别名
        self.clear_send_keys(By.CSS_SELECTOR, '#memberAdd_acctid', userid)  # 账号
        self.double_radio_select_right(By.CSS_SELECTOR, '[name="gender"]', sex)  # 性别
        self._select_inter(inter)  # 国际区号
        self.clear_send_keys(By.CSS_SELECTOR, '#memberAdd_phone', mobil)  # 手机号
        self.clear_send_keys(By.CSS_SELECTOR, '#memberAdd_telephone', phone)  # 座机号
        self.clear_send_keys(By.CSS_SELECTOR, '#memberAdd_mail', email)  # 邮箱
        self.clear_send_keys(By.CSS_SELECTOR, '#memberEdit_address', addr)  # 地址
        # todo 部门选择
        self.clear_send_keys(By.CSS_SELECTOR, '#memberAdd_title', duty)  # 职务
        self.double_radio_select_right(By.CSS_SELECTOR, '[name="identity_stat"]', identity)  # 身份
        # todo 身份-上级身份部门选择
        self.double_radio_select_right(By.CSS_SELECTOR, '[name="extern_position_set"]', out_duty)  # 对外职务
        if out_duty == 1:
            self.clear_send_keys(By.CSS_SELECTOR, '[name="extern_position"]', inv)  # 对外职务-自定义输入
        self.select_checkbox(By.CSS_SELECTOR, '[name="sendInvite"]', sendinvite)  # 通过邮件或短信发送企业邀请
