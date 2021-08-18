# JobOffers_DataExtraction
This approach incorporates both scrapy and requests library.

To use it, import function 'run_spider' from CrawlSpider module (as in example file try.py)


But there is a problem with CrawlerProcess so that you cannot use function run_spider twice in same script.
run_spider takes *args so give him multiple or one spider and it will work as long as you invoke it once.