import time
import unittest

from unittestzero import Assert
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


class ThirdAutomationTests(unittest.TestCase):
    if __name__ == "__main__":
        unittest.main()

    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        # self.chrome_options.add_argument("==user-data-dir=/Users/mac/Library/Application Support/Google/Chrome/")
        self.chrome_options.add_argument("==profile-directory=Default")
        self.browser = webdriver.Chrome()   #options=self.chrome_options
        self.base_url = 'https://toolsqa.com/'
        self.browser.maximize_window()

    def test_three(self):
        self.browser.get(self.base_url)
        time.sleep(1)
        search_input = self.browser.find_element(By.ID, 'accept-cookie-policy')
        search_input.click()
        search_input = self.browser.find_element(By.CSS_SELECTOR, '.btn-primary-shadow')
        search_input.click()
        search_input = self.browser.find_element(By.ID, 'first-name')
        search_input.send_keys('Johan')
        search_input = self.browser.find_element(By.ID, 'last-name')
        search_input.send_keys('Lajos')
        search_input = self.browser.find_element(By.ID, 'email')
        search_input.send_keys('j.lajos@gmail.com')
        search_input = self.browser.find_element(By.ID, 'mobile')
        search_input.send_keys('+4214214214214')
        search_input = self.browser.find_element(By.ID, 'country')
        search_input.click()
        select = Select(search_input)
        select.select_by_visible_text('Slovakia')
        search_input = self.browser.find_element(By.ID, 'city')
        search_input.send_keys('Cadca')
        search_input = self.browser.find_element(By.ID, 'message')
        search_input.send_keys('My message')
        search_input = self.browser.find_element(By.ID, 'code')
        search_input.send_keys('nope')
        search_input = self.browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
        search_input.click()
        time.sleep(1)
        search_input = self.browser.find_element(By.CSS_SELECTOR, '.alert.show')
        output = search_input.text
        Assert.equal('Sorry ! Unable to verify that you are human.', output)


    def tearDown(self):
        time.sleep(3)
        self.browser.close()
