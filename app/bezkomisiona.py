import scrapy


class BezkomisionaSpider(scrapy.Spider):
    name = "bezkomisiona"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
