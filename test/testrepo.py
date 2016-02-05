''' 
Functional tests for the Map Repository.
'''

import os
import unittest
import urllib

from selenium import webdriver


BASE_URL = 'http://lin-mapactionrepo-stage.aptivate.org/'
USER = 'aptivate'
PASS = os.environ['TESTPASS']


WAIT_TIME = 5   #wait up to 5 seconds for pages to load

class Test(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(WAIT_TIME)
        self.addCleanup(self.browser.quit)
    
    #Just checking testing is working
    """
    def test_testing(self):
        self.assertTrue(True)


    #simple test checking there is something at the home page's URL.
    def test_simple_home_page_existence(self):

        page = urllib.urlopen(BASE_URL)
        contents = page.read()
        self.assertTrue(contents != None)
    """

    #Simple browser based test checking there's a plausible page at the home page's URL.
    def test_home_page(self):

        self.browser.get(BASE_URL)
        self.assertTrue('Map' in self.browser.title)


    def test_logging_in(self):

        self.login()
        username_element = self.browser.find_element_by_class_name('username')
        self.assertTrue(username_element.text == USER)


    def test_upload_zipped_dataset(self):

        #STEPS:
        #Login
        #Click on the "add dataset" button on the home page
        #Select the zip file
        #Click on the "finish" button
        #Go to the Datasets page
        #TEST CONDITION: Check the dataset is there

        #CLEAN UP:
        #Click on the dataset
        #Click on the "manage" button
        #Click on delete
        #Click on confirm
        #Go to the datasets page
        #TEST CONDITION: Check the dataset is not there




    #support function for logging in
    def login(self):
        self.browser.get(BASE_URL)
        login_link = self.browser.find_element_by_link_text('Log in')
        login_link.click()
        username_field = self.browser.find_element_by_id('field-login')
        username_field.send_keys(USER)
        pass_field = self.browser.find_element_by_id('field-password')
        pass_field.send_keys(PASS)
        pass_field.submit()






if __name__ == '__main__':
    unittest.main()

