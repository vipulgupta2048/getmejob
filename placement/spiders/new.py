import re
import json
import scrapy
from cerberus import Validator

class PlacementSpider(scrapy.Spider):
    name = "new"
    start_urls = ['https://amity.edu/placement/upcoming-recruitment.asp']

    def parse(self, response):
        lists = response.xpath("//div[@class='content-wrapper']//li")

        x = {}
        for ilist in lists:
            x['link'] = "https://amity.edu/placement/" + ilist.xpath("./a/@href").extract_first()
            x['name'] = ilist.xpath(".//strong/text()").extract_first().strip()
            year = re.findall(r'(20\w{2})', ilist.xpath(".//strong/text()").extract_first())
            try:
                x['year'] = int(year[0])
            except IndexError:
                x['year'] = "Any"
            print(x)

            with open("schema.json") as s:
                schema = json.loads(s.read())
            validator = Validator(schema)
            if validator.validate(x):
                print("Data validating ... 100% \n")
            else:
                 for field_name, error in validator.errors.items():
                    err = {}
                    err[field_name] = error
                    print(f"{err} \n")
                    break
