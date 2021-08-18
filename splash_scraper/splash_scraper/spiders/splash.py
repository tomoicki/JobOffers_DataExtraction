import scrapy
from scrapy_splash import SplashRequest
import datetime


class SplashSpider(scrapy.Spider):
    name = 'splash'
    # start_urls = ['https://nofluffjobs.com/pl/jobs/product-management']

    def start_requests(self):
        url = 'https://nofluffjobs.com/pl/jobs/product-management'
        yield SplashRequest(url, self.parse)

    def parse(self, response, **kwargs):
        all_jobs_from_site = response.xpath('//nfj-postings-list/a/@href').getall()
        base = 'https://nofluffjobs.com'
        for site in all_jobs_from_site:
            yield SplashRequest(base+site, self.parse_job, args={'wait': 1})

        # if next_button_disabled != 'page-item disabled':
        #     next_button = selenium_response.xpath('//a[@aria-label="Next"]/@href').get()
        #     yield from response.follow_all(next_button, self.parse)

    def parse_job(self, response, **kwargs):
        yield {
            'job_name': response.xpath(
                '//h1[@class="font-weight-bold bigger"]/text()').get(),
            'salary': response.xpath(
                '//h4[@class="mb-0"]/text()').get(),
            'requirements': response.xpath(
                '//a[@class="align-items-center back-to-all d-inline-flex"]/text()').getall() +
                            response.xpath(
                '//button[@class="btn btn-outline-success btn-sm no-cursor text-truncate"]/text()').getall(),
            'nice2have': response.xpath(
                '//nfj-posting-requirements[@id="posting-nice-to-have"]/descendant::a/text()').getall() +
                         response.xpath(
                '//nfj-posting-requirements[@id="posting-nice-to-have"]/descendant::button/text()').getall(),
            'employer': response.xpath(
                '//a[@id="postingCompanyUrl"]/descendant::dd/text()').get(),
            'location': response.xpath('//span[@class="text-break"]/text()').getall(),
            'experience': response.xpath(
                '//dt[contains(text(),"Doświadczenie")]/following-sibling::dd/text()').get(),
            'description': response.xpath(
                '//h2[contains(text()," Opis stanowiska ")]/following-sibling::nfj-read-more/text()').get(),
            'time_scraped': datetime.datetime.now()
        }