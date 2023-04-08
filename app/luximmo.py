import scrapy


class LuximmoSpider(scrapy.Spider):
    name = "luximmo"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
