# Author:Pegasus-Yang
# Time:2020/2/13 13:49
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PageObject0105.page.base_page import BasePage


class EditMemberPage(BasePage):
    def __init__(self, driver: WebDriver = None, enter_page=None):
        """重载父类初始化方法，添加进入页的记录，期望能解决页面互相import问题"""
        super(EditMemberPage, self).__init__(driver)
        self._enter_page = enter_page

    def _clear_send_keys(self, locator, sendstr):
        """输入框显式等待、清理和字符串输入"""
        if self._clickable_wait(locator):
            self._find_element(locator).clear()
            self._find_element(locator).send_keys(sendstr)

    def _double_radio_select_right(self, locator, is_right):
        """成对的单选按钮组操作，is_right为True即为选择右边的按钮，False即为选择左边"""
        if self._clickable_wait(locator):
            self._find_elements(locator)[1].click() if is_right else \
                self._find_elements(locator)[0].click()

    def _select_checkbox(self, locator, select):
        """复选框操作，select为True则选中复选框，False则不选中"""
        if self._clickable_wait(locator):
            if select ^ self._find_element(locator).is_selected():
                self._find_element(locator).click()


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
        photo_save_button = (By.CSS_SELECTOR, '.qui_dialog_foot.ww_dialog_foot .qui_btn.ww_btn.ww_btn_Blue.js_save')
        self._click_element(photo_button)
        self._find_element(photo_input).send_keys(photo)
        self._click_element(photo_save_button)

    def set_name(self, username):
        """设置姓名"""
        username_locator = (By.CSS_SELECTOR, '#username')
        self._clear_send_keys(username_locator, username)

    def set_nickname(self, nickname):
        """设置别名"""
        nickname_locator = (By.CSS_SELECTOR, '#memberEdit_english_name')
        self._clear_send_keys(nickname_locator, nickname)

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
        mobile_num_locator = (By.CSS_SELECTOR, '#memberEdit_phone')
        self._select_inter(inter)
        self._clear_send_keys(mobile_num_locator, mobile)

    def set_phone(self, phone):
        """设置座机电话号码"""
        phone_locator = (By.CSS_SELECTOR, '#memberEdit_telephone')
        self._clear_send_keys(phone_locator, phone)

    def set_email(self, email):
        """设置邮箱"""
        email_locator = (By.CSS_SELECTOR, '#memberEdit_mail')
        self._clear_send_keys(email_locator, email)

    def set_address(self, address):
        """设置地址"""
        address_locator = (By.CSS_SELECTOR, '#memberEdit_address')
        self._clear_send_keys(address_locator, address)

    def set_department(self, department):
        """设置部门"""
        pass

    def set_duty(self, duty):
        """设置职务"""
        duty_locator = (By.CSS_SELECTOR, '#memberEdit_title')
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

    def press_save_button(self):
        """点击(保存)按钮"""
        button = (By.CSS_SELECTOR, '.member_colRight_operationBar.ww_operationBar .qui_btn.ww_btn.ww_btn_Blue.js_save')
        self._click_element(button)
        if self._enter_page is None:
            from PageObject0105.page.member_info_page import MemberInfo
            return MemberInfo(self._driver)
        else:
            return self._enter_page