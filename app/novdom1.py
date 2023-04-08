import scrapy


class Novdom1Spider(scrapy.Spider):
    name = "novdom1"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
