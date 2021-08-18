import os
import datetime
now = datetime.date.today()

#  from testing to mobile makes around 20 links
spiders = ['testing',
           'mobile'
           ]

for spider in spiders:
    os.system(f"scrapy crawl {spider} -O json/archive_{now}/{spider}.json")


