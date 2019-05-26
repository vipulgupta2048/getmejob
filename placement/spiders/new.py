import re
import scrapy
from placement.items import Product

class PlacementSpider(scrapy.Spider):
    name = "new"

    def start_requests(self):
        urls = [
            'https://amity.edu/placement/upcoming-recruitment.asp',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lists = response.xpath("//div[@class='content-wrapper']//li")
        x = Product()
        for i in lists:
            x['link'] = "https://amity.edu/placement/" + i.xpath("./a/@href").extract_first()
            x['name'] = i.xpath(".//strong/text()").extract_first()
            print(i.xpath("//img").extract())
            # x['year'] = re.findall(r'(20\w{2})', i)
            yield x








        # x =  response.xpath("//div[@class='content-wrapper']//ul").get()
        # lists = response.xpath("//div[@class='content-wrapper']//ul")
        # lists = list(lists)

        # for listx in lists:
        #     link = response.xpath("//div[@class='content-wrapper']//li/a/@href").extract()
        #     print(link)
        #     # print("https://amity.edu/placement/" + link)
        #     # name = listx.xpath("//div[@class='content-wrapper']//li//strong/text()").get()
        #     # print(name)
        #     # year = re.findall(r'(20\w{2})',listx)
        #     # print(year)
        #     print(" ")

        # regex = re.findall(r'(20\w{2})',x)
        # regex = re.findall(r'(20\w{2})',listx )

        # for listx in lists:
        #     # Make the item dictionary
        #     link = response.xpath("//div[@class='content-wrapper']//li[1]/a/@href").extract_first()
        #     name = response.xpath("//div[@class='content-wrapper']//li[1]//strong/text()").get()
