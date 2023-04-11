from datetime import datetime
import re

import scrapy

from utils import ads_handler


class MirelabgSpider(scrapy.Spider):
    name = "mirelabg"
    allowed_domains = ["https://www.mirela.bg/"]
    start_urls = ["https://www.mirela.bg/index.php?p=offer_list&order_by=21&type=1&cities=3&districts%5B%5D=30&districts%5B%5D=27&districts%5B%5D=28&districts%5B%5D=32&districts%5B%5D=34&districts%5B%5D=37&districts%5B%5D=46&districts%5B%5D=5501&districts%5B%5D=50&districts%5B%5D=51&districts%5B%5D=52&districts%5B%5D=73&districts%5B%5D=77&districts%5B%5D=117&districts%5B%5D=475&districts%5B%5D=53&districts%5B%5D=59&districts%5B%5D=60&districts%5B%5D=61&districts%5B%5D=62&districts%5B%5D=63&districts%5B%5D=64&districts%5B%5D=6103&districts%5B%5D=6104&districts%5B%5D=71&ac_s=&ac_v=&map=&etypes%5B%5D=13&etypes%5B%5D=14&price_from=&price_to=200000&area_from=40&area_to=100&floor_from=&floor_to=&bedrooms=&bathrooms=&locations%5B%5D=54&building_type%5B%5D=480"]
    scraped_on = datetime.now().strftime('%Y-%m-%d')

    def parse(self, response):
        for ad in response.css(".offer-list"):
            if not ad.css('::attr(data-id)') .get():
                continue
            ad_url = response.urljoin(
                ad.css('.offer-list__title.offer-list__anchor::attr(href)').get())
            # These could not be retrieved from the scraping as they are contained sometimes in the title
            home_type = ""
            home_size = ""
            location = ""

            ad_price = ""
            price_string = ad.css(".offer-list__price").get()
            matches = re.findall(r'\d+', price_string)
            if matches:
                ad_price = ''.join(matches)

            ad_image = ""
            img_string = ad.css(
                ".offer-list__photo-main  .offer-list__image::attr('style')").get()
            match = re.search(r'url\((.*?)\)', img_string)
            if match:
                ad_image = match.group(1)

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
            '.b-pagination__list li:last-child a.b-pagination__item::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse, dont_filter=True)
