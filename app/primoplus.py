import scrapy


class PrimoplusSpider(scrapy.Spider):
    name = "primoplus"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
