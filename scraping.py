import scrapy
from urllib.parse import urlencode
from scrapy.selector import Selector

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')

def get_scrapeops_url(url):
    payload={'api_key':api_key, 'url':url, 'bypass': 'cloudflare'}
    proxy_url='https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    print(proxy_url)
    return proxy_url

class QuotesSpider(scrapy.Spider):
    name = 'spiderJusBrasil'

    custom_settings={
        'FEEDS':{
            'quotes.csv':{
                'format': 'csv',
                'overwrite': True
            }
        }
    }
    def parse(self, response):
        quotes = response.xpath('*//div[@data-testid="search-results"]/section')
        nexts = quotes.xpath('./div/a/@href').getall() # aqui eu posso ir em cada pagina 
    
        #for quote in quotes:
        #    next = quote.xpath('./div/a/@href').extract() #acredito que o certo é eu pegar todos e depois fazer uma pesquisa um por um, por que nao da para eu ficar indo e voltando nas paginas (pelo menos nao que eu saiba)
        #    title=''.join(quote.xpath('.//h2[@class="search-results_SearchResults-title__QeJBI"]//text()').extract())
        #    yield{
        #        'title': title,
        #    }
        #    
        #    aux = quote.xpath('.//article').getall()
        #    
        #    for a in aux:
        #        selector = Selector(text=a)
        #        subtitulosAux = ''.join(selector.xpath('*//a[@data-testid="search-snippet-title-link"]//text()').getall())
        #        texto = ''.join(selector.xpath('z'//text()').getall())
        #        yield{
        #            'title': title,
        #            'subtitle': subtitulosAux,
        #            'texto': texto
        #        }

            #------------------------
            #textos = quote.xpath('.//div[@data-testid="search-snippet-base-body"]//p')        
            #for texto in textos:
            #    textoAux = ''.join(texto.xpath('.//text()').getall())
            #acabei de fazer-------------------

            #subtitulosAux =  quote.xpath('*//a[@data-testid="search-snippet-title-link"]').getall()
            #for sub in subtitulosAux:
            #    selector = Selector(text=sub)
            #    subtitle = ''.join(selector.xpath('.//text()').getall())
            #    yield{
            #        'title': title,
            #        'subtitle': subtitle
            #    }
            

    def take_information(self,response):
        quotes = response.xpath('*//div[@data-testid="search-results"]/section')
        print("chamou a função")
        #nexts = quotes.xpath('./div/a/@href').getall() # aqui eu posso ir em cada pagina 
        for quote in quotes:
            next = quote.xpath('./div/a/@href').extract() #acredito que o certo é eu pegar todos e depois fazer uma pesquisa um por um, por que nao da para eu ficar indo e voltando nas paginas (pelo menos nao que eu saiba)
            title=''.join(quote.xpath('.//h2[@class="search-results_SearchResults-title__QeJBI"]//text()').extract())
            
            aux = quote.xpath('.//article').getall()
            
            for a in aux:
                selector = Selector(text=a)
                subtitulosAux = ''.join(selector.xpath('*//a[@data-testid="search-snippet-title-link"]//text()').getall())
                texto = ''.join(selector.xpath('.//div[@data-testid="search-snippet-base-body"]//p//text()').getall())
                yield{
                    'title': title,
                    'subtitle': subtitulosAux,
                    'texto': texto
                }
                
    def start_requests(self):
        urlCentral = 'https://www.jusbrasil.com.br/busca?q='
        termos = ['segurança de dados', 'proteção de dados']
        urls=['https://www.jusbrasil.com.br/busca?q=seguran%C3%A7a+de+dados']
        
        for url in urls:
            yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse)
        #for termo in termos:
        #    yield scrapy.Request(url=get_scrapeops_url(urlCentral+termo), callback=self.take_information)

