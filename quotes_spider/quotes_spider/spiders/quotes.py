import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ('http://quotes.toscrape.com/',)
    
    def parse(self, response):
        # h1_tag=response.xpath("//h1/a/text()").extract_first()
        # all_tags=response.xpath('//*[@class="tag-item"]/a/text()').extract()
        

        quotes=response.xpath('//*[@class="quote"]')
        for quote in quotes:
                text=quote.xpath('.//*[@class="text"]/text()').extract_first() #dot: .// only for current quote, otherwise whole page's quotes
                author=quote.xpath('.//*[@itemprop="author"]/text()').extract_first()   
                tags= quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first() #['change,deep-thoughts,thinking,world']
                #quote.xpath('.//*[@class="tag"]/text()').extract() //return ['change', 'deep-thoughts', 'thinking', 'world']
            
                yield{'Text': text,
                      'Author': author,
                      'Tags': tags }
 
        
        next_page_url=response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url=response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)