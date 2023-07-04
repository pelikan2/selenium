import time
import unittest
"""Assert  je na overovanie niecoho
"""

from unittestzero import Assert
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



class FirstAutomationTests(unittest.TestCase):

    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("==user-data-dir=/Users/mac/Library/Application Support/Google/Chrome/")
        self.chrome_options.add_argument("==profile-directory=Default")
        self.browser = webdriver.Chrome(options=self.chrome_options)
        self.base_url = 'https://www.google.com'


    def test_gmail_button(self):
        self.browser.get(self.base_url)
        search_input = self.browser.find_element(By.ID, 'W0wltc')
        search_input.click()
        #assert search_input.text == "Google"
        search_input = self.browser.find_element(By.CLASS_NAME, 'gb_v')
        search_input.click()
        URL = self.browser.current_url
        Assert.not_none(URL)

        time.sleep(3)

    def tearDown(self):
        time.sleep(3)


    def test_2(self):
        self.browser.get(self.base_url)
        search_input = self.browser.find_element(By.ID, 'W0wltc')
        search_input.click()
        search_input = self.browser.find_element(By.ID, 'APjFqb')
        search_input.send_keys("Hello world")
        time.sleep(3)
        search_input.submit()
        URL = self.browser.current_url
        Assert.not_none(URL)


    if __name__ == "__main__":
        unittest.main()
