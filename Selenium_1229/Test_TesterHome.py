# Author:Pegasus-Yang
# Time:2019/12/29 13:02
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class TestTesterHome:

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get('https://testerhome.com/')

    def teardown_method(self):
        time.sleep(5)
        self.driver.quit()

    def test_mainpage(self):
        self.driver.find_element(By.CSS_SELECTOR, '#main-nav-menu > ul > li:nth-child(4) > a').click()
        time.sleep(2)
        WebDriverWait(self.driver,10,poll_frequency=0.5).until(
            expected_conditions.element_to_be_clickable(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]')
        )
        self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'div.panel-body > div:nth-child(1) > div.infos.media-body > div.title.media-heading > a').click()
