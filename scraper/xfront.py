import os
import datetime
now = datetime.date.today()

spiders = ['frontend']

for spider in spiders:
    os.system(f"scrapy crawl {spider} -O json/archive_{now}/{spider}.json")

