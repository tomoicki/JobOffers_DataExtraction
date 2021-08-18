from ..spiders.AbstractSpider import AbstractSpider
import scrapy
import json
import datetime


class NoFluffJobsSpider(AbstractSpider):
    name = 'nofluffjobs'
    start_urls = ['https://docs.scrapy.org/']

    @classmethod
    def __str__(cls):
        return cls.name

    def parse(self, response, **kwargs):
        url = 'https://nofluffjobs.com/api/posting/'
        yield scrapy.Request(url, callback=self.parse_api)

    def parse_api(self, response):
        base = 'https://nofluffjobs.com/api/posting/'
        raw_data = response.body
        data = json.loads(raw_data)
        actual_data = data['postings']
        id_list = []
        for item in actual_data:
            id_list.append(item['id'])
        id_list = list(set(id_list))
        for offer_id in id_list:
            offer_url = base + offer_id
            yield scrapy.Request(offer_url, callback=self.parse_offer)

    def parse_offer(self, response):
        base = 'https://nofluffjobs.com/pl/job/'
        offer_raw_data = response.body
        offer_data = json.loads(offer_raw_data)
        yield {
            'title': offer_data['title'],
            'company_name': offer_data['company']['name'],
            'city': offer_data['location']['places'],
            'company_size': offer_data['company']['size'],
            'jj_url': base + offer_data['postingUrl'],
            'employment_types': offer_data['essentials']['originalSalary'],
            'experience_level': offer_data['basics']['seniority'],
            'skills_must:': offer_data['requirements']['musts'],
            'skills_nice:': offer_data['requirements']['nices'],
            'scraped_at': datetime.datetime.now(),
            'expired': False,
            'expired_at': ' '
        }
