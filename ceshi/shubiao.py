#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
shezhi=driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(shezhi).perform()
time.sleep(3)
driver.find_element_by_link_text(u"搜索设置").click()
time.sleep(5)
driver.quit()
