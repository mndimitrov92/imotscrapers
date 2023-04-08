import scrapy


class ArcorealSpider(scrapy.Spider):
    name = "arcoreal"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
