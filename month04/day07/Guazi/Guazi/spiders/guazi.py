# -*- coding: utf-8 -*-
import scrapy
from ..items import GuaziItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    url = 'https://www.guazi.com/bj/buy/o{}#bread'

    # 1. 删除start_url变量
    # 2. 重写start_urls()方法
    def start_requests(self):
        """生成所有要抓取的URL地址，交给调度器入队列"""
        for o in range(1, 6):
            page_url = self.url.format(o)
            # 交给调度器入队列
            yield scrapy.Request(url=page_url,
                                 callback=self.detail)

    def detail(self, response):
        """提取具体数据"""
        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for li in li_list:
            item = GuaziItem()
            item['name'] = li.xpath('./a/@title').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()
            item['link'] = 'https://www.guazi.com' + li.xpath('./a/@href').get()

            # 数据交给管道文件处理
            # yield item

            # 把详情页的链接继续交给调度器入队列
            # meta作用：不同解析函数间船体数据
            # meta随着请求先到调度器，然后到下载器，
            # 随着response一起交个callback解析函数
            yield scrapy.Request(
                url=item['link'],
                meta={'item':item},
            callback = self.get_car_info
            )

    def get_car_info(self,response):
        """二级页面解析函数：里程 排量 变速箱"""
        # 获取上个解析函数传递过来的item对象
        item = response.meta['item']
        item['km'] = response.xpath('//li[@class="two"]/span/text()').get()
        item['displace'] = response.xpath('//li[@class="three"]/span/text()').get()
        item['typ'] = response.xpath('//li[@class="last"]/span/text()').get()
        # 至此，一条完整的汽车数据提取完成，交给管道。
        yield item