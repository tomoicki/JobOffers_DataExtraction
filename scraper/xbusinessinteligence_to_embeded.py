import os
import datetime
now = datetime.date.today()

#  from embeded to businessintelligence makes around 20 links
spiders = ['businessintelligence',
           'projectmanager',
           'productmanager',
           'agile',
           'ITadmin',
           'support',
           'gaming',
           'embedded']

for spider in spiders:
    os.system(f"scrapy crawl {spider} -O json/archive_{now}/{spider}.json")


