#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as  EC
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
#判断文本内容
locator=("name","tj_trnews")
text=(u"新闻")
result=EC.text_to_be_present_in_element(locator,text)(driver)
#这句等价title=EC.text_to_be_present_in_element(locator,text)
#       a=title(dirver)    #   return a
print result
#判断元素属性
locator1=("id","su")
text1=(u"百度一下")
result1=EC.text_to_be_present_in_element_value(locator1,text1)(driver)
print result1
driver.quit()
