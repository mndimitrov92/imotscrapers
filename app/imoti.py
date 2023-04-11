from datetime import datetime
import scrapy

from utils import ads_handler


class ImotiSpider(scrapy.Spider):
    name = "imoti"
    allowed_domains = ["https://www.imoti.com"]
    start_urls = [
        "https://www.imoti.com/prodazhbi/grad-sofiya?et1=999&ybuild=2000&sraion=136~60~&price=200000&pubtype=2~3~&et=2"]
    scraped_on = datetime.now().strftime('%Y-%m-%d')

    def parse(self, response):
        for ad in response.css('.main .list .item'):

            ad_url = ad.css('a::attr(href)').get()
            ad_price = ad.css(".title .price::text").get().strip()
            home_type = ad.css(".title .type::text").get()
            home_size = ad.css(".location").get().split(
                "<br>")[-1].replace("</div>", "").strip()
            location = ad.css(".location::text").get().strip()
            ad_image = response.urljoin(ad.css(".photo img::attr(src)").get())
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
        next_page = response.css(
            ".pageNavigation a.page-link:not(.disabled)::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse, dont_filter=True)
