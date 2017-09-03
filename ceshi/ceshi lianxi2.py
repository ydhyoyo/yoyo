#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys(u"中国")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.get("https://www.jd.com")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
driver.quit()
