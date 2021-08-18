# JobOffers_DataExtraction
On this branch we use scrapy library to gather data.
As both jobsites provide dynamic content, scrapy alone is not enough. Website initial respone needs to be handled by external tools that then provide html response understandable by scrapy.

To acheive this, we use selenium and its headless webdriver.

It scrapes nofluffjobs.com with several spiders, each spider has its own category to search from. For example "backend" spider goes only to https://nofluffjobs.com/pl/jobs/backend

Scraped data is put inside json/ directory, each spider produces one .json file. You will notice that each spider is fed with multiple links, for example /backend?page=2, /backend?page=3. Normally, it is not necessary. Each spider should be given domain like /backend and set of rules and directions which links to follow. It is done in nofluffspider.py (which is the parent class of all spiders) in lines 41-43, there the spider should find next page button and always after scraping data from one page automatically go to next page and do the same. For some odd reason it doesnt work here (tried and tested on many other sites and was working so far).

Note that, for selenium part to work properly you have to provide valid path to chromedrive.exe, line 13 in nofluffspider.py
