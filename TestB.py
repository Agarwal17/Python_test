'''
Created on Oct 17, 2017

@author: chetan.a
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
class letzNav(unittest.TestCase):


    @classmethod
    def setUpClass(ins):
        ins.driver=webdriver.Chrome("C:/Users/chetan.a/Documents/Softwares/Chrome Diriver/chromedriver.exe")
        ins.driver.implicitly_wait(6)
        ins.driver.get("https://navppm.herokuapp.com")
        ins.driver.title
        
    def test_2(self):
        pass
        self.username=self.driver.find_element_by_css_selector("input[name=username]").send_keys("venkateshwarlu.thota@excers.com") 
        self.password=self.driver.find_element_by_css_selector("input[name=password]").send_keys("Thota@excers169") 
        self.login=self.driver.find_element_by_css_selector("button[type=submit]").click()
        time.sleep(3)
    def test_3(self):
        pass
        self.createflow=self.driver.find_element_by_css_selector("button[class*=create-flow]").click()
        self.entertitle=self.driver.find_element_by_name("name").send_keys("test")
      #  time.sleep(6)
      # self.driver.find_element_by_css_selector("input[name=alwaysvisble]").click()
  
        driver.find_element_by_css_selector("input[name=alwaysvisble]").click()
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()