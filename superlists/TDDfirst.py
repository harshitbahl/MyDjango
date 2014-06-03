# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 00:57:13 2014

@author: harshitbahl
"""
def main():
    from selenium import webdriver
    browser = webdriver.Firefox()
    browser.get('http://127.0.0.1:8000')
    assert 'Django' in browser.title

if __name__ == '__main__':  
    main()
