# Author:Pegasus-Yang
# Time:2020/1/5 21:41
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from PageObject0105.tools.common_tools import wait_load, clickable_wait


def select_inter(driver, inter):
    """国际区号选择"""
    if inter is not None:
        inter_list = (By.CSS_SELECTOR, '.ww_telInput_zipCode_input .qui_inputText.ww_inputText')
        si = (By.CSS_SELECTOR, '[data-value="{}"]'.format(inter))
        wait_load(driver).until(expected_conditions.element_to_be_clickable(inter_list))
        driver.find_element(*inter_list).click()
        wait_load(driver).until(expected_conditions.element_to_be_clickable(si))
        driver.find_element(*si).click()


def select_checkbox(driver, by, value, select):
    """复选框操作"""
    if clickable_wait(driver, by, value, select):
        if bool(select) ^ driver.find_element(by, value).is_selected():
            driver.find_element(by, value).click()
