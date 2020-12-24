# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['https://maoyan.com/board/4']
    start_urls = ['https://maoyan.com/board/4/']

    def parse(self, response):
        # 提取具体数据
        dd_list = response.xpath('//dl/dd')
        for dd in dd_list:
            item = MaoyanItem()
            item['name'] = dd.xpath('./a/@title').get()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get()
            yield item

    # 进程 线程 协程
    # 协程： 微协程 纤程
    # yield 语句实现协程的关键字
    # 实现协程的模块： gevent greenlet
