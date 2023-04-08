"""
Helper module for executing all spiders.
https://docs.scrapy.org/en/latest/topics/practices.html#running-multiple-spiders-in-the-same-process
"""
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings


def run_simultaneously(my_spiders):
    """
    Run all spiders simultaneously.
    """
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    for spider in my_spiders:
        process.crawl(spider)
    process.start()  # the script will block here until all crawling jobs are finished


def run_sequentially(my_spiders):
    """
    Run all spiders one after the other
    """
    from twisted.internet import reactor, defer
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)

    @defer.inlineCallbacks
    def crawl():
        """
        Start the crawling
        """
        nonlocal runner
        for spider in my_spiders:
            yield runner.crawl(spider)
        reactor.stop()

    crawl()
    reactor.run()  # the script will block here until the last crawl call is finished


def execute(spider_list):
    """
    The function executes a list of spiders sequentially and simultaneously.

    :param spider_list: spider_list is a list of spider objects that will be passed to the functions
    run_sequentially and run_simultaneously. These spider objects are likely instances of a web scraping
    framework such as Scrapy or Beautiful Soup, and contain the logic for crawling and extracting data
    from websites
    """
    run_sequentially(my_spiders=spider_list)
    run_simultaneously(my_spiders=spider_list)
