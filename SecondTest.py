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
        # self.chrome_options.add_argument("==user-data-dir=/Users/mac/Library/Application Support/Google/Chrome/")
        self.chrome_options.add_argument("==profile-directory=Default")
        self.browser = webdriver.Chrome(options=self.chrome_options)
        self.base_url = 'https://www.verizon.com/'
        self.browser.maximize_window()

    def test_one(self):
        self.browser.get(self.base_url)
        search_input = self.browser.find_element(By.ID, 'gnav20-sign-id')
        search_input.click()
        search_input = self.browser.find_element(By.CLASS_NAME, 'gnav20-dropdown-menu')
        data = search_input.text
        Assert.contains('Sign in to My Account', data)

    def tearDown(self):
        time.sleep(3)
        self.browser.close()