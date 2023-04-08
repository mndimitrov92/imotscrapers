import scrapy


class UesSpider(scrapy.Spider):
    name = "ues"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
