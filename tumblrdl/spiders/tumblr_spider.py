from scrapy.contrib.spiders import SitemapSpider
from scrapy.selector import HtmlXPathSelector
from tumblrdl.items import TumblrItem
from scrapy.http import Request
import os

class Tumblrdl(SitemapSpider):
    name = 'tumblr'

    def __init__(self, tumblr=None, path=None):
        super(Tumblrdl, self).__init__()
        try:
            self.sitemap_urls = [ "%s/sitemap.xml" % tumblr ]
            
        except NameError:
            exit("Usage : $ scrapy crawl tumblr -a tumblr=http://securityreactions.tumblr.com path=/tmp/    ")
        
        
        if path != None:
            self.image_store_path = path
        else:
            self.image_store_path = os.getcwdu() + "/"


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        
        images = hxs.select('//img[not(contains(@src,"pixel.quantserve.com") or contains(@src,"avatar_"))]')
        name = hxs.select('//title/text()').extract()

        for image in images:
            for url in image.select('@src').extract():
                 request = Request(url, callback=self.saveme)
                 request.meta['image_name'] = name[0]
                 yield request


    def saveme(self, response):
        """Returns the media requests to download"""

        i = TumblrItem()
        i['image_url'] = response.url
        i['image'] = response.body
        i['image_name'] = response.meta['image_name']
        i['image_store_path'] = self.image_store_path

        return i