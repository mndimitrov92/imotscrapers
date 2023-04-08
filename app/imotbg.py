import scrapy


class ImotbgSpider(scrapy.Spider):
    name = "imotbg"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
