import re
import scrapy
from placement.items import Product


class PlacementSpider(scrapy.Spider):
    name = "integrated"
    start_urls = ['https://amity.edu/placement/upcoming-recruitment.asp']

    def parse(self, response):
        lists = response.xpath("//div[@class='content-wrapper']//li")

        for ilist in lists:
            x = Product()
            x['link'] = "https://amity.edu/placement/" + ilist.xpath("./a/@href").extract_first()
            x['name'] = ilist.xpath(".//strong/text()").extract_first().strip()
            x['year'] = re.findall(r'(20\w{2})', ilist.xpath(".//strong/text()").extract_first())
            yield x
