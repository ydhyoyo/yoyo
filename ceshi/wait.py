#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get(("https://www.baidu.com"))
e=driver.find_element_by_id("kw")
print e
e1=WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("kw"))
print e1
e1.send_keys("beijing")
is_dis=WebDriverWait(driver,10,2,(ElementNotVisibleException)).until_not(lambda x:x.find_element_by_id("kw1").is_displayed())
print is_dis

#定位参数化
#e2=driver.find_element(By.ID,"kw")#id=By.ID
#e2.send_keys("yoyo")
e2=driver.find_element(id,"kw").send_keys("yoyo")

driver.quit()