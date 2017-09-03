#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By



class Base():
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,locator):
        element=WebDriverWait(self.driver,10,2).until(lambda x:x.find_element(*locator))
        return element
    def is_dis(self,locator):
        try:
             is_dis=WebDriverWait(self.driver,10,2).until_not(lambda x:x.find_element(*locator).is_dis())
             return True
        except:
             return False
    def send_keys(self,locator,text):
        self.find_element(locator).send_keys(text)
    def click(self,locator):
        self.find_element(locator).click

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
input_locator=("id","kw")
Base(driver).send_keys(input_locator,"xian")
button_locator=("id","su")
Base(driver).click(button_locator)
driver.quit()
