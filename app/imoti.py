import scrapy

from utils import ads_handler


class ImotiSpider(scrapy.Spider):
    name = "imoti"
    allowed_domains = ["https://www.imoti.com/"]
    start_urls = ["todo"]

    def parse(self, response):
        pass
