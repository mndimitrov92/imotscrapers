import scrapy


class SuperimotiSpider(scrapy.Spider):
    name = "superimoti"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
