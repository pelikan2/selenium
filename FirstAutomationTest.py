import time
import unittest

from unittestzero import Assert
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



class FirstAutomationTests(unittest.TestCase):

    if __name__ == "__main__":
        unittest.main()

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
        search_input = self.browser.find_element(By.CLASS_NAME, 'gb_E')
        search_input.click()
        search_input = self.browser.find_element(By.ID, 'identifierId')
        search_input.send_keys("pelikan.vladimir24@gmail.com")
        time.sleep(3)
        search_input = self.browser.find_element(By.ID, 'identifierNext')
        search_input.click()
        URL = self.browser.current_url
        Assert.not_none(URL)

    def tearDown(self):
        time.sleep(30)
        self.browser.close()


