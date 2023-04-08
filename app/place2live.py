import scrapy


class Place2liveSpider(scrapy.Spider):
    name = "place2live"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
