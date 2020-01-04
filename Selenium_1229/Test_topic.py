# Author:Pegasus-Yang
# Time:2019/12/29 15:43
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class TestTesterHome:

    def wait_click(self, element):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(element)
        )

    def setup_method(self):
        option = Options()
        option.add_argument("headless")
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.get('https://testerhome.com/')

    def teardown_method(self):
        time.sleep(5)
        self.driver.quit()

    def test_page(self):
        button1 = (By.CSS_SELECTOR, 'div > button[data-toggle="dropdown"]')
        href1 = (By.CSS_SELECTOR, 'ul.list > li:nth-child(4) a')
        self.driver.find_element(By.CSS_SELECTOR, '[title="MTSC2020 中国互联网测试开发大会议题征集"]').click()
        self.wait_click(button1)
        self.driver.find_element(*button1).click()
        self.wait_click(href1)
        self.driver.find_element(*href1).click()