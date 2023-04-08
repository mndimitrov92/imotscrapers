import scrapy


class EraSpider(scrapy.Spider):
    name = "era"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
