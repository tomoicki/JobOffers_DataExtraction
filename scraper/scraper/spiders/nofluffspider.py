import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import datetime


def selenium_html_giver(link: str, class_name: str) -> scrapy.Selector:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('C:\chromedriver.exe', options=options)
    driver.get(link)
    WebDriverWait(driver, timeout=1, poll_frequency=0.01).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, class_name)))
    source = driver.page_source
    driver.quit()
    response = scrapy.Selector(text=source)
    return response


# r = selenium_html_giver(
#     'https://nofluffjobs.com/pl/job/android-developer-oke-poland-remote-iwccz8jw',
#     "d-block")
# print(r.xpath('//button').getall())


class NoFluffSpider(scrapy.Spider):
    name = 'nofluff'

    # start_urls = []

    def parse(self, response, **kwargs):
        selenium_response = selenium_html_giver(response.url, "ng-star-inserted")
        all_jobs_from_site = selenium_response.xpath('//nfj-postings-list/a/@href').getall()
        yield from response.follow_all(all_jobs_from_site, self.parse_job)

        selenium_response = selenium_html_giver(response.url, "page-link")
        next_button_disabled = selenium_response.xpath('//a[@aria-label="Next"]/parent::li/@class').get()
        # if next_button_disabled != 'page-item disabled':
        #     next_button = selenium_response.xpath('//a[@aria-label="Next"]/@href').get()
        #     yield from response.follow_all(next_button, self.parse)

    def parse_job(self, response):
        selenium_response = selenium_html_giver(response.url, "job")
        yield {
            'job_name': selenium_response.xpath(
                '//h1[@class="font-weight-bold bigger"]/text()').get(),
            'salary': selenium_response.xpath(
                '//span[@class="font-weight-bold font-size-20"]/text()').get(),
            'requirements': selenium_response.xpath(
                '//nfj-posting-requirements[@id="posting-requirements"]/descendant::a/text()').getall() +
                            selenium_response.xpath(
                '//nfj-posting-requirements[@id="posting-requirements"]/descendant::button/text()').getall(),
            'nice2have': selenium_response.xpath(
                '//nfj-posting-requirements[@id="posting-nice-to-have"]/descendant::a/text()').getall() +
                         selenium_response.xpath(
                '//nfj-posting-requirements[@id="posting-nice-to-have"]/descendant::button/text()').getall(),
            'employer': selenium_response.xpath(
                '//a[@id="postingCompanyUrl"]/descendant::dd/text()').get(),
            'location': selenium_response.xpath('//span[@class="text-break"]/text()').getall(),
            'experience': selenium_response.xpath(
                '//dt[contains(text(),"Doświadczenie")]/following-sibling::dd/text()').get(),
            'description': selenium_response.xpath(
                '//h2[contains(text()," Opis stanowiska ")]/following-sibling::nfj-read-more/text()').get(),
            'time_scraped': datetime.datetime.now()
        }