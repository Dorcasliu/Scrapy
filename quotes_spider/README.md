#### Web Scraping & Crawling with Python
Scrapy 
- Urlllib2
- beautiful soup: extracting data \
 Library: lxml 

For mac:\
$ python \
$ sudo pip install scrapy\
$ scrapy\
$ sudo install ipython


In terminal: (Eg: quotes to scrape page)\
$ scrapy\
$ scrapy startproject quotes_spider 		(folder)\
$ scrapy genspider qutotes quotes.toscrape.com 	(name of the spider, the url)

$ scrapy shell\
In[]: fetch(“url”)	\
Or : scrapy shell “url”

[] Response.xpath(‘//h1/a/text()’).extract()\
[u’Quotes to Scrape’]

[] Response.xpath(‘//h1/a/text()’).extract_first()\
u’Quotes to Scrape’

get ten tages on the page, eg: love, life…\
[] response.xpath(‘//*[@class=”tag-item”]/a/text()’) 


Selector:\
$ scrapy shell\
[]: from scrapy.selector import Selector\
sel=Selector(text=html_doc)

sel.xpath(“//p()’).extract()

sel.xpath(“//p/text()’).extract_first()

run:\
$ scrapy crawl quotes -o items.csv\
$ scrapy crawl quotes -o items.json	\
$ scrapy crawl quotes -o items.xml

[]: response.xpath('.//*[@class="next"]/a/@href').extract()\
Output: ['/page/2/']\
[]: response.xpath('.//*[@class="next"]/a/@href').extract_first()\
Output: ‘/page/2/'
