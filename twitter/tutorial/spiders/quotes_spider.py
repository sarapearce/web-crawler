import logging
import scrapy
import datetime
import json


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
        logging.info('Begin parsing the response')

        # grab html that has a class of tweet-text for parsing
        all_tweet_text = response.xpath('//*[contains(@class, "tweet-text")]/text()').extract()

        date = datetime.datetime.today().strftime('%Y-%m-%d')
        site = response.url.split("/")[-1]

        # this is unique identifier for each crawl, it is used frequently as a key
        site_date = site + date

        # assign to filename for output
        filename = '%s-twitter-crawl.html' % site_date


        # loop and grab proper nouns
        proper_nouns = []
        for tweet in all_tweet_text:
            words = tweet.split()

            for word in words:

             if word[0].isupper():
                 proper_nouns.append(word)

        print('PROPER NOUNS ARRAY')
        print(proper_nouns)

        # with open(filename, 'wb') as f:
        #     f.write(all_cleaned_by_website)
        # self.log('Saved file %s' % filename)
