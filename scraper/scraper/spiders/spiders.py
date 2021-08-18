from . import nofluffspider


class Backend1Spider(nofluffspider.NoFluffSpider):
    name = 'backend1'
    start_urls = ['https://nofluffjobs.com/pl/jobs/backend',
                  'https://nofluffjobs.com/pl/jobs/backend?page=2',
                  'https://nofluffjobs.com/pl/jobs/backend?page=3',
                  'https://nofluffjobs.com/pl/jobs/backend?page=4',
                  'https://nofluffjobs.com/pl/jobs/backend?page=5',
                  'https://nofluffjobs.com/pl/jobs/backend?page=6',
                  'https://nofluffjobs.com/pl/jobs/backend?page=7',
                  'https://nofluffjobs.com/pl/jobs/backend?page=8',
                  'https://nofluffjobs.com/pl/jobs/backend?page=9',
                  'https://nofluffjobs.com/pl/jobs/backend?page=10',
                  'https://nofluffjobs.com/pl/jobs/backend?page=11',
                  'https://nofluffjobs.com/pl/jobs/backend?page=12',
                  'https://nofluffjobs.com/pl/jobs/backend?page=13',
                  'https://nofluffjobs.com/pl/jobs/backend?page=14',
                  'https://nofluffjobs.com/pl/jobs/backend?page=15',
                  'https://nofluffjobs.com/pl/jobs/backend?page=16',
                  'https://nofluffjobs.com/pl/jobs/backend?page=17',
                  'https://nofluffjobs.com/pl/jobs/backend?page=18',
                  'https://nofluffjobs.com/pl/jobs/backend?page=19',
                  'https://nofluffjobs.com/pl/jobs/backend?page=20',
                  'https://nofluffjobs.com/pl/jobs/backend?page=21',
                  'https://nofluffjobs.com/pl/jobs/backend?page=22',
                  ]


class Backend2Spider(nofluffspider.NoFluffSpider):
    name = 'backend2'
    start_urls = ['https://nofluffjobs.com/pl/jobs/backend?page=23',
                  'https://nofluffjobs.com/pl/jobs/backend?page=24',
                  'https://nofluffjobs.com/pl/jobs/backend?page=25',
                  'https://nofluffjobs.com/pl/jobs/backend?page=26',
                  'https://nofluffjobs.com/pl/jobs/backend?page=27',
                  'https://nofluffjobs.com/pl/jobs/backend?page=28',
                  'https://nofluffjobs.com/pl/jobs/backend?page=29',
                  'https://nofluffjobs.com/pl/jobs/backend?page=30',
                  'https://nofluffjobs.com/pl/jobs/backend?page=31',
                  'https://nofluffjobs.com/pl/jobs/backend?page=32',
                  'https://nofluffjobs.com/pl/jobs/backend?page=33',
                  'https://nofluffjobs.com/pl/jobs/backend?page=34',
                  'https://nofluffjobs.com/pl/jobs/backend?page=35',
                  'https://nofluffjobs.com/pl/jobs/backend?page=36',
                  'https://nofluffjobs.com/pl/jobs/backend?page=37',
                  'https://nofluffjobs.com/pl/jobs/backend?page=38',
                  'https://nofluffjobs.com/pl/jobs/backend?page=39',
                  'https://nofluffjobs.com/pl/jobs/backend?page=40',
                  'https://nofluffjobs.com/pl/jobs/backend?page=41',
                  'https://nofluffjobs.com/pl/jobs/backend?page=42',
                  'https://nofluffjobs.com/pl/jobs/backend?page=43',
                  'https://nofluffjobs.com/pl/jobs/backend?page=44',
                  'https://nofluffjobs.com/pl/jobs/backend?page=45',
                  'https://nofluffjobs.com/pl/jobs/backend?page=46',
                  'https://nofluffjobs.com/pl/jobs/backend?page=47',
                  'https://nofluffjobs.com/pl/jobs/backend?page=48',
                  'https://nofluffjobs.com/pl/jobs/backend?page=49',
                  'https://nofluffjobs.com/pl/jobs/backend?page=50'
                  ]


class FrontSpider(nofluffspider.NoFluffSpider):
    name = 'frontend'
    start_urls = ['https://nofluffjobs.com/pl/jobs/frontend',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=2',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=3',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=4',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=5',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=6',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=7',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=8',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=9',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=10',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=11',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=12',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=13',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=14',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=15',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=16',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=17',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=18',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=19',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=20',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=21',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=22',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=23',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=24',
                  'https://nofluffjobs.com/pl/jobs/frontend?page=25'
                  ]

class FullstackSpider(nofluffspider.NoFluffSpider):
    name = 'fullstack'
    start_urls = ['https://nofluffjobs.com/pl/jobs/fullstack',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=2',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=3',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=4',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=5',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=6',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=7',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=8',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=9',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=10',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=11',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=12',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=13',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=14',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=15',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=16',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=17',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=18',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=19',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=20',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=21',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=22',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=23',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=24',
                  'https://nofluffjobs.com/pl/jobs/fullstack?page=25'
                  ]


class MobileSpider(nofluffspider.NoFluffSpider):
    name = 'mobile'
    start_urls = ['https://nofluffjobs.com/pl/jobs/mobile',
                  'https://nofluffjobs.com/pl/jobs/mobile?page=2',
                  'https://nofluffjobs.com/pl/jobs/mobile?page=3',
                  'https://nofluffjobs.com/pl/jobs/mobile?page=4',
                  'https://nofluffjobs.com/pl/jobs/mobile?page=5',
                  'https://nofluffjobs.com/pl/jobs/mobile?page=6',
                  'https://nofluffjobs.com/pl/jobs/mobile?page=7',
                  'https://nofluffjobs.com/pl/jobs/mobile?page=8',
                  'https://nofluffjobs.com/pl/jobs/mobile?page=9',
                  'https://nofluffjobs.com/pl/jobs/mobile?page=10',
                  'https://nofluffjobs.com/pl/jobs/mobile?page=11',
                  'https://nofluffjobs.com/pl/jobs/mobile?page=12',
                  ]


class TestingSpider(nofluffspider.NoFluffSpider):
    name = 'testing'
    start_urls = ['https://nofluffjobs.com/pl/jobs/testing',
                  'https://nofluffjobs.com/pl/jobs/testing?page=2',
                  'https://nofluffjobs.com/pl/jobs/testing?page=3',
                  'https://nofluffjobs.com/pl/jobs/testing?page=4',
                  'https://nofluffjobs.com/pl/jobs/testing?page=5',
                  'https://nofluffjobs.com/pl/jobs/testing?page=6',
                  'https://nofluffjobs.com/pl/jobs/testing?page=7',
                  'https://nofluffjobs.com/pl/jobs/testing?page=8',
                  'https://nofluffjobs.com/pl/jobs/testing?page=9',
                  'https://nofluffjobs.com/pl/jobs/testing?page=10',
                  'https://nofluffjobs.com/pl/jobs/testing?page=11',
                  'https://nofluffjobs.com/pl/jobs/testing?page=12',
                  'https://nofluffjobs.com/pl/jobs/testing?page=13',
                  'https://nofluffjobs.com/pl/jobs/testing?page=14',
                  'https://nofluffjobs.com/pl/jobs/testing?page=15'
                  ]


class DevopsSpider(nofluffspider.NoFluffSpider):
    name = 'devops'
    start_urls = ['https://nofluffjobs.com/pl/jobs/devops',
                  'https://nofluffjobs.com/pl/jobs/devops?page=2',
                  'https://nofluffjobs.com/pl/jobs/devops?page=3',
                  'https://nofluffjobs.com/pl/jobs/devops?page=4',
                  'https://nofluffjobs.com/pl/jobs/devops?page=5',
                  'https://nofluffjobs.com/pl/jobs/devops?page=6',
                  'https://nofluffjobs.com/pl/jobs/devops?page=7',
                  'https://nofluffjobs.com/pl/jobs/devops?page=8',
                  'https://nofluffjobs.com/pl/jobs/devops?page=9',
                  'https://nofluffjobs.com/pl/jobs/devops?page=10',
                  'https://nofluffjobs.com/pl/jobs/devops?page=11',
                  'https://nofluffjobs.com/pl/jobs/devops?page=12',
                  ]


class AISpider(nofluffspider.NoFluffSpider):
    name = 'AI'
    start_urls = ['https://nofluffjobs.com/pl/jobs/artificial-intelligence',
                  'https://nofluffjobs.com/pl/jobs/artificial-intelligence?page=2',
                  'https://nofluffjobs.com/pl/jobs/artificial-intelligence?page=3',
                  'https://nofluffjobs.com/pl/jobs/artificial-intelligence?page=4',
                  'https://nofluffjobs.com/pl/jobs/artificial-intelligence?page=5'
                  ]


class BigdataSpider(nofluffspider.NoFluffSpider):
    name = 'bigdata'
    start_urls = ['https://nofluffjobs.com/pl/jobs/big-data',
                  'https://nofluffjobs.com/pl/jobs/big-data?page=2',
                  'https://nofluffjobs.com/pl/jobs/big-data?page=3',
                  'https://nofluffjobs.com/pl/jobs/big-data?page=4',
                  'https://nofluffjobs.com/pl/jobs/big-data?page=5'
                  ]

# 41
class EmbeddedSpider(nofluffspider.NoFluffSpider):
    name = 'embedded'
    start_urls = ['https://nofluffjobs.com/pl/jobs/embedded',
                  'https://nofluffjobs.com/pl/jobs/embedded?page=2',
                  'https://nofluffjobs.com/pl/jobs/embedded?page=3',
                  'https://nofluffjobs.com/pl/jobs/embedded?page=4',
                  'https://nofluffjobs.com/pl/jobs/embedded?page=5'
                  ]


class GamingSpider(nofluffspider.NoFluffSpider):
    name = 'gaming'
    start_urls = ['https://nofluffjobs.com/pl/jobs/gaming',
                  'https://nofluffjobs.com/pl/jobs/gaming?page=2',
                  'https://nofluffjobs.com/pl/jobs/gaming?page=3'
                  ]


class SupportSpider(nofluffspider.NoFluffSpider):
    name = 'support'
    start_urls = ['https://nofluffjobs.com/pl/jobs/support',
                  'https://nofluffjobs.com/pl/jobs/support?page=2',
                  'https://nofluffjobs.com/pl/jobs/support?page=3',
                  'https://nofluffjobs.com/pl/jobs/support?page=4',
                  'https://nofluffjobs.com/pl/jobs/support?page=5'
                  ]


class ITadminSpider(nofluffspider.NoFluffSpider):
    name = 'ITadmin'
    start_urls = ['https://nofluffjobs.com/pl/jobs/it-administrator',
                  'https://nofluffjobs.com/pl/jobs/it-administrator?page=2',
                  'https://nofluffjobs.com/pl/jobs/it-administrator?page=3',
                  'https://nofluffjobs.com/pl/jobs/it-administrator?page=4',
                  'https://nofluffjobs.com/pl/jobs/it-administrator?page=5'
                  ]


class AgileSpider(nofluffspider.NoFluffSpider):
    name = 'agile'
    start_urls = ['https://nofluffjobs.com/pl/jobs/agile',
                  'https://nofluffjobs.com/pl/jobs/agile?page=2',
                  'https://nofluffjobs.com/pl/jobs/agile?page=3'
                  ]


class ProductManagerSpider(nofluffspider.NoFluffSpider):
    name = 'productmanager'
    start_urls = ['https://nofluffjobs.com/pl/jobs/product-management',
                  'https://nofluffjobs.com/pl/jobs/product-management?page=2',
                  'https://nofluffjobs.com/pl/jobs/product-management?page=3'
                  ]


class ProjectManagerSpider(nofluffspider.NoFluffSpider):
    name = 'projectmanager'
    start_urls = ['https://nofluffjobs.com/pl/jobs/project-manager',
                  'https://nofluffjobs.com/pl/jobs/project-manager?page=2',
                  'https://nofluffjobs.com/pl/jobs/project-manager?page=3',
                  'https://nofluffjobs.com/pl/jobs/project-manager?page=4',
                  'https://nofluffjobs.com/pl/jobs/project-manager?page=5',
                  'https://nofluffjobs.com/pl/jobs/project-manager?page=6',
                  'https://nofluffjobs.com/pl/jobs/project-manager?page=7',
                  'https://nofluffjobs.com/pl/jobs/project-manager?page=8'
                  ]


class BusinessIntelligenceSpider(nofluffspider.NoFluffSpider):
    name = 'businessintelligence'
    start_urls = ['https://nofluffjobs.com/pl/jobs/business-intelligence',
                  'https://nofluffjobs.com/pl/jobs/business-intelligence?page=2',
                  'https://nofluffjobs.com/pl/jobs/business-intelligence?page=3',
                  'https://nofluffjobs.com/pl/jobs/business-intelligence?page=4',
                  'https://nofluffjobs.com/pl/jobs/business-intelligence?page=5',
                  'https://nofluffjobs.com/pl/jobs/business-intelligence?page=6'
                  ]


class BusinessAnalystSpider(nofluffspider.NoFluffSpider):
    name = 'businessanalyst'
    start_urls = ['https://nofluffjobs.com/pl/jobs/business-analyst',
                  'https://nofluffjobs.com/pl/jobs/business-analyst?page=2',
                  'https://nofluffjobs.com/pl/jobs/business-analyst?page=3',
                  'https://nofluffjobs.com/pl/jobs/business-analyst?page=4',
                  'https://nofluffjobs.com/pl/jobs/business-analyst?page=5',
                  'https://nofluffjobs.com/pl/jobs/business-analyst?page=6'
                  ]


class UXSpider(nofluffspider.NoFluffSpider):
    name = 'ux'
    start_urls = ['https://nofluffjobs.com/pl/jobs/ux',
                  'https://nofluffjobs.com/pl/jobs/ux?page=2',
                  'https://nofluffjobs.com/pl/jobs/ux?page=3',
                  'https://nofluffjobs.com/pl/jobs/ux?page=4',
                  'https://nofluffjobs.com/pl/jobs/ux?page=5',
                  'https://nofluffjobs.com/pl/jobs/ux?page=6'
                  ]


class SalesSpider(nofluffspider.NoFluffSpider):
    name = 'sales'
    start_urls = ['https://nofluffjobs.com/pl/jobs/sales',
                  'https://nofluffjobs.com/pl/jobs/sales?page=2',
                  'https://nofluffjobs.com/pl/jobs/sales?page=3'
                  ]


class MarketingSpider(nofluffspider.NoFluffSpider):
    name = 'marketing'
    start_urls = ['https://nofluffjobs.com/pl/jobs/marketing',
                  'https://nofluffjobs.com/pl/jobs/marketing?page=2',
                  'https://nofluffjobs.com/pl/jobs/marketing?page=3'
                  ]


class BackofficeSpider(nofluffspider.NoFluffSpider):
    name = 'backoffice'
    start_urls = ['https://nofluffjobs.com/pl/jobs/backoffice',
                  'https://nofluffjobs.com/pl/jobs/backoffice?page=2'
                  ]


class HRSpider(nofluffspider.NoFluffSpider):
    name = 'hr'
    start_urls = ['https://nofluffjobs.com/pl/jobs/hr',
                  'https://nofluffjobs.com/pl/jobs/hr?page=2'
                  ]


class OtherSpider(nofluffspider.NoFluffSpider):
    name = 'other'
    start_urls = ['https://nofluffjobs.com/pl/jobs/other',
                  'https://nofluffjobs.com/pl/jobs/other?page=2',
                  'https://nofluffjobs.com/pl/jobs/other?page=3',
                  'https://nofluffjobs.com/pl/jobs/other?page=4',
                  'https://nofluffjobs.com/pl/jobs/other?page=5',
                  'https://nofluffjobs.com/pl/jobs/other?page=6'
                  ]
