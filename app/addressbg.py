import scrapy


class AddressbgSpider(scrapy.Spider):
    name = "addressbg"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
