import time

from selenium import webdriver

class YdSpider:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url='http://fanyi.youdao.com/')
        self.word = input('请输入要翻译的单词: ')

    def translate(self):
        self.driver.find_element_by_xpath('//*[@id="inputOriginal"]').send_keys(self.word)
        time.sleep(1)
        result = self.driver.find_element_by_xpath('//*[@id="transTarget"]/p/span').text
        return result

if __name__ == '__main__':
    spider = YdSpider()
    result=spider.translate()
    print(result)