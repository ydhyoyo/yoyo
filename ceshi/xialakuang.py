#coding=utf-8
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://weibo.com/signup/signup.php")
time.sleep(3)
driver.find_element_by_xpath('//*[@class="tel_country CH"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@class="select"]/a').click()
time.sleep(5)
driver.quit()

