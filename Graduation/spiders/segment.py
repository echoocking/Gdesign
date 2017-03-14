# -*- coding: utf-8 -*-
import scrapy


class SegmentSpider(scrapy.Spider):
    name = "segment"
    allowed_domains = ["https://segmentfault.com/"]
    start_urls = ['http://https://segmentfault.com//']

    def parse(self, response):
        pass
