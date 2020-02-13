# Author:Pegasus-Yang
# Time:2020/1/5 20:01
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PageObject0105.page.base_page import BasePage


class AddMemberInfoPage(BasePage):
    """添加成员页面"""

    def __init__(self, driver: WebDriver = None, enter_page=None):
        """重载父类初始化方法，添加进入页的记录，期望能解决页面互相import问题"""
        super(AddMemberInfoPage, self).__init__(driver)
        self._enter_page = enter_page

    def _select_inter(self, inter):
        """从国际区号列表中选择输入的国际区号"""
        inter_list = (By.CSS_SELECTOR, '.ww_telInput_zipCode_input .qui_inputText.ww_inputText')
        inter_num = (By.CSS_SELECTOR, '[data-value="{}"]'.format(inter))
        self._click_element(inter_list)
        self._click_element(inter_num)

    def set_photo(self, photo):
        """设置头像，参数为头像图片绝对路径"""
        photo_button = (By.CSS_SELECTOR, '.member_edit_cover_avatar_mask.js_open_avatarEditor')
        photo_input = (By.CSS_SELECTOR, '.js_no_img.cropper_noImage .ww_fileInput.js_file')
        photo_save_button = (By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Blue.js_save')
        self._click_element(photo_button)
        self._find_element(photo_input).send_keys(photo)
        self._click_element(photo_save_button)

    def set_name(self, username):
        """设置姓名"""
        username_locator = (By.CSS_SELECTOR, '#username')
        self._clear_send_keys(username_locator, username)

    def set_nickname(self, nickname):
        """设置别名"""
        nickname_locator = (By.CSS_SELECTOR, '#memberAdd_english_name')
        self._clear_send_keys(nickname_locator, nickname)

    def set_userid(self, userid):
        """设置账号(成员唯一标识，设定以后不支持修改)"""
        userid_locator = (By.CSS_SELECTOR, '#memberAdd_acctid')
        self._clear_send_keys(userid_locator, userid)

    def set_sex(self, sex):
        """设置性别"""
        sex_select_locator = (By.CSS_SELECTOR, '[name="gender"]')
        if sex == '女':
            sex = True
        elif sex == '男':
            sex = False
        else:
            return False
        self._double_radio_select_right(sex_select_locator, sex)

    def set_mobile(self, inter, mobile):
        """设置手机号码(包含国际区号)"""
        mobile_num_locator = (By.CSS_SELECTOR, '#memberAdd_phone')
        self._select_inter(inter)
        self._clear_send_keys(mobile_num_locator, mobile)

    def set_phone(self, phone):
        """设置座机电话号码"""
        phone_locator = (By.CSS_SELECTOR, '#memberAdd_telephone')
        self._clear_send_keys(phone_locator, phone)

    def set_email(self, email):
        """设置邮箱"""
        email_locator = (By.CSS_SELECTOR, '#memberAdd_mail')
        self._clear_send_keys(email_locator, email)

    def set_address(self, address):
        """设置地址"""
        address_locator = (By.CSS_SELECTOR, '#memberEdit_address')
        self._clear_send_keys(address_locator, address)

    def set_department(self, department, major_department=None):
        """设置部门，department为List可以设置选择多个部门，major_department是用来设置为主部门的"""
        department_edit_locator = (By.CSS_SELECTOR, '.ww_groupSelBtn_add.js_show_party_selector')
        department_select_list = (By.CSS_SELECTOR, '.multiPickerDlg_right li')
        department_search_input_locator = (By.CSS_SELECTOR, '[placeholder="搜索部门"]')
        department_search_result_locator = (By.CSS_SELECTOR, '.multiPickerDlg_left_cnt .ww_searchResult ul li')
        department_save_locator = (By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Blue.js_submit')
        select_list = []
        self._click_element(department_edit_locator)
        for element in self._find_elements(department_select_list):
            select_list.append(element.find_elements(By.TAG_NAME, 'span')[1].text)
        if major_department not in select_list:
            self._clear_send_keys(department_search_input_locator, major_department)
            sleep(1)
            self._click_element(department_search_result_locator)
        for depart in department:
            if depart in select_list:
                continue
            self._clear_send_keys(department_search_input_locator, depart)
            sleep(1)
            self._click_element(department_search_result_locator)
        for e in self._find_elements(department_select_list):
            if (e.find_elements(By.TAG_NAME, 'span')[1].text == major_department) and (
                    e.find_elements(By.TAG_NAME, 'span')[2].text != '主部门'):
                self._driver.execute_script('arguments[0].click()', e.find_elements(By.TAG_NAME, 'span')[2])
                break
        self._click_element(department_save_locator)

    def set_duty(self, duty):
        """设置职务"""
        duty_locator = (By.CSS_SELECTOR, '#memberAdd_title')
        self._clear_send_keys(duty_locator, duty)

    def set_identity(self, identity):
        """设置身份"""
        identity_locator = (By.CSS_SELECTOR, '[name="identity_stat"]')
        if identity == '普通成员':
            self._double_radio_select_right(identity_locator, False)
        else:
            pass

    def set_public_duty(self, public_duty):
        """设置对外信息-职务，如果值不为(同步公司内职务)则会选择自定义并将值填入职务"""
        public_duty_locator = (By.CSS_SELECTOR, '[name="extern_position_set"]')
        public_duty_input_locator = (By.CSS_SELECTOR, '[name="extern_position"]')
        if public_duty == '同步公司内职务':
            self._double_radio_select_right(public_duty_locator, False)
        else:
            self._double_radio_select_right(public_duty_locator, True)
            self._clear_send_keys(public_duty_input_locator, public_duty)

    def set_is_sendinvite(self, is_send_invite):
        """设置是否通过邮件或短信发送企业邀请"""
        checkbox = (By.CSS_SELECTOR, '[name="sendInvite"]')
        if is_send_invite == '是':
            is_send_invite = True
        elif is_send_invite == '否':
            is_send_invite = False
        else:
            return False
        self._select_checkbox(checkbox, is_send_invite)  # 通过邮件或短信发送企业邀请

    def press_continue_button(self):
        """点击(保存并继续添加)按钮"""
        button = (By.CSS_SELECTOR, '.js_btn_continue')
        self._click_element(button)

    def press_save_button(self):
        """点击(保存)按钮"""
        button = (By.CSS_SELECTOR, '.js_btn_save')
        self._click_element(button)
        if self._enter_page is None:
            from PageObject0105.page.contacts_page import ContactsPage
            return ContactsPage(self._driver)
        else:
            return self._enter_page
