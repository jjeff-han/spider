#coding=utf8

import scrapy
import re
import json
from health.items import HealthItem

class health39(scrapy.Spider):
    name = "heal"
    allowed_domains = ['39.net']
#    start_urls = ["http://jbk.39.net/bw/huxineike_t1",
#            "http://jbk.39.net/bw/huxineike_t1_p1#ps",
#            "http://jbk.39.net/bw/huxineike_t1_p2#ps",
#            ]

    def start_requests(self):
        pages=[]
        for npage in range(0,1):
            if npage == 0:
                page = scrapy.Request("http://jbk.39.net/bw/huxineike_t1")
            else:
                #npage = npage + 1
                un = str(npage)
                header = "/bw/huxineike_t1_p"
                tail = "#ps"
                url = "http://jbk.39.net" + header + un + tail
                page = scrapy.Request(url)
            pages.append(page)
        return pages

    def parse(self, response):
        #jbItem = HealthItem()
        print response.url
        for hel in response.xpath('//div[@id="res_tab_2"]/div[@class="res_list"]'):
           # yield {'url':hel.xpath('./dl/dt/h3/a/@href').extract_first(),
            #        'name':hel.xpath('./dl/dt/h3/a/text()').extract()        }
            #jbItem['Alias'] = hel.xpath('./dl/dt/h3/a/@href').extract_first()
            #jbItem['Name_cn'] = hel.xpath('./dl/dt/h3/a/text()').extract() 
            #yield jbItem
            detail = hel.xpath('./dl/dt/h3/a/@href').extract_first()
            detailPage = detail + 'jbzs'
            yield scrapy.Request(detailPage, callback=self.parse_detail)
            #yield scrapy.Request(detail, meta={'item':jbItem}, callback=self.parse_detail)

    def parse_detail(self, response):
        jbItem = HealthItem()
        regexc = re.compile(u"http://jbk.39.net\/(.+)\/zztz/")
        print response.url
        #jbItem = response.meta['item']
        jbItem['Id'] = response.url
        jbItem['Head_dep'] = '内科'
        jbItem['Level2_dep'] = '呼吸内科'
        abstring = response.xpath('//div[@class="chi-know"]/dl/dd/a[@    class="more"]/@href').extract_first() 
        jbItem['Disease_ab'] =  regexc.findall(abstring)
        jbItem['Disease_cn'] =  response.xpath('//div[@class="chi-know"]/dl/dt/text()').extract_first()[:-2]
        jbItem['Alias'] = response.xpath('//div[@class="chi-know"]/dl/dd/text()').extract()[1]
        SymptomUrl =  response.xpath('//div[@class="chi-know"]/dl/dd/a[@class="more"]/@href').extract_first()
        jbItem['Descript']= response.xpath('//div[@class="chi-know"]/dl/dd/text()').extract_first()
        jbItem['Treatment'] = response.url.replace('jbzs','yyzl')
        yield scrapy.Request(SymptomUrl, meta = {'jbItem':jbItem}, callback=self.parse_symptom)
        #response.xpath('//div[@class="chi-know"]/dl/dd/a/text()').extract()[3:8]
        #print jbItem
        #return jbItem
    def parse_symptom(self, response):
        jbItem = response.meta['jbItem']
        jbItem['Symptom'] = response.xpath('//div[@class="chi-know chi-int"]/dl[@class="links"]/dd/a/text()').extract()
        return jbItem


    
