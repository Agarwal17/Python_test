'''
Created on Oct 17, 2017

@author: chetan.a
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
 


class CA_PPM(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome("C:/Users/chetan.a/Documents/Softwares/Chrome Diriver/chromedriver.exe")
        cls.driver.implicitly_wait(6)
        cls.driver.get("http://clarityv15.excers.com")
        cls.driver.title
        
    def test_1(self):
        self.username=self.driver.find_element_by_id('ppm_login_username').send_keys("admin")
        self.password=self.driver.find_element_by_id('ppm_login_password').send_keys("clarity1")
        self.driver.find_element_by_id('ppm_login_button').click()
        try :
             self.error=self.driver.find_element_by_id("ppm_login_msg_aria_live").text
             self.assertTrue("CMN-10013: User name and password required.",self.error)
        except NoSuchElementException:
             print("skipped")
             
        
    def test_2(self):
        pass
        try:
            self.driver.find_element_by_class_name('letznav-black-label').click()
            self.search=self.driver.find_element_by_class_name('letznav-search-box').send_keys("Assign a Resource to a Task")
            self.driver.find_element_by_link_text("Assign a Resource to a Task").click()
            time.sleep(5)
            self.home=self.driver.find_element_by_css_selector('span[alt="Home"]')
            self.hover=ActionChains(self.driver).move_to_element(self.home)
            self.hover.perform()
            time.sleep(4)
            try:
                self.project=self.driver.find_element_by_css_selector('a[title="Projects"]').text
                time.sleep(3)
                self.assertEqual("Projects",self.project)
                self.project=self.driver.find_element_by_link_text("Projects").click()
                time.sleep(4)
            except NoSuchElementException:
                print("not pointed to projects") 
                

        except NoSuchElementException:
            print ("Skipped*****")
    
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
   
    
    
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()