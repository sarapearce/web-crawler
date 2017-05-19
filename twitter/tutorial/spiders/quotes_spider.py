import logging
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "media_aggregate"

    def start_requests(self):
        urls = [
            'https://twitter.com/nytimes', 'https://twitter.com/AP', 'https://twitter.com/AJEnglish',
            'https://twitter.com/CNN', 'https://twitter.com/ABC', 'https://twitter.com/CBSNews',
            'https://twitter.com/FoxNews', 'https://twitter.com/FoxBusiness', 'https://twitter.com/NBCNewsBusiness'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        logging.info('Inside the parse function')
        # full_text = response.body
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        site = response.url.split("/")[-1]
        site_date = site + date
        filename = 'twitter-crawl-%s.html' % site_date

        with open(filename, 'wb') as f:
            f.write('this is the last step when im done, my big output')
        self.log('Saved file %s' % filename)
