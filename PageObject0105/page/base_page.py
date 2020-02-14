# Author:Pegasus-Yang
# Time:2020/1/5 11:03
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject0105.tools.login_tools import use_cookies_login, is_login_cookies_work, is_login_ok, \
    login_and_save_cookies


class BasePage:
    """所有页面类的基类，定义一些公共方法供所有页面使用"""

    def __init__(self, driver: WebDriver = None):
        """基类初始化方法，如果cookies记录的登陆信息有效直接使用进行登陆，如果无效就进行扫码登陆并保存登陆后的cookies"""
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
            if is_login_cookies_work():
                use_cookies_login(self._driver)
            self._driver.get(self._url)
            while not is_login_ok(self._driver):
                login_and_save_cookies(self._driver)
                self._driver.get(self._url)
        else:
            self._driver = driver

    def get_url(self) -> str:
        """返回当前页面的URL"""
        return self._driver.current_url

    def get_title(self) -> str:
        """返回当前页面的Title"""
        return self._driver.title

    def quit_driver(self, delay=10):
        """在10秒后关闭浏览器"""
        sleep(delay)
        self._driver.quit()

    def _find_element(self, locator: tuple) -> WebElement:
        """封装selenium的find_element方法"""
        return self._driver.find_element(*locator)

    def _find_elements(self, locator: tuple) -> list:
        """封装selenium的find_elements方法"""
        return self._driver.find_elements(*locator)

    def _move_to_element(self, element):
        return ActionChains(self._driver).move_to_element(element)

    def _click_element(self, locator: tuple):
        """对元素进行clickable显式等待、并在结束后点击元素"""
        self._clickable_wait(locator)
        self._find_element(locator).click()

    def _wait_load(self, pf=0.5, maxtime=10) -> WebDriverWait:
        """为显式等待方法添加默认值"""
        return WebDriverWait(self._driver, maxtime, poll_frequency=pf)

    def _clickable_wait(self, locator: tuple) -> bool:
        """进行元素clickable判断的显式等待"""
        self._wait_load().until(expected_conditions.element_to_be_clickable(locator))
        return True

