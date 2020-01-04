# Author:Pegasus-Yang
# Time:2019/12/29 18:00
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# 测试用户数据完整格式(照片上传方式搞不定暂不考虑)：
# 姓名,账号,别名,性别(0男 1女)
# 国际区号,手机,座机,邮箱,地址
# 部门,职务,身份(0普通成员 1上级),上级身份负责部门
# 对外职务(0同步公司内职务 1自定义),自定义职务,是否通过邮件或短信发送企业邀请(0否 1是)

userinfo = [
    ('天马0001', 'tianma0001', '0001', 1,
     '82', '10012340001', '12340001', 'tianma0001@tianma.com', '天马公司工位0001',
     None, '测试开发工程师', 1, None,
     1, '测试', 0)
]


def wait_load(driver, pf=0.5, maxtime=10) -> WebDriverWait:
    """定义显式等待方法"""
    return WebDriverWait(driver, maxtime, poll_frequency=pf)


def is_in_add_page(driver: webdriver.Chrome) -> bool:
    """判断是否进入了添加成员页面"""
    if len(driver.find_elements(By.CSS_SELECTOR, '#username')) > 0:
        return True
    driver.find_element(By.CSS_SELECTOR, '[class|=ww_operationBar] .qui_btn.ww_btn.js_add_member').click()
    return False


class TestWorkWX:

    def setup_method(self):
        """每个测试用例执行前调用的方法，进行浏览器打开，页面打开等设定"""
        # 设定Chrome浏览器选项，调用已打开的chrome浏览器进行操作绕过扫码登陆部分
        option = Options()
        option.debugger_address = 'localhost:8888'
        self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()
        # 打开操作页面
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        # 设定隐式等待时间为5秒
        self.driver.implicitly_wait(2)

    def teardown_method(self):
        """每个测试用例执行完毕之后调用的方法，进行退出操作"""
        self.driver.quit()

    def contacts_to_add(self):
        """通讯录页面的进入添加成员页面(听错了作业要求。。暂时废弃这个方法)"""
        # todo 循环点击按钮，直到页面成功跳转   可以使用until方法
        # add_member = (By.CSS_SELECTOR, '[class|=ww_operationBar] .qui_btn.ww_btn.js_add_member')
        # wait_load(self.driver).until(lambda x: self.driver.execute_script('return $("[class|=ww_operationBar] .qui_btn.ww_btn.js_add_member").length') > 0)
        wait_load(self.driver).until(is_in_add_page)
        # ActionChains(self.driver).click(self.driver.find_element(*add_member)).perform()
        # self.driver.execute_script('$("[class|=ww_operationBar] .qui_btn.ww_btn.js_add_member").click()')

    def index_to_add_member(self):
        """通过首页进入添加成员页面"""
        add_member = (By.CSS_SELECTOR, '[node-type="addmember"]')
        wait_load(self.driver).until(ec.element_to_be_clickable(add_member))
        self.driver.find_element(*add_member).click()

    def clickable_wait(self, by, value, attr) -> bool:
        """判断参数是否传入、并进行clickable判断的显式等待"""
        if attr is None:
            return False
        wait_load(self.driver).until(ec.element_to_be_clickable((by, value)))
        return True

    def clear_send_keys(self, by, value, sendstr):
        """输入框显式等待、清理和输入"""
        if self.clickable_wait(by, value, sendstr):
            self.driver.find_element(by, value).clear()
            self.driver.find_element(by, value).send_keys(sendstr)

    def select_radio(self, by, value, isright):
        """成对的单选按钮组操作"""
        if self.clickable_wait(by, value, isright):
            self.driver.find_elements(by, value)[1].click() if bool(isright) else \
                self.driver.find_elements(by, value)[0].click()

    def select_inter(self, inter):
        """国际区号选择"""
        if inter is not None:
            list = (By.CSS_SELECTOR, '.ww_telInput_zipCode_input .qui_inputText.ww_inputText')
            si = (By.CSS_SELECTOR, '[data-value="{}"]'.format(inter))
            wait_load(self.driver).until(ec.element_to_be_clickable(list))
            self.driver.find_element(*list).click()
            wait_load(self.driver).until(ec.element_to_be_clickable(si))
            self.driver.find_element(*si).click()

    def select_checkbox(self, by, value, select):
        """复选框操作"""
        if self.clickable_wait(by, value, select):
            if bool(select) ^ self.driver.find_element(by, value).is_selected():
                self.driver.find_element(by, value).click()

    def add_member_info(self, username=None, userid=None, nickname=None, sex=None,
                        inter=None, mobil=None, phone=None, email=None, addr=None,
                        group=None, duty=None, identity=None, leadergroup=None,
                        out_duty=None, inv=None, sendinvite=None):
        """添加成员页面的填写成员信息"""
        # todo 上传照片
        self.clear_send_keys(By.CSS_SELECTOR, '#username', username)  # 姓名
        self.clear_send_keys(By.CSS_SELECTOR, '#memberAdd_english_name', nickname)  # 别名
        self.clear_send_keys(By.CSS_SELECTOR, '#memberAdd_acctid', userid)  # 账号
        self.select_radio(By.CSS_SELECTOR, '[name="gender"]', sex)  # 性别
        self.select_inter(inter)  # 国际区号
        self.clear_send_keys(By.CSS_SELECTOR, '#memberAdd_phone', mobil)  # 手机号
        self.clear_send_keys(By.CSS_SELECTOR, '#memberAdd_telephone', phone)  # 座机号
        self.clear_send_keys(By.CSS_SELECTOR, '#memberAdd_mail', email)  # 邮箱
        self.clear_send_keys(By.CSS_SELECTOR, '#memberEdit_address', addr)  # 地址
        # todo 部门选择
        self.clear_send_keys(By.CSS_SELECTOR, '#memberAdd_title', duty)  # 职务
        self.select_radio(By.CSS_SELECTOR, '[name="identity_stat"]', identity)  # 身份
        # todo 身份-上级身份部门选择
        self.select_radio(By.CSS_SELECTOR, '[name="extern_position_set"]', out_duty)  # 对外职务
        if out_duty == 1:
            self.clear_send_keys(By.CSS_SELECTOR, '[name="extern_position"]', inv)  # 对外职务-自定义输入
        self.select_checkbox(By.CSS_SELECTOR, '[name="sendInvite"]', sendinvite)  # 通过邮件或短信发送企业邀请

    def submit_contact(self):
        """添加成员页面submit提交"""
        self.driver.find_element(By.CSS_SELECTOR, 'form').submit()

    def save_contact(self):
        """添加成员页面保存按钮提交"""
        savebutton = (By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save')
        wait_load(self.driver).until(ec.element_to_be_clickable(savebutton))
        self.driver.find_elements(*savebutton)[0].click()

    @pytest.mark.parametrize('username, userid, nickname, sex,'
                             'inter,mobil,phone, email, addr,'
                             'group, duty, identity,leadergroup,'
                             'out_duty,inv,sendinvite', userinfo)
    def test_index_addContact(self, username, userid, nickname, sex,
                              inter, mobil, phone, email, addr,
                              group, duty, identity, leadergroup,
                              out_duty, inv, sendinvite):
        """首页-添加成员-填写信息-点击保存"""
        self.contacts_to_add()
        # self.index_to_add_member()
        # self.add_member_info(username=username, userid=userid, nickname=nickname, sex=sex,
        #                      inter=inter, mobil=mobil, phone=phone, email=email, addr=addr,
        #                      group=group, duty=duty, identity=identity, leadergroup=leadergroup,
        #                      out_duty=out_duty, inv=inv, sendinvite=sendinvite)
        # self.save_contact()
        # self.submit_one_contact()
