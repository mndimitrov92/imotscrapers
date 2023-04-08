import scrapy


class YourhomeSpider(scrapy.Spider):
    name = "yourhome"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
