# -*- coding: utf-8 -*-
import scrapy


class PttrnsSpider(scrapy.Spider):
    name = "pttrns"
    allowed_domains = ["http://beta.pttrns.com/"]
    start_urls = (
        'http://beta.pttrns.com/?did=1&scid=33',
    )

    def parse(self, response):
        print '======================='
    	for sel in response.xpath('//div'):
    		
    		img = sel.xpath('//section/figure/a/img/@src').extract()
    		print img

    	print '======================='
