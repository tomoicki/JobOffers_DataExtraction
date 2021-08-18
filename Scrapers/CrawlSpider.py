import datetime
from scrapy.crawler import CrawlerProcess


def run_spider(*spiders):
    """Function that is equivalent for 'scrapy crawl spider_name' in terminal but as an argument
    you can provide multiple spiders. It runs them in parallel."""
    spiders_list = list(spiders)
    for spider in spiders_list:
        process = CrawlerProcess(settings={
            "FEEDS": {
                f"json/{spider.__str__()}_{datetime.date.today()}.json": {"format": "json", "overwrite": True},
            },
        })
        # process.settings = {}
        process.crawl(spider)
    process.start()



