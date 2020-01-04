from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from time import sleep


class Testtmp:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/')
        self.driver.implicitly_wait(3)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    def switch_to_iframe(self, driver):
        if len(self.driver.find_elements(
                By.CSS_SELECTOR, '.ant-btn.published-form__submit.sc-htpNat.hyXsOZ.ant-btn-primary')) > 0:
            return True
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, 'iframe'))
        return False

    def test_temp(self):
        self.driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("问卷", Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, '.result:nth-child(1)>.topic>a').click()

        submit = (By.CSS_SELECTOR, '.ant-btn.published-form__submit.sc-htpNat.hyXsOZ.ant-btn-primary')
        WebDriverWait(self.driver, 10).until(self.switch_to_iframe)
        self.driver.find_element(*submit).click()
