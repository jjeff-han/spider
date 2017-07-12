# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HealthItem(scrapy.Item):
    # define the fields for your item here like:
    Id = scrapy.Field()
    Head_dep = scrapy.Field()
    Level2_dep = scrapy.Field()
    Disease_ab = scrapy.Field()
    Disease_cn = scrapy.Field()
    Alias = scrapy.Field()
    Symptom = scrapy.Field()
    #ConDisease = scrapy.Field()
    Descript = scrapy.Field()
    Treatment = scrapy.Field()
#    Age = scrapy.Field()
#    Gender = scrapy.Field()
#    Patient_name= scrapy.Field()
