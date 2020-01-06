# Author:Pegasus-Yang
# Time:2020/1/5 11:03
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from PageObject0105.tools.login_tools import use_cookies_login


class BasePage:

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            # option = Options()
            # option.debugger_address = 'localhost:8888'
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
            use_cookies_login(self._driver)
            self._driver.get(self._url)

        else:
            self._driver = driver

    def get_url(self) -> str:
        """返回当前页面的URL"""
        return self._driver.current_url

    def get_title(self) -> str:
        """返回当前页面的Title"""
        return self._driver.title

    def quit(self):
        """在10秒后关闭浏览器"""
        sleep(10)
        self._driver.quit()
