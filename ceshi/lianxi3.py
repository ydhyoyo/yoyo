#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
url="http://mail.126.com"
driver.get(url)
time.sleep(3)
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").send_keys("abc")
driver.find_element_by_name("email").click()
#driver.find_element_by_name("password").send_keys("123")
#driver.find_element_by_id("dologin").click()
#driver.find_element_by_name("password").submit()
time.sleep(5)
driver.quit()
