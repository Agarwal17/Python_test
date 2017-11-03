import unittest
import HtmlTestRunner
import os
from TestA import CA_PPM
from TestB import letzNav

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
Test_A = unittest.TestLoader().loadTestsFromTestCase(CA_PPM)
Test_B = unittest.TestLoader().loadTestsFromTestCase(letzNav)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([Test_A, Test_B])

# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "wb")

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)