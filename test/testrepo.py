''' 
Functional tests for the Map Repository.
'''

import os
import unittest
import urllib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = 'http://lin-mapactionrepo-stage.aptivate.org/'
USER = 'aptivate'
PASS = os.environ['TESTPASS']
TEST_ZIP_FILE = os.path.join('test_data', 'MA001_Aptivate_Example.zip')
TEST_TITLE = 'Central African Republic: \nExample Map-\nReference\n(as of 3 Feb 2099)'

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
        #Click on the "upload" button
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


        #Login
        self.login()

        #Click on the "add dataset" button on the home page
        add_dataset_link = self.browser.find_element_by_id('add_dataset')
        add_dataset_link.click()

        #enter the zip file to upload
        zip_file_field = self.browser.find_element_by_id('zip_file')
        path = os.path.abspath(TEST_ZIP_FILE)
        zip_file_field.text = path

        #Click on the "upload" button
        zip_file_upload_link = self.browser.find_element_by_id('zip_file_upload')
        zip_file_upload_link.click()
        #Wait for the file to upload
        element = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element_value((By.ID, 'field-title'), TEST_TITLE)
        )

        #save the form
        zip_file_field.submit()

        #Go to the datasets page
        self.browser.find_element_by_link_text('Datasets').click()

        #Check our new dataset is there
        dataset_link = self.browser.find_element_by_link_text(TEST_TITLE)


        #CLEAN UP

        #Click on the dataset
        dataset_link.click()

        #Click on the "manage" button
        self.browser.find_element_by_link_text('Manage').click()

        #Click on delete
        self.browser.find_element_by_link_text('Delete').click()

        #Click on confirm
        self.browser.find_element_by_link_text('Confirm').click()        

        #Go to the datasets page
        self.browser.find_element_by_link_text('Datasets').click()

        #TEST CONDITION: Check the dataset is not there
        link_list = self.browser.find_elements_by_link_text(TEST_TITLE)
        self.assertTrue(len(link_list) == 0)




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

