# JobOffers_DataExtraction
On this branch we use scrapy library to gather data. As both jobsites provide dynamic content, scrapy alone is not enough. Website initial respone needs to be handled by external tools that then provide html response understandable by scrapy.

To achieve this, we use splash and its website renderer.

For more details how to set up splash visit:
https://github.com/scrapy-plugins/scrapy-splash
