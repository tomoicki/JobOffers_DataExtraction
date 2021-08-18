from Scrapers.spiders.JustJoinSpider import JustJoinSpider
from Scrapers.spiders.NoFluffJobsSpider import NoFluffJobsSpider
from CrawlSpider import run_spider

# run_spider(NoFluffJobsSpider)
# run_spider(JustJoinSpider)
run_spider(NoFluffJobsSpider, JustJoinSpider)


