from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders.crawl import CrawlSpider, Rule
from scrapy.http.request import Request
from scrapy.http.request.form import FormRequest


class OdeskSpider(CrawlSpider):
    name = 'odesk_spider'
    allowed_domains = ['odesk.com']
    start_urls = ['https://www.odesk.com/login']
    login_url = 'https://www.odesk.com/login'
    rules = [Rule(
        SgmlLinkExtractor(allow=('')),
        callback='after_login',
        follow=True,
    )]

    def init_request(self):
        return Request(url=self.login_url, callback=self.login)

    def login(self, response):
        return FormRequest.from_response(response,
                                         formdata={'username': 'niger.aleksandr@rambler.ru', 'password': 'vital11..'},
                                         callback=self.after_login)

    def after_login(self, response):
        with open('filename', 'wb') as f:
            f.write(response.body)
        if 'Andrey Sykhovei' in response.body:
            self.log('ololo!!')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        else:
            self.log('not ololo')
            print('---------------------------------------')