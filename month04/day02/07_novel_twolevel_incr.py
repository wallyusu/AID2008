"""
增量爬虫：
"""
"""
*********一级页面需抓取***********
        1、小说名称
        2、小说详情页链接
        3、小说作者
        4、小说描述
        
*********二级页面需抓取***********
    1、最新更新的章节名称
    2、最新更新的章节链接
"""
import re
import requests
import time
import random
from hashlib import md5
import redis


class NovelSpider:
    def __init__(self):
        self.url = 'https://www.biqukan.cc/fenlei1/{}.html'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
        # 链接redis
        self.r = redis.Redis(
            host='localhost', port=6379, db=0
        )

    def get_html(self, url):
        """功能函数1：请求"""
        html = requests.get(url=url,
                            headers=self.headers).text
        return html

    def refunc(self, regex, html):
        """功能函数2：正则解析函数"""
        r_list = re.findall(regex, html, re.S)
        return r_list

    def md5_href(self,href):
        """功能函数3：md5加密"""
        m = md5()
        m.update(href.encode())

        return m.hexdigest()  # 对url进行hash加密
    def crawl(self, first_url):
        """爬虫逻辑函数"""
        first_html = self.get_html(url=first_url)
        first_regex = '<div class="caption">.*?href="(.*?)" title="(.*?)">.*?<small class="text-muted fs-12">(.*?)</small>.*?>(.*?)</p>'
        first_list = self.refunc(first_regex, first_html)
        for one_novel_tuple in first_list:
            item = {}
            item['title'] = one_novel_tuple[1].strip()
            item['href'] = one_novel_tuple[0].strip()
            item['author'] = one_novel_tuple[2].strip()
            item['comment'] = one_novel_tuple[3].strip()
            # 获取此本小说中剩余的数据
            self.parse_second_page(item)
            # print(item)

    def parse_second_page(self, item):
        """二级页面解析函数"""
        # 全部章节名称 和 链接
        second_html = self.get_html(url=item['href'])
        second_regex = '<dd class="col-md-4"><a href="(.*?)">(.*?)</a></dd>'
        second_list = self.refunc(
            second_regex, second_html
        )
        for second_tuple in second_list:
            item['son_title'] = second_tuple[1]
            item['son_href'] = second_tuple[0]
            # print(item)
            # 先生成指纹
            finger = self.md5_href(item['son_href'])
            if self.r.sadd('novel:spiders',finger) == 1:
                print('开始抓取此章节',item['son_title'])
            else:
                print('此章节已经抓取过')

    def run(self):
        for page in range(1, 2):
            page_url = self.url.format(page)
            self.crawl(page_url)
            # 控制频率
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    spider = NovelSpider()
    spider.run()
