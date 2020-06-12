from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

class LegoItem(Item):
    number = Field()
    name = Field()


class LegoCrawler(CrawlSpider):
    name = "Crawler_01"
    start_urls = ['https://brickset.com/sets/year-2020']
    allowed_domains = ['brickset.com']  # Lista de dominios permitidos

    # Restricciones que debe acatar el crawler
    rules = (
        Rule(LinkExtractor(allow=r'page-')),  # Puede ingresar a las páginas que tienen en la url la expresión regular
        Rule(LinkExtractor(allow=r'/sets/[0-9-]+[0-9]{1}'), callback='parse_items'),
    )

    # Función que es llamada cuando se cumpla la regla
    def parse_items(self, response):
        item = ItemLoader(LegoItem(), response)
        item.add_xpath('number', '//*[@id="body"]/div[1]/div/aside/section[2]/div/dl/dd[1]/text()')
        item.add_xpath('name', '//*[@id="body"]/div[1]/div/aside/section[2]/div/dl/dd[2]/text()')

        yield item.load_item()
