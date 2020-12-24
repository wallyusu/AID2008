# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    # 允许爬去的域名
    allowed_domains = ['www.baidu.com']
    # 起始的URL地址
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        """解析提取数据"""
        # response.xpath():[<>,<>,<>,...]
        # extract(): ['百度一下,你就知道'],会常使用
        # extract_first(): '百度一下,你就知道'  (序列化提取第一个)
        # get:同extract_first(),使用最多
        r = response.xpath('//title/text()').get()
        print(r)
        print('*' * 50)
        # text属性：响应内容-字符串
        # body属性：响应内容-字节串
        print(response.text)
        print(response.body)
