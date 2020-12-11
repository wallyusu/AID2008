"""
笔趣阁小说数据抓取
1. 小说链接
2. 小说名称
3. 小说作者
4. 小说简介
"""
import re
import requests
import time
import random
import pymongo

class NoverSpider:
    def __init__(self):
        self.url = 'https://www.biqukan.cc/fenlei1/{}.html'
        self.headers = {'User-Agent':''}
        # 创建3个对象
        self.conn = pymongo.MongoClient(
            'localhost', 27017
        )
        self.db = self.conn['noveldb']
        self.myset = self.db['novelset']


    def get_html(self,url):
        html = requests.get(url=url,
                            headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self,html):
        """正则解析函数"""
        regex = '<div class="caption">.*?href="(.*?)" title="(.*?)">.*?<small class="text-muted fs-12">(.*?)</small>.*?>(.*?)</p>'
        novel_list = re.findall(regex,
                                html,
                                re.S)
        # 直接调用数据处理
        self.save_html(novel_list)

    def save_html(self, novel_list):
        """数据处理"""
        # 打印输出每个小数的数据
        for one_nover_tuple in novel_list:
            item = {}
            item['title'] = one_nover_tuple[1].strip()
            item['href'] = one_nover_tuple[0].strip()
            item['author'] = one_nover_tuple[2].strip()
            item['comment'] = one_nover_tuple[3].strip()
            print(item)
            # 存入MongoDB数据库
            self.myset.insert_one(item)

    def crawl(self):
        for page in range(1,6):
            page_url = self.url.format(page)
            self.get_html(url=page_url)
            # 控制数据抓取的频率
            time.sleep(random.randint(1,3))


if __name__ == '__main__':
    spider = NoverSpider()
    spider.crawl()