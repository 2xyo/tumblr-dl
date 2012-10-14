from scrapy.contrib.spiders import SitemapSpider
from scrapy.selector import HtmlXPathSelector
from tumblrdl.items import TumblrItem
from scrapy.http import Request

class Tumblrdl(SitemapSpider):
    name = 'tumblr'
    sitemap_urls = ['http://securityreactions.tumblr.com/sitemap1.xml']
    #sitemap_urls = ['http://alertepelleteuse.tumblr.com/sitemap1.xml']

    def parse(self, response):
        #self.log('A response from %s just arrived!' % response.url)
        hxs = HtmlXPathSelector(response)
        
        #images = hxs.select('//img[not(contains(@src,"pixel.quantserve.com") or contains(@src,"avatar_")) and contains(@src,".gif")]')
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

        return i


