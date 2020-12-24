"""
https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=80&limit=20
"""
import time
import requests
import json
import random
from fake_useragent import UserAgent


class DouBanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'

    def get_html(self, url):
        """功能函数"""
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).text()
        return html

    def parse_html(self, url):
        """爬虫逻辑函数"""
        html = self.get_html(url)
        html = json.loads(html)  # 将json转为python对象
        for one_film_dict in html:
            item = {}
            item['rank'] = one_film_dict['rank']
            item['title'] = one_film_dict['title']
            item['score'] = one_film_dict['score']
            item['time'] = one_film_dict['release_date']
            item['types'] = one_film_dict['types']
            print(item)

    def get_total(self):
        """获取某个类别下的电影总数"""
        pass

    def crawl(self):
        for start in range(0, 730, 20):
           page_url = self.url.format(start)
           self.parse_html(url=page_url)
           # 控制频率
           time.sleep(random.randint(0,3))

if __name__ == '__main__':
    spider = DouBanSpider()
    spider.crawl()