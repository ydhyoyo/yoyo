# coding = utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
url="http://mail.163.com"
driver.get(url)
time.sleep(3)
driver.switch_to.frame("x-URS-iframe")
#time.sleep(3)
#driver.switch_to.frame("login-form")
time.sleep(3)
driver.find_element_by_name("email").send_keys("abc")
time.sleep(3)
driver.find_element_by_name("password").send_keys("111")
time.sleep(3)
driver.find_element_by_id("dologin").click()