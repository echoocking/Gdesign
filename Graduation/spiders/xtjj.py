# -*- coding: utf-8 -*-
import scrapy


class XtjjSpider(scrapy.Spider):
    name = "xtjj"
    allowed_domains = ["https://gold.xitu.io/"]
    start_urls = ['http://https://gold.xitu.io//']

    def parse(self, response):
        pass
