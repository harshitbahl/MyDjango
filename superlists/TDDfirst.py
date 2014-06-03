# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 00:57:13 2014

@author: harshitbahl
"""
from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_later(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('To Do', self.browser.title)
        self.fail('finished the test!!')
        
if __name__ == '__main__':  
    unittest.main()
