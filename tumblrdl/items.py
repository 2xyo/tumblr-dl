# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TumblrItem(Item):
    # define the fields for your item here like:
    # name = Field()
    image_url = Field()
    image = Field()
    image_name = Field()
    image_store_path = Field()