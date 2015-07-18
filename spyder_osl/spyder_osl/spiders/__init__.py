# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from spyder_osl.items import SpyderOslItem

class MySpider(BaseSpider):
    name = "spyder1"
    allowed_domains = ["osl.ugr.es"]
    start_urls = ["http://osl.ugr.es"]

    def parse(self, response):
        #hxs = HtmlXPathSelector(response)
        #titles = hxs.select("//a")
        items = []
        for sel in response.xpath('//a'):
			item = SpyderOslItem()
			item ["titulo"] = sel.xpath("text()").extract()
			item ["link"] = sel.xpath("@href").extract()
			items.append(item)
        return items
