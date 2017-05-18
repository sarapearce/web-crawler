import scrapy


class QuotesSpider(scrapy.Spider):
    name = "trump_twit"

    def start_requests(self):
        urls = [
            'https://twitter.com/realDonaldTrump'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # full_text = response.body
        # TODO: add date to the end of the file name
        filename = 'twitter-crawl.html'
        with open(filename, 'wb') as f:
            f.write('this is the last step when im done, my big output')
        self.log('Saved file %s' % filename)
