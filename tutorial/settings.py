BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
ITEM_PIPELINES = ['tutorial.pipelines.AmazonSpiderMongoDB',]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "scrapy_spiders"
MONGODB_COLLECTION = "amazon_spider_books"