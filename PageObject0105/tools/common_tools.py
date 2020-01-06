# Author:Pegasus-Yang
# Time:2020/1/5 20:27
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def clickable_wait(driver: WebDriver, by, value, attr) -> bool:
    """判断参数是否传入、并进行clickable判断的显式等待"""
    if attr is None:
        return False
    wait_load(driver).until(expected_conditions.element_to_be_clickable((by, value)))
    return True


def wait_load(driver, pf=0.5, maxtime=10) -> WebDriverWait:
    """定义显式等待方法"""
    return WebDriverWait(driver, maxtime, poll_frequency=pf)


def clear_send_keys(driver, by, value, sendstr):
    """输入框显式等待、清理和输入"""
    if clickable_wait(driver, by, value, sendstr):
        driver.find_element(by, value).clear()
        driver.find_element(by, value).send_keys(sendstr)


def select_radio(driver, by, value, isright):
    """成对的单选按钮组操作"""
    if clickable_wait(driver, by, value, isright):
        driver.find_elements(by, value)[1].click() if bool(isright) else \
            driver.find_elements(by, value)[0].click()
