from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


class Pregunta(Item):
    """Clase que define los Items
    id: corresponde al id secuencial de las preguntas
    pregunta: corresponde a la pregunta de StackOverflow
    """
    id = Field()
    pregunta = Field()


class StackOverflowSpider(Spider):
    name = "Spider_01"  # Nombre del Spider
    start_urls = ['https://es.stackoverflow.com/questions']  # url semilla

    def parse(seld, response):
        selector = Selector(response)
        # // -> Indica la raíz del arbol (padre)
        # //*[@id="questions"] -> Div con todas las preguntas
        preguntas = selector.xpath('//div[@id="questions"]/div')
        # Se itera sobre las preguntas
        for n, pregunta in enumerate(preguntas):
            # Creamos el Item
            i = ItemLoader(Pregunta(), pregunta)
            # //*[@id="question-summary-189320"]/div[2]/h3/a
            i.add_xpath('pregunta', './/h3/a[@class="question-hyperlink"]/text()')
            i.add_value('id', n)

            # retornamos el item
            yield i.load_item()
