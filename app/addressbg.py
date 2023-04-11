from datetime import datetime
import scrapy

from utils import ads_handler


class AddressbgSpider(scrapy.Spider):
    name = "addressbg"
    allowed_domains = ["https://address.bg"]
    start_urls = [
        "https://address.bg/sale/sofia/l4451?sublocations=1231,1164,1147,1120&estateTypes=3,4,2,5&priceMax=200000"]
    scraped_on = datetime.now().strftime('%Y-%m-%d')

    def parse(self, response):
        for ad in response.css('.offer-card'):
            ad_url = ad.css('.content a::attr(href)').get()
            ad_image = ad.css('.image picture img::attr(src)').get()
            home_type = ad.css(
                '.content .row:last-child .right small::text').get()
            location = ad.css('.content .row > div > small::text').get()
            try:
                ad_price = ad.css(
                    '.content .row:last-child .left small.price::text').get().strip()
            except AttributeError:
                # No image found
                ad_price = "No price found"
            home_size = ad.css('.content .row .right small::text').get()
            data = {"url": ad_url,
                    "price": ad_price,
                    "home_type": home_type,
                    "home_size": home_size,
                    "location": location,
                    "image": ad_image,
                    "scraping_date": self.scraped_on,
                    "taken_from": self.allowed_domains[0],
                    "source_name": self.name}
            ads_handler.add_record(record_data=data)
            yield data
        # @TODO: Currently only collects data from the first page
        next_page = response.css(
            ".pagination .pagination-next-nav a.page-link:not(.disabled)::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse, dont_filter=True)
