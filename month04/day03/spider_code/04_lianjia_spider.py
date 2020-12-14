"""
链家二手房数据抓取
"""

import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent
import pymysql


class LianJiaSpider:
    def __init__(self):
        self.url = 'https://sh.lianjia.com/ershoufang/pg{}/'
        self.db = pymysql.connect('localhost','root','123456','lianjia_db',charset='utf8')
        self.cur = self.db.cursor()

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        # utf-8:查看源代码charset的值
        # ignore:解码时遇到不识别的字符直接忽略
        # .text能自动识别编码
        html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')
        # 直接调用解析函数
        self.parse_html(html)


    def parse_html(self, html):
        """xpath解析提取数据"""
        eobj = etree.HTML(html)
        li_list = eobj.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        for li in li_list:
            item = {}
            name_list = li.xpath(".//div[@class='positionInfo']/a[1]/text()")
            item['name'] = name_list[0].strip() if name_list else None
            add_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            item['add'] = add_list[0].strip() if add_list else None
            info_list = li.xpath('.//div[@class="houseInfo"]/text()')
            item['info'] = info_list[0].strip() if info_list else None
            total_list = li.xpath('.//div[@class="totalPrice"]/span/text()')
            item['total'] = total_list[0].strip() if total_list else None
            unit_list = li.xpath('.//div[@class="unitPrice"]/span/text()')
            item['unit'] = unit_list[0].strip() if unit_list else None
            self.save_html(item)

    def save_html(self,item):
        """存储数据处理"""
        lianjia_list = [values for key,values in item.items()]
        print(lianjia_list)
        info = 'insert into lianjia_info values (%s,%s,%s,%s,%s);'
        self.cur.execute(info,lianjia_list)
        self.db.commit()


    def crawl(self):
        for page in range(11):
            page_url = self.url.format(page)
            self.get_html(url=page_url)
            # 控制频率
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    spider = LianJiaSpider()
    spider.crawl()
