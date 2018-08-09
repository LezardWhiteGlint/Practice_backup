#!/usr/bin/env python3

#import and initiate webdriver
import os
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('window-size=800x600')
driver = webdriver.Chrome(executable_path='/Users/lezardvaleth/Documents/Python/chromedriver',chrome_options=options)
os.chdir('/Users/lezardvaleth/Documents/Python/Customer_Compensation')

#login backend
driver.get('http://34.237.161.188/portal/login')
account = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
login = driver.find_elements_by_id('submit-btn')
account.send_keys('admin')
password.send_keys('000000')
account.submit()

#go to compensation page
driver.get('http://34.237.161.188/portal/send-gold-diamond-honour-email?platform=2&district=1')
