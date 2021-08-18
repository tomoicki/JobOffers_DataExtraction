from ..spiders.AbstractSpider import AbstractSpider
import scrapy
import json
import datetime


class JustJoinSpider(AbstractSpider):
    name = 'justjoin'
    start_urls = ['https://docs.scrapy.org/']

    @classmethod
    def __str__(cls):
        return cls.name

    def parse(self, response, **kwargs):
        url = 'https://justjoin.it/api/offers'
        yield scrapy.Request(url, callback=self.parse_api)

    def parse_api(self, response):
        base = 'https://justjoin.it/api/offers/'
        raw_data = response.body
        data = json.loads(raw_data)
        for offer in data:
            offer_id = offer['id']
            offer_url = base + offer_id
            yield scrapy.Request(offer_url, callback=self.parse_offer)

    def parse_offer(self, response):
        base = 'https://justjoin.it/offers/'
        offer_raw_data = response.body
        offer_data = json.loads(offer_raw_data)
        yield {
            'title': offer_data['title'],
            'company_name': offer_data['company_name'],
            'city': offer_data['city'],
            'workplace_type': offer_data['workplace_type'],
            'company_size': offer_data['company_size'],
            'company_url': offer_data['company_url'],
            'jj_url': base + offer_data['id'],
            'employment_types': offer_data['employment_types'],
            'experience_level': offer_data['experience_level'],
            'skills:': offer_data['skills'],
            'published_at': offer_data['published_at'],
            'scraped_at': datetime.datetime.now(),
            'expired': False,
            'expired_at': ' '
        }
