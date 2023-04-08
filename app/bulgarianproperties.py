import scrapy


class BulgarianpropertiesSpider(scrapy.Spider):
    name = "bulgarianproperties"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
