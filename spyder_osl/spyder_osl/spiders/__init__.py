# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from spyder_osl.items import SpyderOslItem

class MySpider(BaseSpider):
    name = "spyder1"
    allowed_domains = ["osl.ugr.es"]
    start_urls = ["http://osl.ugr.es"]

    def parse(self, response):        
        for url in response.xpath('//header/h2/a/@href').extract():
			print url
			yield scrapy.Request(url, callback=self.obtener_items)
        
    def obtener_items(self, response):
		items = []
		for sel in response.xpath('//article'):
			item = SpyderOslItem()
			item ["titulo"] = sel.xpath('header[@class="entry-header"]/h1[@class="entry-title format-icon"]/text()').extract()
			item ["autor"] = sel.xpath('header/div/span/span/a/text()').extract()
			item ["contenido"] = sel.xpath('section[@class="entry-content "]/p/text()').extract()
			item ["categorias"] = sel.xpath('header[@class="entry-header"]/div[@class="entry-meta"]/a[contains(@href, "http://osl.ugr.es/category/")]/text()').extract()
			item ["etiquetas"] = sel.xpath('header[@class="entry-header"]/div[@class="entry-meta"]/a[contains(@href, "http://osl.ugr.es/tag/")]/text()').extract()

			yield item
