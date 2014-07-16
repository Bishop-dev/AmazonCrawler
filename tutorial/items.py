from scrapy.item import Item, Field


class AmazonItem(Item):
    title = Field()
    link = Field()
    price = Field()