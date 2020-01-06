# Author:Pegasus-Yang
# Time:2020/1/6 19:29
import pickle
import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def save_login_cookies():
    """打开登陆页面，登陆后抓取cookies信息保存下来以便之后自动登陆使用"""
    driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    time.sleep(30)
    cookies = []
    for i in driver.get_cookies():
        cookies.append(i)
    with open('../data/wxcookies.pickle', 'wb') as cookies_file:
        pickle.dump(cookies, cookies_file)


def use_cookies_login(driver: WebDriver):
    """加载文件中的cookies信息，进入登陆状态"""
    driver.get('https://work.weixin.qq.com/wework_admin/')
    with open('../data/wxcookies.pickle', 'rb') as cookies_file:
        cookies = pickle.load(cookies_file)
    for i in cookies:
        if i.get('name') in ['wwrtx.refid', 'wwrtx.ref', 'wwrtx.i18n_lan']:
            continue
        driver.add_cookie(i)


