import scrapy

class AvistaSpider(scrapy.Spider):
    name = "avista"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
