"""
//*[@id="app"]/div/div/div[1]/dl
"""
# 1. 打开浏览器 - 创建浏览器对象
from selenium import webdriver

# 设置无头模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
url = 'https://maoyan.com/board/4'


# 2. 输入百度URL地址
driver.get(url=url)
def parse_one_page():
    x = '//*[@id="app"]/div/div/div[1]/dl/dd'
    dd_list = driver.find_elements_by_xpath(x)
    for dd in dd_list:
        info_list = dd.text.split('\n')
        item = {}
        item['rank'] = info_list[0]
        item['name'] = info_list[1]
        item['star'] = info_list[2]
        item['time'] = info_list[3]
        item['score'] = info_list[4]
        print(item)

while True:
    parse_one_page()
    try:
        # 点击下一页
        driver.find_element_by_link_text('下一页').click()
    except Exception as e:
        print('抓取完成')
        break

