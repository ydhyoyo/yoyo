#coding:utf-8
class Title_is():
    def __init__(self,title):
        self.title=title
    def __call__(self,driver):
        return self.title==driver.title
def is_title(title,driver):
    return title==driver.title





