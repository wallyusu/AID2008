"""
1、输入贴吧名称: 赵丽颖吧
2、输入起始页: 1
3、输入终止页: 2
4、保存到本地文件：赵丽颖吧_第1页.html、赵丽颖吧_第2页.html
"""

import requests
from urllib import parse
import time
import random


class TiebaSpider:
    def __init__(self):
        """定义常用变量"""
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

    def get_html(self, url):
        """
        请求函数：发请求获取html
        :return:
        """
        html = requests.get(url=url,
                            headers=self.headers).text
        return html

    def parse_html(self):
        """
        解析函数：解析提取数据
        :return:
        """
        pass

    def save_html(self, filename, html):
        """
        数据处理函数：比如存储数据库 CSV
        :return:
        """
        with open(filename, 'w') as f:
            f.write(html)

    def crawl(self):
        """
        程序入口函数：整体逻辑调控
        :return:
        """
        name = input('请输入贴吧名：')
        start = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        # 1. 先编码
        params = parse.quote(name)
        # 2. for循环拼接多页的url地址，请求+数据处理
        for content in range(start,end+1):
            pn = (content - 1) * 50
            page_url = self.url.format(params,pn)
            page_text = self.get_html(page_url)
            filename = '{}_第{}页.html'.format(name,content)
            self.save_html(filename,page_text)
        # 要求： 每抓取一页随机休眠1-3秒钟
            time.sleep(random.randint(1,3))


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.crawl()
