import scrapy


class MirelabgSpider(scrapy.Spider):
    name = "mirelabg"
    allowed_domains = ["todo"]
    start_urls = ["http://todo/"]

    def parse(self, response):
        pass
