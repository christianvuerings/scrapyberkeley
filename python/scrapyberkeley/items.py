# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class ScrapyberkeleyItem(Item):
    # define the fields for your item here like:
    # name = Field()
    department = Field()
    course = Field()
    title = Field()