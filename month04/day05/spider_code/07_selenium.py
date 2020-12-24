"""
打开浏览器，输入百度的url地址
"""
from selenium import webdriver

# 1. 打开浏览器 - 创建浏览器对象
driver = webdriver.Chrome()

# 2. 输入百度URL地址
driver.get(url='http://www.baidu.com/')
html = driver.page_source
print(html)

driver.quit()

# 使用PhantomJS会有警告: 请使用无头版本的Chrome或Firefox替用