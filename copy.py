from selenium import webdriver
import time
import os
if 'HTTP_PROXY'in os.environ:
    del os.environ['HTTP_PROXY']


browser = webdriver.Chrome() # open Chrome or Firefox
browser.get("http://*******.com") # load di.taobao.com
time.sleep(5) # let the page load

print('maximize browser')
browser.maximize_window() # maximize the browser window
browser.find_element_by_name('userName').send_keys('*****')
browser.find_element_by_name('password').send_keys('******')

verify = input('input verification code and press enter key :')
browser.find_element_by_name('verifyCode').send_keys(verify)
browser.find_element_by_xpath('*********').click()

time.sleep(5)