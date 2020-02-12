# Author:Pegasus-Yang
# Time:2020/1/6 19:29
import pickle
import time
import os

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def login_and_save_cookies(driver: WebDriver = None):
    """打开登陆页面，登陆后抓取cookies信息保存下来以便之后自动登陆使用"""
    if driver is None:
        driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    while r'https://work.weixin.qq.com/wework_admin/loginpage_wx' in driver.current_url:
        time.sleep(5)
    cookies = []
    for i in driver.get_cookies():
        cookies.append(i)
    with open('../data/wxcookies.pickle', 'wb') as cookies_file:
        pickle.dump(cookies, cookies_file)


def use_cookies_login(driver: WebDriver):
    """加载wxcookies.pickle文件中的cookies信息，进入登陆状态"""
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    with open('../data/wxcookies.pickle', 'rb') as cookies_file:
        cookies = pickle.load(cookies_file)
    for i in cookies:
        if i.get('name') in ['wwrtx.refid', 'wwrtx.ref', 'wwrtx.i18n_lan']:
            continue
        driver.add_cookie(i)


def is_login_cookies_work() -> bool:
    """通过保存在wxcookies.pickle文件中的cookies中的过期时间判断cookies是否还有效"""
    if not os.path.exists('../data/wxcookies.pickle'):
        return False
    with open('../data/wxcookies.pickle', 'rb') as cookies_file:
        cookies = pickle.load(cookies_file)
    if len(cookies) == 0:
        return False
    for i in cookies:
        if i.get('name') in ['_gid']:
            if time.time() < i.get('expiry'):
                return True
    return False


def is_login_ok(driver: WebDriver) -> bool:
    """校验是否已登陆"""
    if r'https://work.weixin.qq.com/wework_admin/loginpage_wx' in driver.current_url:
        return False
    return True
