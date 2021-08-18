import os
import datetime
now = datetime.date.today()

#  from businessanalyst to others makes around 20 links
spiders = [
           'hr'
           # 'backoffice',
           # 'marketing',
           # 'sales',
           # 'ux',
           # 'businessanalyst',
           ]


for spider in spiders:
    os.system(f"scrapy crawl {spider} -O json/archive_{now}/{spider}.json")


