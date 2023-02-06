"""
Helper module for executing all spiders.
https://docs.scrapy.org/en/latest/topics/practices.html#running-multiple-spiders-in-the-same-process
"""
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
# @TODO Import the Spider classes and add them to the list

# @TODO Include all imported spider classes in the list below
my_spiders = []


def run_simultaneously():
    """
    Run all spiders simultaneously.
    """
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    for spider in my_spiders:
        process.crawl(spider)
    process.start()  # the script will block here until all crawling jobs are finished


def run_sequentially():
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