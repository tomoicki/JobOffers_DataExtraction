import os
import datetime
now = datetime.date.today()

#  from bigdata to devops makes around 20 links
spiders = ['bigdata',
           'AI',
           'devops'
           ]

for spider in spiders:
    os.system(f"scrapy crawl {spider} -O json/archive_{now}/{spider}.json")
