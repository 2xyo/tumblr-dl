# Scrapy settings for tumblrdl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'tumblrdl'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['tumblrdl.spiders']
NEWSPIDER_MODULE = 'tumblrdl.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['tumblrdl.pipelines.MyImagesPipeline']

