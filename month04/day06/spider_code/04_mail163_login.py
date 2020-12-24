from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='http://mail.163.com')

# 切换iframe
node = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
driver.switch_to.frame(node)
# 找节点：用户名 密码 登录按钮
driver.find_element_by_name('email').send_keys('willy.usu')
driver.find_element_by_name('password').send_keys('Wally018730')
driver.find_element_by_xpath('//*[@id="dologin"]').click()