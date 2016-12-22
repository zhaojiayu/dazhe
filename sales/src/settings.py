# Scrapy settings for getmovieurl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'src'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['src.spiders']
NEWSPIDER_MODULE = 'src.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = {'src.pipelines.GetMarketPipeline'}