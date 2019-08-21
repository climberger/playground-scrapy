import scrapy
from ..items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # title = response.css('title::text').extract()
        # title = response.css('title::text')[0].extract()
        # title = response.css('title::text').extract_first()
        # title = response.xpath('//title').extract()
        # title = response.xpath('//title/text()').extract()
        # text = response.xpath('//span[@class="text"]/text()').extract()
        # next_link = response.css('li.next a').xpath('@href').extract()
        # get all links of hrefs
        # href_links = response.css('a').xpath('@href').extract()

        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            text = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()

            item = QuoteItem()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

            # yield {
            #     'text': text,
            #     'author': author,
            #     'tags': tags
            # }
