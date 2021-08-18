from abc import ABC, abstractmethod
import scrapy


class AbstractSpider(scrapy.Spider, ABC):
    name = 'abstract'

    @abstractmethod
    def parse(self, response, **kwargs) -> scrapy.Request:
        """Initial parse. This function yields scrapy.Request(url, callback=self.parse_api)."""
        pass

    @abstractmethod
    def parse_api(self, response) -> scrapy.Request:
        """This function intends to extract links to all job offers and send it to parse_offer function."""
        pass

    @abstractmethod
    def parse_offer(self, response) -> dict:
        """This function extracts desired information about specific job offer."""
        pass
