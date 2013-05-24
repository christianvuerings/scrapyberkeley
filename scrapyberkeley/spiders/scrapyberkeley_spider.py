#http://osoc.berkeley.edu/OSOC/osoc?p_term=SP&p_list_all=Y

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from scrapyberkeley.items import ScrapyberkeleyItem


class ScrapyberkeleySpider(BaseSpider):
    name = "scrapyberkeley"
    allowed_domains = ["osoc.berkeley.edu"]
    start_urls = [
        "http://osoc.berkeley.edu/OSOC/osoc?p_term=SP&p_list_all=Y"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//tr')
        items = []
        for site in sites:
            item = ScrapyberkeleyItem()
            if site.select('td[3]/label/text()').extract():
                item['department'] = site.select('td[1]/label/text()').extract()[0]
                item['course'] = site.select('td[2]/label/text()').extract()[0].strip()
                item['title'] = site.select('td[3]/label/text()').extract()[0]
                items.append(item)
                #print item['department'], item['course'], item['title']
        return items
        #filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)
