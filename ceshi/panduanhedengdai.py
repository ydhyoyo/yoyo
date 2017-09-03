#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
class Base():
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,locator):
        element=WebDriverWait(self.driver,10,2).until(lambda x:x.find_element(*locator))
        return element
    def open(self,url):
        self.driver.get(url)
        self.driver.maxmize_window()#窗口最大化
    def move_to_element(self,locator):
        element=driver.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform
    def is_dis(self,locator):
        try:
             is_dis=WebDriverWait(self.driver,10,2).until_not(lambda x:x.find_element(*locator).is_dis())
             return True
        except:
             return False
    def send_keys(self,locator,text):
        self.find_element(locator).send_keys(text)
    def click(self,locator):
        self.find_element(locator).click()
    def clear(self,locator):
        self.find_element(locator).clear()
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
input_locator=("id","kw")
text=(u"北京")
Base(driver).send_keys(input_locator,text)
time.sleep(3)
driver.quit()