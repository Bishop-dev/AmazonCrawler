from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from tutorial.items import AmazonItem


class Amazon_Spider_Books(CrawlSpider):
    name = 'amazon_spider_books'
    allowed_domains = ['amazon.com']
    query = 'Books'
    start_urls = ['http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + query]
    rules = [Rule
             (
                 SgmlLinkExtractor(restrict_xpaths=('//a[@class="pagnNext"]')),
                 callback='parse_products',
                 follow=True,
             )
    ]

    def parse_products(self, response):
        hxs = HtmlXPathSelector(response)
        item = AmazonItem()
        item['title'] = hxs.select('//a[@class="title"]/text()').extract()
        item['link'] = hxs.select('//a[@class="title"]/@href').extract()
        item['price'] = hxs.select('//div[@class="tp"]/table/tr[2]/td[3]/a/text()').extract()
        return item